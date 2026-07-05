from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from extract_features import extract_features
from url_analyzer import analyze_url
from image_analyzer import analyze_image

import threading
import webbrowser
import os

app = Flask(__name__)

# ==========================================
# Upload Folder Configuration
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==========================================
# Load Dataset & Train Model
# ==========================================

from model import load_model

model = load_model()
# ==========================================
# Home Page
# ==========================================

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        url = request.form.get("url", "").strip()

        image = request.files.get("image")

        # User must provide URL or Image
        if not url and (image is None or not image.filename):

            return render_template(
                "index.html",
                error="Please provide a URL or upload an image."
            )

        # ==========================================
        # Image Analysis
        # ==========================================

        if image and image.filename:

            result_data = analyze_image(
                image,
                app.config["UPLOAD_FOLDER"]
            )

            return render_template(
                "result.html",
                **result_data
            )

        # ==========================================
        # URL Analysis
        # ==========================================

        result_data = analyze_url(
            url,
            model
        )

        return render_template(
            "result.html",
            **result_data
        )

    return render_template("index.html")

# ==========================================
# Auto Open Browser
# ==========================================

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":

    threading.Timer(1.0, open_browser).start()

    app.run(debug=True)