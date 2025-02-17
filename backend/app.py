from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils.pdf_to_image import pdf_to_images
from utils.image_to_json import image_to_json

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    pdf_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(pdf_path)

    # Convert PDF to images
    image_folder = os.path.join(UPLOAD_FOLDER, "images")
    image_paths = pdf_to_images(pdf_path, image_folder)

    # Extract text from images and convert to JSON
    json_data = []
    for image_path in image_paths:
        json_data.append(image_to_json(image_path))

    return jsonify(json_data)

if __name__ == "__main__":
    app.run(debug=True)
