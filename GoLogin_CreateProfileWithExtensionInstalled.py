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
    "name": "Ubuntu_Chrome_Profile4",
    "os": "lin",
    "browserType": "chrome",
    "chromeExtensions": [EXTENSION_ID],
    "navigator": {
        "userAgent": "random",
        "resolution": "1920x1080",
        "language": "en-US",
        "platform": "Linux x86_64"
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
    },
    "fonts": {
        "enableMasking": True,
        "enableDomRect": True,
        "families": [
            "Arial", "Courier New", "Times New Roman",
            "Verdana", "Tahoma", "Georgia"
        ]
    }
}


response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 201:
    print("Profile created successfully:")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Failed to create profile: {response.status_code}")
    print(response.text)
