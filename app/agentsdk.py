import os
import requests
import json
import re
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'

def clean_response(text: str) -> str:
    return re.sub(r"[\"'*`~^|\\/\[\]{}<>=@#$%&;:]", "", text)

def get_agent_response(prompt: str) -> str:
    headers = {
        'Authorization': f'Bearer {GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful and conversational voice assistant. "
                    "Keep responses friendly, clear, and concise — around 50 words or less. "
                    "Avoid using special characters like quotation marks, asterisks, or other symbols that could confuse voice output systems. "
                    "Basic punctuation like commas, periods, and question marks is fine."
                    "Do not ask me any questions. "
                    )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    
    try:
        response = requests.post(GROQ_API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()

        print(f"Groq API response status: {response.status_code}")
        print(f"Groq API response body: {response.text}")
        
        response_json = response.json()

        if "choices" not in response_json:
            print(f"Error: 'choices' key not found in response. Response keys: {response_json.keys()}")
            return "I'm sorry, there was an issue processing your request."
        
        content = response_json["choices"][0]["message"]["content"]
        return clean_response(content)
        
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return "I'm sorry, there was an issue connecting to the language model."
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}, Response content: {response.text}")
        return "I'm sorry, there was an issue processing the response."
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "I'm sorry, an unexpected error occurred."
