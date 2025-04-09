from fastapi import FastAPI, Form, Request, APIRouter
from fastapi.responses import Response
from twilio.twiml.voice_response import VoiceResponse
from app.twilio_utils import download_twilio_audio, handle_status_callback
import os
import logging
from dotenv import load_dotenv
from app.transcriber import transcribe_audio
from app.gcs_utils import upload_to_gcs
from app.agentsdk import get_agent_response

load_dotenv()
router = APIRouter()
app = FastAPI()
logging.basicConfig(level=logging.INFO)

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
GCS_BUCKET = os.getenv("GCS_BUCKET")

session_transcript = ""

@app.post("/voice")
async def voice_handler(request: Request):
    response = VoiceResponse()

    response.say("Hi! Please leave your message after the beep.", voice="alice")

    response.record(
        timeout=4,  
        max_length=30,  
        action="/recording",  
        method="POST",  
        play_beep=True,  
        status_callback="/status_callback",  
        status_callback_method="POST"
    )

    return Response(content=str(response), media_type="application/xml")


@app.post("/recording")
async def recording_handler(request: Request):
    global session_transcript  

    form = await request.form()
    recording_url = form.get("RecordingUrl")
    call_sid = form.get("CallSid")

    print(f"📞 Final Recording URL: {recording_url}")
    print(f"📼 CallSid: {call_sid}")

    if not recording_url:
        return Response("No recording received", status_code=400)

    audio_path = f"/tmp/{call_sid}.wav"
    
    download_successful = download_twilio_audio(recording_url, audio_path)

    if not download_successful:
        return Response("Failed to download the audio file", status_code=500)

    try:
        transcript = transcribe_audio(audio_path)

        session_transcript += f"\n{transcript}"

        response_json = get_agent_response(transcript)
        
        response = VoiceResponse()
        if "goodbye" in transcript.lower() or "bye" in transcript.lower() or "end call" in transcript.lower():
            response.say("Thank you for calling. Goodbye!", voice='alice')
            response.hangup()
            # Corrected to pass folder
            upload_to_gcs(audio_path, session_transcript, call_sid, "recordings")
            upload_to_gcs(audio_path, session_transcript, call_sid, "transcripts")
            
        else:
            response.say(response_json, voice='alice')
            response.say("Do you have another question?", voice='alice')
            response.record(
                timeout=4,
                max_length=30,
                action="/recording",
                method="POST",
                play_beep=True
            )

        return Response(content=str(response), media_type="application/xml")

    except Exception as e:
        print(f"❌ Error during transcription or AI response: {str(e)}")
        return Response("Error processing the message", status_code=500)


@app.post("/status_callback")
async def status_callback(request: Request):
    form_data = await request.form()
    call_sid = form_data.get("CallSid")
    call_status = form_data.get("CallStatus")
    logging.info(f"Call SID: {call_sid}, Status: {call_status}")
    if call_status == "completed":
        logging.info(f"Call {call_sid} completed.")
        audio_path = f"/tmp/{call_sid}.wav"  
        try:
            upload_to_gcs(audio_path, None, call_sid, "recordings")
            upload_to_gcs(None, session_transcript, call_sid, "transcripts")
        except Exception as e:
            logging.error(f"Error uploading transcript for Call {call_sid}: {str(e)}")

    elif call_status == "busy":
        logging.info(f"Call {call_sid} was busy.")
    elif call_status == "failed":
        logging.info(f"Call {call_sid} failed.")
    elif call_status == "no-answer":
        logging.info(f"Call {call_sid} was not answered.")
    return {"status": "success"}