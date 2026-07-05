import pandas as pd
from extract_features import extract_features
from ai_explainer import explain_url
from threat_classifier import classify_threat


def analyze_url(url, model):

    url_features = extract_features(url)

    feature_df = pd.DataFrame([url_features])

    prediction = model.predict(feature_df)[0]

    probability = model.predict_proba(feature_df)[0]

    spam_score = round(probability[1] * 100)

    if prediction == 1:

        result = "🚨 HIGH RISK"

        color = "#ef4444"

        advice = [
            "Do NOT open this link.",
            "Never enter passwords.",
            "Block or report the sender.",
            "Verify from the official website.",
            "Enable Two-Factor Authentication (2FA)."
        ]

    else:

        result = "✅ SAFE"

        color = "#22c55e"

        advice = [
            "No major phishing indicators detected.",
            "Still verify the domain before login.",
            "Avoid sharing sensitive information.",
            "Keep browser security enabled."
        ]

    reasons = []

    if url_features["has_ip_address"]:
        reasons.append("Uses an IP address instead of a trusted domain.")

    if url_features["has_suspicious_words"]:
        reasons.append("Contains suspicious keywords.")

    if url_features["has_special_chars"]:
        reasons.append("Contains unusual special characters.")

    if not url_features["contains_https"]:
        reasons.append("Website is not using HTTPS.")

    if len(reasons) == 0:
        reasons.append("No obvious phishing indicators were detected.")

    threat = classify_threat(url, reasons)

    ai_response = explain_url(
        url,
        result,
        reasons
    )

    return {
        "result": result,
        "score": spam_score,
        "color": color,
        "reasons": reasons,
        "advice": advice,
        "ai_response": ai_response,
        "threat": threat
    }