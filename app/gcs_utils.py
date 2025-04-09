from google.cloud import storage
import os
from dotenv import load_dotenv

load_dotenv()
bucket_name = os.getenv("GCS_BUCKET") 

def upload_to_gcs(local_file_path: str, content: str, file_name: str, folder: str):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    
    if content:
        blob = bucket.blob(f"{folder}/{file_name}.txt")
        blob.upload_from_string(content)
        print(f"✅ Uploaded transcript to {folder}/{file_name}.txt")
    else:
        blob = bucket.blob(f"{folder}/{file_name}.wav")
        blob.upload_from_filename(local_file_path)
        print(f"✅ Uploaded audio to {folder}/{file_name}.wav")
