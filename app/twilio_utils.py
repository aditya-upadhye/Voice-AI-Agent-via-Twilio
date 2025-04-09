import requests
import os
import time
from dotenv import load_dotenv
import logging

from app.gcs_utils import upload_to_gcs

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
GCS_BUCKET = os.getenv("GCS_BUCKET")

def download_twilio_audio(recording_url: str, save_path: str):
    """Download audio recording from Twilio."""
    recording_sid = recording_url.split("/")[-1]
    recording_api_url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_ACCOUNT_SID}/Recordings/{recording_sid}.json"

    for _ in range(5): 
        response = requests.get(recording_api_url, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
        
        if response.status_code == 200:
            recording_data = response.json()
            print(f"✅ Recording details: {recording_data}")
            
            if recording_data['status'] == 'completed':
                audio_url = recording_data['media_url'] + '.wav'
                audio_response = requests.get(audio_url, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
                
                if audio_response.status_code == 200:
                    with open(save_path, "wb") as f:
                        f.write(audio_response.content)
                    print(f"✅ Audio saved to {save_path}")
                    return True
                else:
                    print(f"❌ Failed to download audio: {audio_response.status_code} - {audio_response.text}")
                    return False
            else:
                print(f"❌ Recording is still processing, retrying in 2 seconds...")
                time.sleep(2)
        else:
            print(f"❌ Failed to fetch recording details: {response.status_code} - {response.text}")
            return False

    print("❌ Failed to download audio after multiple attempts.")
    return False


def handle_status_callback(form_data, session_transcript, call_sid, audio_path):
    """Handle the call status callback from Twilio."""
    call_status = form_data.get("CallStatus")
    print(f"Call SID: {call_sid} Status: {call_status}")

    if call_status == "completed":
        print(f"Call {call_sid} was completed.")
        upload_to_gcs(audio_path, session_transcript, call_sid)
        
    elif call_status == "busy":
        print(f"Call {call_sid} was busy.")

    elif call_status == "failed":
        print(f"Call {call_sid} failed.")

    elif call_status == "no-answer":
        print(f"Call {call_sid} was not answered.")

    return {"status": "success"}
