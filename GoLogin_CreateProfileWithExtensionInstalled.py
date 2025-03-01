import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch credentials securely from .env
GOLOGIN_API_TOKEN = os.getenv('GOLOGIN_API_TOKEN')
EXTENSION_ID = 'nomnklagbgmgghhjidfhnoelnjfndfpd'

url = 'https://api.gologin.com/browser'

headers = {
    'Authorization': f'Bearer {GOLOGIN_API_TOKEN}',
    'Content-Type': 'application/json'
}

payload = {
    "name": "Ubuntu_Chrome_Profile2",
    "os": "lin",
    "browserType": "chrome",
    "extensions": [
        {"id": EXTENSION_ID}
    ],
    "navigator": {
        "userAgent": "random",
        "resolution": "1920x1080",  # Explicit resolution
        "language": "en-US",
        "platform": "Linux x86_64"  # Explicit platform
    },
    "proxy": {
        "mode": "none"
    },
    "webGL": {
        "mode": "noise"
    },
    "canvas": {
        "mode": "noise"
    },
    "webRTC": {
        "mode": "alerted"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 201:
    print("Profile created successfully:")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Failed to create profile: {response.status_code}")
    print(response.text)
