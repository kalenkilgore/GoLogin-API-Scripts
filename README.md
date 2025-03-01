# GoLogin Browser Profile Creator with Extension

This script automatically creates a new browser profile on GoLogin with a Chrome extension pre-installed.

### What Does This Script Do?
- Creates a new GoLogin browser profile.
- Automatically pre-installs a specified Chrome extension.
- Sets browser fingerprint settings (user agent, resolution, language, and platform).
- Enhances privacy by applying randomization (noise) for WebGL and Canvas data.

---

## Setup Instructions

### Step 1: Install Python

**Windows and Mac:**
- Go to [Python.org](https://www.python.org/downloads/) and download Python.
- Run the installer and follow the prompts. Check "Add Python to PATH" when installing.

**Ubuntu:**
Open Terminal (Ctrl + Alt + T) and run:
```
sudo apt update
sudo apt install python3 python3-pip -y
```

---

### Step 2: Download the Script

- Download this repository or copy the script code and save it as `create_gologin_profile.py`.

---

### Step 3: Install Required Python Libraries

Open your terminal (Ubuntu/Mac) or Command Prompt (Windows):
```
pip install requests python-dotenv
```

---

### Step 4: Set Up Your GoLogin API Token

- Create an account at [GoLogin](https://gologin.com/).
- Go to your dashboard and navigate to **Settings > API** to find your API token.
- Copy the token.

Create a `.env` file in the same folder as your script:
```
GOLOGIN_API_TOKEN=your_actual_api_token_here
```
Replace `your_actual_api_token_here` with your copied token.

---

### Step 5: Run the Script

Open Terminal (Ubuntu/Mac) or Command Prompt (Windows), navigate to the folder containing the script, and run:
```
python create_gologin_profile.py
```

---

## Verifying Success

- The script will output details of the created browser profile.
- Log in to [GoLogin](https://app.gologin.com/) to see the new profile with the pre-installed extension.

---

## Customizing the Extension

To change the Chrome extension, edit the line in the script:
```python
EXTENSION_ID = 'your_extension_id_here'
```
Replace `'your_extension_id_here'` with the ID of your desired Chrome extension.

---

### Troubleshooting Common Errors

- If profile creation fails, double-check your API token and internet connection.
- Ensure `.env` file is in the same folder as the script.
