import os
from google.cloud import speech
import io

def transcribe_audio(audio_path):
    client = speech.SpeechClient()

    with io.open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16, 
        language_code="en-US",
        sample_rate_hertz=8000  # I'll decide the sample rate based on the audio file
    )

    try:
        response = client.recognize(config=config, audio=audio)

        if not response.results:
            print("No results found in the transcription response.")
            return None

        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript

        if not transcript:
            print("No transcript available.")
        else:
            print("Transcript: ", transcript)

        return transcript

    except Exception as e:
        print(f"Error during transcription: {e}")
        return None
