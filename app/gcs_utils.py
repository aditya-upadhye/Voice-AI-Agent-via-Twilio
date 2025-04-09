from google.cloud import storage
import os
if os.getenv("ENV") != "production":
    from dotenv import load_dotenv
    load_dotenv()

bucket_name = os.getenv("GCS_BUCKET") 

def upload_to_gcs(local_file_path: str, content: str, file_name: str, folder: str):
    try:
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        
        if content:
            if folder != "transcripts":
                raise ValueError("Transcript content must be uploaded to the 'transcripts/' folder.")
            blob = bucket.blob(f"{folder}/{file_name}.txt")
            blob.upload_from_string(content)
            print(f"✅ Uploaded transcript to {folder}/{file_name}.txt")
        else:
            if folder != "recordings":
                raise ValueError("Audio files must be uploaded to the 'recordings/' folder.")
            blob = bucket.blob(f"{folder}/{file_name}.wav")
            blob.upload_from_filename(local_file_path)
            print(f"✅ Uploaded audio to {folder}/{file_name}.wav")
        return True
    except Exception as e:
        print(f"❌ Error uploading to GCS: {str(e)}")
        import traceback
        traceback.print_exc()
        return False