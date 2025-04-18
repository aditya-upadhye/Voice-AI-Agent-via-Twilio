# 📞 Voice Assistant with FastAPI, Twilio, Google Cloud & LLaMA 3(using Groq API)

<p align="center"> <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="225" height="90"/> <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 133 48" class="customer-logo" width="180" height="90>
<title>Twilio logo</title>
  <g class="twilio">
    <g class="path-fill logo-fill">
<path d="M15 32.8462C17.1242 32.8462 18.8461 31.1242 18.8461 29C18.8461 26.8758 17.1242 25.1539 15 25.1539C12.8758 25.1539 11.1538 26.8758 11.1538 29C11.1538 31.1242 12.8758 32.8462 15 32.8462ZM15 22.8462C17.1242 22.8462 18.8461 21.1242 18.8461 19C18.8461 16.8758 17.1242 15.1538 15 15.1538C12.8758 15.1538 11.1538 16.8758 11.1538 19C11.1538 21.1242 12.8758 22.8462 15 22.8462ZM25 32.8462C27.1242 32.8462 28.8462 31.1242 28.8462 29C28.8462 26.8758 27.1242 25.1539 25 25.1539C22.8758 25.1539 21.1538 26.8758 21.1538 29C21.1538 31.1242 22.8758 32.8462 25 32.8462ZM25 22.8462C27.1242 22.8462 28.8462 21.1242 28.8462 19C28.8462 16.8758 27.1242 15.1538 25 15.1538C22.8758 15.1538 21.1538 16.8758 21.1538 19C21.1538 21.1242 22.8758 22.8462 25 22.8462ZM20 4C30.8333 4 40 13.1667 40 24C40 34.8333 30.8333 44 20 44C9.16668 44 0 34.8333 0 24C0 13.1668 9.16673 4 20 4ZM20 9.38461C11.9512 9.38461 5.38462 15.7238 5.38462 23.7315C5.38462 31.7392 11.9512 38.6154 20 38.6154C28.0488 38.6154 34.6154 31.7392 34.6154 23.7315C34.6154 15.7238 28.0488 9.38461 20 9.38461ZM62.6848 35.9231H68.9693C69.1955 35.9231 69.2924 35.8262 69.357 35.6L71.4382 27.9166L73.4572 35.6C73.5218 35.8262 73.6187 35.9231 73.8449 35.9231H80.1268C80.3852 35.9231 80.5468 35.8262 80.6114 35.6L85.0011 19.3077V35.5354C85.0011 35.7615 85.1626 35.9231 85.3888 35.9231H92.3026C92.5287 35.9231 92.6903 35.7615 92.6903 35.5354V18.6185C92.6903 18.3923 92.5287 18.2308 92.3026 18.2308L78.8307 18.2321C78.6046 18.2321 78.4753 18.3291 78.4107 18.5875L76.8848 26.4076L75.3482 18.5875C75.3159 18.3614 75.1544 18.2321 74.9282 18.2321H68.0901C67.8639 18.2321 67.7024 18.3614 67.6701 18.5875L66.1738 26.4076L64.6823 18.5875C64.6177 18.3291 64.4885 18.2321 64.2623 18.2321L54.0538 18.2308V12.4678C54.0538 12.177 53.8536 12.0478 53.5306 12.1447L47.1123 14.215C46.8861 14.2796 46.7569 14.4735 46.7569 14.6996L46.7494 17.4155C46.7494 18.094 46.394 18.3847 45.7155 18.3847H44.0563C43.8301 18.3847 43.6685 18.5462 43.6685 18.7724V23.6139C43.6685 23.8401 43.8301 24.0016 44.0563 24.0016H46.5385V29.8815C46.5385 34.0492 48.1785 36.4046 53.1861 36.4046C55.1246 36.4046 56.7092 36.1555 57.5493 35.7678C57.8077 35.6386 57.9 35.477 57.9 35.2186V30.6413C57.9 30.3828 57.6462 30.2536 57.3231 30.4151C56.9031 30.609 56.4169 30.6413 55.9323 30.6413C54.64 30.6413 54.2276 30.1567 54.2276 28.5413V24.0016H57.238C57.4642 24.0016 57.6149 23.8518 57.6149 23.6257V19.3077L62.2002 35.6C62.2648 35.8262 62.4263 35.9231 62.6848 35.9231ZM85.0011 16.3053C85.0011 16.5315 85.1626 16.6931 85.3888 16.6931H92.3026C92.5287 16.6931 92.6903 16.5315 92.6903 16.3053V12.4678C92.6903 12.2416 92.5287 12.0801 92.3026 12.0801H85.3888C85.1626 12.0801 85.0011 12.2416 85.0011 12.4678V16.3053ZM94.2299 35.5354C94.2299 35.7615 94.3914 35.9231 94.6176 35.9231H101.539C101.765 35.9231 101.926 35.7615 101.926 35.5354V12.4678C101.926 12.2416 101.765 12.0801 101.539 12.0801H94.6176C94.3914 12.0801 94.2299 12.2416 94.2299 12.4678V35.5354ZM103.465 35.5354C103.465 35.7615 103.627 35.9231 103.853 35.9231H110.755C110.982 35.9231 111.143 35.7615 111.143 35.5354L111.139 18.6185C111.139 18.3923 110.978 18.2308 110.752 18.2308H103.849C103.623 18.2308 103.462 18.3923 103.462 18.6185L103.465 35.5354ZM103.462 16.3053C103.462 16.5315 103.623 16.6931 103.849 16.6931H110.755C110.982 16.6931 111.143 16.5315 111.143 16.3053L111.139 12.4678C111.139 12.2416 110.978 12.0801 110.752 12.0801H103.849C103.623 12.0801 103.462 12.2416 103.462 12.4678V16.3053ZM112.352 27.2323C112.352 32.4985 116.395 36.4615 122.308 36.4615C128.22 36.4615 132.228 32.4985 132.228 27.2323V26.8123C132.228 21.5462 128.22 17.6923 122.308 17.6923C116.395 17.6923 112.352 21.5462 112.352 26.8123V27.2323ZM119.769 27.2462V26.9307C119.769 24.5077 120.886 23.56 122.308 23.56C123.729 23.56 124.852 24.5077 124.852 26.9307V27.2462C124.852 29.637 123.729 30.6369 122.308 30.6369C120.886 30.6369 119.769 29.637 119.769 27.2462Z" fill="#F22F46"></path>
    </g>
  </g>
</svg> <img src="https://cloud.google.com/images/social-icon-google-cloud-1200-630.png" alt="Google Cloud" width="180" height="90"/> <img loading="lazy" decoding="async" width="158" height="150" src="https://groq.com/wp-content/uploads/2024/03/PBG-mark1-color.svg" class="attachment-full size-full wp-image-3603" alt="Groq"> </p>

## This project is a conversational voice assistant built using:

- Groq’s LLaMA 3 for natural language responses

- Twilio for phone call interactions

- Google Speech-to-Text for audio transcription

- Google Cloud Storage for audio/transcript archiving

- FastAPI backend

## 📂 Project Structure

```
app/
│
├── agentsdk.py           # Handles communication with the Groq LLaMA model
├── gcs_utils.py          # Uploads audio and transcript to Google Cloud Storage
├── transcriber.py        # Google STT transcription logic
├── twilio_utils.py       # Twilio-specific helper functions
├── main.py               # FastAPI application entry point
requirements.txt          # Python dependencies
.env                      # Environment variables (local use)
```

## How It Works

1. A user calls the Twilio number.

2. The bot prompts the user to ask a question.

3. The message is recorded and saved temporarily.

4. The audio is transcribed via Google Speech-to-Text.

5. The transcription is fed to Groq's LLaMA3 to generate a conversational response.

6. The conversation continues until the user says a termination keyword like “bye” or hangs up the call.

7. Audio and transcript are uploaded to Google Cloud Storage.

## Local Setup

1.  Install Dependencies

```
pip install -r requirements.txt
```

2. Set Up Environment Variables

- Create a .env file in the root directory with the following contents:

```
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
GCS_BUCKET=your-gcs-bucket-name
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/credentials.json
```

> ✅ Place your credentials.json file (Google Cloud service account key) inside a secure location on your machine.

3. Start the FastAPI Server

```
   uvicorn app.main:app --reload --port 8000
```

4. Expose Locally Using Ngrok (For Twilio Webhook)
   Install Ngrok and run:

```
ngrok http 8000
```

Update your Twilio webhook settings (for voice calls) to point to:

```
https://<ngrok-url>/voice
```

Update the **Call status changes** to point to:

```
https://<ngrok-url>/status_callback
```

---

## Deploying on Google Cloud App Engine (Standard Environment)

1. Set Up Your GCP Project

- Make sure your Google Cloud project is initialized and App Engine is enabled.

```
gcloud init
gcloud app create --region=us-central
```

> Replace `us-central` with your desired region if needed.

2. 🗂️ Project Structure for Google Cloud App Engine

```
.
├── app/
│   ├── agentsdk.py
│   ├── gcs_utils.py
│   ├── transcriber.py
│   └── twilio_utils.py
├── main.py
├── requirements.txt
├── app.yaml              ← Required for App Engine deployment
├── credentials.json      ← (Optional) If not using env-based auth
```

> Clone **this** repository

3. Deploy to App Engine

- From your project root, run:

```
gcloud app deploy
```

- Follow the prompts and confirm the deployment. Once complete, your service will be live at:

```
https://<your-project-id>.appspot.com
```

4. Set Twilio Webhooks

- Update your Twilio number’s **Voice & Fax → A Call Comes In** field to:

```
https://<your-project-id>.appspot.com/voice
```

- Update the **Call status changes** to:

```
https://<your-project-id>.appspot.com/status_callback
```
