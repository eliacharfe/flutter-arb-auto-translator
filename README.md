# 🌍 Flutter ARB Auto Translator

Automatically translate Flutter `.arb` localization files using the Google Translate API - while safely preserving placeholder variables like `{name}`, `{count}`, etc.

This tool reads a source ARB file (e.g. `intl_en.arb`) and generates a fully translated ARB file (e.g. `intl_fr.arb`) without breaking dynamic placeholders or metadata entries.

---

## ✨ Why This Exists

When building multilingual Flutter apps, maintaining large `.arb` files can become:

- Time-consuming  
- Error-prone  
- Hard to scale  

This tool automates full-file translation while:

- Preserving `{placeholders}`
- Keeping `@metadata` entries intact
- Generating properly formatted `.arb` output
- Preventing accidental placeholder corruption

---

## 🚀 Features

- ✅ Full ARB file translation  
- ✅ Placeholder protection (`{name}`, `{count}` etc.)  
- ✅ Metadata preservation (`@key` entries)  
- ✅ UTF-8 safe output  
- ✅ Environment-based API key configuration  
- ✅ Simple, lightweight setup  

---

## 📦 Example

### Input (`intl_en.arb`)

```json
{
  "welcome_message": "Hello {name}, welcome back!",
  "@welcome_message": {
    "description": "Greeting message with username"
  },
  "home_title": "Awesome Home Screen"
}
```

### Output (`intl_fr.arb`)

```json
{
  "welcome_message": "Bonjour {name}, bon retour !",
  "@welcome_message": {
    "description": "Greeting message with username"
  },
  "home_title": "Écran d'accueil incroyable"
}
```

Notice that:

- `{name}` is preserved
- Metadata stays untouched
- Structure remains valid

---

# 🛠 Setup Instructions

## 1️⃣ Enable Google Translate API

Go to:

https://console.cloud.google.com/marketplace/product/google/translate.googleapis.com

Enable the API for your project.

---

## 2️⃣ Create an API Key

In Google Cloud Console:

APIs & Services → Credentials → Create API Key

Copy your generated key.

---

## 3️⃣ Create a `.env` File (Important)

In the project root directory, create a file named:

`.env`

Inside it, add:

```
GOOGLE_TRANSLATE_API_KEY=your_real_api_key_here
```

⚠️ Never commit this file to GitHub.

---

## 4️⃣ Install Dependencies

It is recommended to use a virtual environment.

### macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Then install requirements:

```bash
pip install -r requirements.txt
```

### Required Packages

- `requests`
- `python-dotenv`

---

## 5️⃣ Configure Target Language

Inside `main.py`, set:

```python
TARGET_LANG = "fr"
TARGET_FILE_NAME = "intl_fr.arb"
```

Use ISO language codes:

| Language | Code |
|----------|------|
| French   | fr   |
| Spanish  | es   |
| Hebrew   | he   |
| Russian  | ru   |
| German   | de   |

---

## 6️⃣ Add Your Source File

Make sure your source file exists:

`intl_en.arb`

It must be in the same directory as the script.

---

## 7️⃣ Run the Script

```bash
python main.py
```

Your translated file will be generated automatically.

---

# 🔐 Security Notes

Add this to your `.gitignore`:

```
.env
venv/
__pycache__/
```

Never expose your API key publicly.

---

# 💰 Cost Considerations

Google Translate API is a paid service.

Billing depends on:
- Total characters translated
- Monthly usage

Check pricing here:
https://cloud.google.com/translate/pricing

---

# 🧠 How It Works

1. Loads `intl_en.arb`
2. Iterates through all keys
3. Skips metadata entries (`@key`)
4. Protects placeholders using temporary tokens
5. Sends text to Google Translate API
6. Restores placeholders
7. Writes translated `.arb` file

---

# 📁 Recommended Project Structure

```
flutter-arb-auto-translator/
│
├── translate_arb.py
├── intl_en.arb
├── README.md
├── .env              (local only – NOT committed)
└── .gitignore
```

---

# 🎯 Use Cases

- Flutter app localization
- Rapid multilingual expansion
- Internal developer tooling
- CI-based localization workflows
- Pre-release language generation

---



