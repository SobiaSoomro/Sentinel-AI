import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# =====================================================
# Sentinel AI Configuration
# =====================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


# =====================================================
# URL Analysis
# =====================================================

def explain_url(url, result, reasons):

    prompt = f"""
You are Sentinel AI.

You are an elite Cyber Security Analyst.

Analyze the following URL.

URL:
{url}

Machine Learning Prediction:
{result}

Detected Indicators:
{', '.join(reasons)}

Return ONLY the following format.

🛡 Threat Summary

(2-3 sentences)

----------------------------------

🎯 Threat Category

Examples:

Credential Phishing

Banking Scam

Crypto Scam

Shopping Scam

Government Scam

Fake Login Page

Safe Website

----------------------------------

🎯 Possible Target

Examples:

Passwords

Bank Accounts

Personal Information

Crypto Wallet

Payment Cards

----------------------------------

📊 Risk Score

Return ONLY a number from 0 to 100.

----------------------------------

📈 Confidence

Return ONLY a percentage.

Example:

96%

----------------------------------

⚠ Why was this detected?

Return 4 bullet points.

----------------------------------

💡 Security Advice

Return 4 bullet points.

----------------------------------

🎯 Final Verdict

One short sentence.

Rules:

Use simple English.

Maximum 220 words.

Never mention AI.

Use emojis where appropriate.
"""

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"""
🛡 Threat Summary

Unable to generate AI analysis.

🎯 Threat Category

Unknown

🎯 Possible Target

Unknown

📊 Risk Score

0

📈 Confidence

0%

⚠ Why was this detected?

• Gemini API unavailable.

💡 Security Advice

• Check your API Key.
• Check your Internet connection.
• Enable Gemini API.
• Try again later.

🎯 Final Verdict

Analysis Failed.

Error:

{e}
"""


# =====================================================
# Image Analysis
# =====================================================

def explain_image(image_path):

    prompt = """
You are Sentinel AI.

You are a Cyber Security Expert.

Analyze the uploaded image carefully.

The image may contain:

• Login Page
• Fake Website
• Certificate
• Email
• QR Code
• WhatsApp Chat
• Payment Screen
• Browser Screenshot
• Government Portal
• Bank Website

Return ONLY this format.

🖼 Image Type

Examples:

Certificate

Login Page

QR Code

Email

Bank Website

Website Screenshot

Browser

----------------------------------

🎯 Threat Category

Examples:

Safe Document

Credential Phishing

QR Scam

Email Scam

Banking Scam

Fake Website

Malware

Safe Image

----------------------------------

📊 Risk Score

Return ONLY one number between 0 and 100.

----------------------------------

📈 Confidence

Return ONLY percentage.

----------------------------------

🎯 Possible Target

Examples:

Passwords

Personal Data

Money

Identity

None

----------------------------------

⚠ Why?

Give exactly four bullet points.

----------------------------------

💡 Safety Advice

Give exactly four bullet points.

----------------------------------

🎯 Final Verdict

One short sentence.

Rules:

Maximum 220 words.

Use simple English.

Never mention AI.

Never explain your reasoning.
"""

    try:

        image = Image.open(image_path)

        response = model.generate_content(
            [prompt, image]
        )

        return response.text

    except Exception as e:

        return f"""
🖼 Image Type

Unknown

🎯 Threat Category

Unknown

📊 Risk Score

0

📈 Confidence

0%

🎯 Possible Target

Unknown

⚠ Why?

• Unable to analyze image.

💡 Safety Advice

• Verify your Gemini API Key.
• Check Internet connection.
• Upload a supported image.
• Try again later.

🎯 Final Verdict

Image Analysis Failed.

Error:

{e}
"""