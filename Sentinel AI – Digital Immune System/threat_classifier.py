# ==========================================
# Sentinel AI Threat Classification Engine
# ==========================================

def classify_threat(url, reasons):

    url = url.lower()

    # Default Result
    threat = {
        "category": "⚠ Suspicious Website",
        "risk": "Medium",
        "target": "Unknown",
        "confidence": "65%",
        "severity": "Medium",
        "action": "Review Carefully"
    }

    # ==========================================
    # Banking / Payment Phishing
    # ==========================================

    if any(word in url for word in [
        "paypal",
        "bank",
        "payment",
        "visa",
        "mastercard",
        "credit",
        "debit",
        "upi",
        "wallet",
        "stripe"
    ]):

        threat.update({
            "category": "🎣 Credential Phishing",
            "risk": "Critical",
            "target": "Banking Credentials",
            "confidence": "97%",
            "severity": "Critical",
            "action": "Block Immediately"
        })

    # ==========================================
    # Login Credential Theft
    # ==========================================

    elif any(word in url for word in [
        "login",
        "signin",
        "verify",
        "account",
        "password",
        "authenticate",
        "security"
    ]):

        threat.update({
            "category": "🔐 Account Credential Theft",
            "risk": "High",
            "target": "Username & Password",
            "confidence": "92%",
            "severity": "High",
            "action": "Do Not Login"
        })

    # ==========================================
    # Crypto Scam
    # ==========================================

    elif any(word in url for word in [
        "crypto",
        "bitcoin",
        "wallet",
        "bnb",
        "eth",
        "usdt",
        "airdrop",
        "coin"
    ]):

        threat.update({
            "category": "💰 Crypto Scam",
            "risk": "Critical",
            "target": "Crypto Assets",
            "confidence": "95%",
            "severity": "Critical",
            "action": "Avoid Immediately"
        })

    # ==========================================
    # Shopping Scam
    # ==========================================

    elif any(word in url for word in [
        "amazon",
        "daraz",
        "shop",
        "discount",
        "offer",
        "sale",
        "coupon"
    ]):

        threat.update({
            "category": "🛒 Shopping Scam",
            "risk": "Medium",
            "target": "Payment Information",
            "confidence": "83%",
            "severity": "Medium",
            "action": "Verify Seller"
        })

    # ==========================================
    # Government Scam
    # ==========================================

    elif any(word in url for word in [
        "gov",
        "nadra",
        "fbr",
        "tax",
        "passport"
    ]):

        threat.update({
            "category": "🏛 Government Impersonation",
            "risk": "High",
            "target": "Personal Identity",
            "confidence": "90%",
            "severity": "High",
            "action": "Verify Official Website"
        })

    # ==========================================
    # Email Scam
    # ==========================================

    elif any(word in url for word in [
        "mail",
        "gmail",
        "outlook",
        "email"
    ]):

        threat.update({
            "category": "📧 Email Phishing",
            "risk": "High",
            "target": "Email Credentials",
            "confidence": "91%",
            "severity": "High",
            "action": "Do Not Enter Password"
        })

    # ==========================================
    # Feature Based Improvements
    # ==========================================

    if "Website is not using HTTPS." in reasons:
        threat["confidence"] = "98%"

    if "Uses an IP address instead of a trusted domain." in reasons:
        threat["severity"] = "Critical"

    if "Contains suspicious keywords." in reasons:
        threat["risk"] = "Critical"

    return threat