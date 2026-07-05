import re

# Suspicious words jo aksar spam links me hoti hain
SUSPICIOUS_WORDS = ['login', 'free', 'verify', 'click', 'update', 'win', 'bonus', 'money', 'offer']

def extract_features(url):
    features = {}
    
    # 1. URL length
    features['url_length'] = len(url)
    
    # 2. Contains IP address
    features['has_ip_address'] = 1 if re.search(r'(\d{1,3}\.){3}\d{1,3}', url) else 0
    
    # 3. Contains HTTPS
    features['contains_https'] = 1 if url.startswith('https') else 0

    # 4. Special characters
    special_chars = ['@', '-', '_', '%', '=', '?']
    features['has_special_chars'] = 1 if any(char in url for char in special_chars) else 0

    # 5. Suspicious words
    features['has_suspicious_words'] = 1 if any(word in url.lower() for word in SUSPICIOUS_WORDS) else 0

    return features
# Testing block (just for checking if it's working)
if __name__ == "__main__":
    test_url = "http://freegift.ru"
    features = extract_features(test_url)
    print("Extracted Features:", features)
