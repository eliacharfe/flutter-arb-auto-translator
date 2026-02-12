
"""
Flutter ARB Auto Translator
----------------------------

This script automatically translates a Flutter `.arb` localization file
using the Google Translate API while preserving placeholder variables
such as {name}, {count}, etc.

It reads `intl_en.arb` and generates a translated `.arb` file
(e.g., intl_fr.arb) in the same directory.

------------------------------------------------------------
SETUP INSTRUCTIONS
------------------------------------------------------------

1. Enable Google Cloud Translate API

   Visit:
   https://console.cloud.google.com/marketplace/product/google/translate.googleapis.com

   Enable the API for your project.

2. Generate an API Key

   In Google Cloud Console:
   APIs & Services → Credentials → Create API Key

3. Create a .env file (DO NOT commit this file)

   In the root of your project, create a file named:

       .env

   Inside it, add:

       GOOGLE_TRANSLATE_API_KEY=your_real_api_key_here

4. Install Dependencies

   It is recommended to use a virtual environment:

       python3 -m venv venv
       source venv/bin/activate  (macOS/Linux)
       venv\Scripts\activate     (Windows)

   Then install dependencies:

       pip install -r requirements.txt

   Required packages:
       - requests
       - python-dotenv

5. Configure Target Language

   In the script, set:

       TARGET_LANG = "fr"
       TARGET_FILE_NAME = "intl_fr.arb"

   Use ISO language codes (e.g., "fr", "es", "he", "ru").

6. Add Source ARB File

   Make sure `intl_en.arb` exists in the same directory
   as this script.

7. Run the Script

       python translate_arb.py

   The translated file will be generated automatically.

------------------------------------------------------------
SECURITY NOTES
------------------------------------------------------------

- Never commit your .env file.
- Add the following to your .gitignore:

      .env
      venv/
      __pycache__/

- API usage may incur billing charges depending on
  translation volume.

------------------------------------------------------------
"""

import os
import json
import requests
import re
from dotenv import load_dotenv

load_dotenv()

GOOGLE_TRANSLATE_API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")
TARGET_LANG = "fr" # set here your output language
TARGET_FILE_NAME = "intl_fr.arb" # set here your target file name

PLACEHOLDER_PATTERN = re.compile(r"\{[a-zA-Z0-9_]+}")

def protect_placeholders(text):
    placeholders = PLACEHOLDER_PATTERN.findall(text)
    protected = text
    for i, ph in enumerate(placeholders):
        protected = protected.replace(ph, f"__PH_{i}__")
    return protected, placeholders

def restore_placeholders(text, placeholders):
    restored = text
    for i, ph in enumerate(placeholders):
        restored = restored.replace(f"__PH_{i}__", ph)
    return restored

def translate(text):
    response = requests.post(
        "https://translation.googleapis.com/language/translate/v2",
        params={"key": GOOGLE_TRANSLATE_API_KEY},
        json={
            "q": text,
            "target": TARGET_LANG,
            "format": "text"
        }
    )
    return response.json()["data"]["translations"][0]["translatedText"]

def run():
    if not GOOGLE_TRANSLATE_API_KEY:
        raise ValueError("Missing GOOGLE_TRANSLATE_API_KEY. Please set it in your .env file.")

    with open("intl_en.arb", "r", encoding="utf-8") as f:
        data = json.load(f)

    translated = {}

    for key, value in data.items():
        if key.startswith("@"):
            translated[key] = value
            continue

        if not isinstance(value, str):
            translated[key] = value
            continue

        protected_text, placeholders = protect_placeholders(value)
        translated_text = translate(protected_text)
        final_text = restore_placeholders(translated_text, placeholders)

        translated[key] = final_text

    with open(TARGET_FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    run()
