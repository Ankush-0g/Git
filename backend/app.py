from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from deep_translator import GoogleTranslator
import os

app = Flask(
    __name__,
    static_folder="../frontend",
    static_url_path=""
)

CORS(app)

language = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    "la": "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/languages", methods=["GET"])
def get_languages():
    return jsonify(language)

@app.route("/translate", methods=["POST"])
def translate_text():

    data = request.json

    text = data.get("text")
    target = data.get("target")

    if not text or not target:
        return jsonify({"error": "Missing text or target"}), 400

    translated = GoogleTranslator(
        source="auto",
        target=target
    ).translate(text)

    return jsonify({
        "translated_text": translated
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
