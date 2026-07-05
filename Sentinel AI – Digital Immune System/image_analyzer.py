import os
import uuid

from ai_explainer import explain_image


def analyze_image(image, upload_folder):

    # ==========================
    # Save Uploaded Image
    # ==========================

    extension = os.path.splitext(image.filename)[1]

    filename = f"{uuid.uuid4().hex}{extension}"

    image_path = os.path.join(upload_folder, filename)

    image.save(image_path)

    # ==========================
    # Gemini Analysis
    # ==========================

    ai_response = explain_image(image_path)

    # ==========================
    # Simple Image Classification
    # (Later we'll make this AI-powered)
    # ==========================

    lower = ai_response.lower()

    category = "🖼 Image Analysis"
    risk = "Low"
    target = "Unknown"
    confidence = "95%"
    severity = "Informational"
    action = "Review AI Analysis"
    score = 15
    color = "#22c55e"

    if "phishing" in lower:

        category = "🎣 Credential Phishing"
        risk = "Critical"
        target = "Passwords"
        confidence = "98%"
        severity = "High"
        action = "Do NOT trust this page."
        score = 95
        color = "#ef4444"

    elif "bank" in lower:

        category = "🏦 Banking Scam"
        risk = "Critical"
        target = "Bank Account"
        confidence = "97%"
        severity = "High"
        action = "Avoid entering banking details."
        score = 92
        color = "#ef4444"

    elif "paypal" in lower:

        category = "💳 Payment Scam"
        risk = "Critical"
        target = "Payment Credentials"
        confidence = "97%"
        severity = "High"
        action = "Never login using this page."
        score = 94
        color = "#ef4444"

    elif "certificate" in lower:

        category = "📄 Safe Document"
        risk = "Very Low"
        target = "None"
        confidence = "99%"
        severity = "Safe"
        action = "Document appears legitimate."
        score = 5
        color = "#22c55e"

    elif "qr" in lower:

        category = "📱 QR Code"
        risk = "Medium"
        target = "Unknown"
        confidence = "92%"
        severity = "Warning"
        action = "Verify before scanning."
        score = 45
        color = "#f59e0b"

    # ==========================
    # Return Result
    # ==========================

    return {

        "result": "🖼 Screenshot Analysis",

        "score": score,

        "color": color,

        "reasons": [
            "Screenshot analyzed using Gemini Vision."
        ],

        "advice": [
            "Review the AI findings carefully.",
            "Verify suspicious websites manually.",
            "Never enter passwords on unknown pages."
        ],

        "ai_response": ai_response,

        "image_path": f"/static/uploads/{filename}",

        "threat": {

            "category": category,

            "risk": risk,

            "target": target,

            "confidence": confidence,

            "severity": severity,

            "action": action

        }

    }