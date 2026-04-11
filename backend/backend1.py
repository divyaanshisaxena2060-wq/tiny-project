from flask import Flask, request, send_file, jsonify
import subprocess
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = os.path.join("..", "Model", "output")  # using your existing output path

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/colorize", methods=["POST"])
def colorize():
    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["image"]
    filename = secure_filename(file.filename)

    input_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(input_path)

    # 👇 Trick: pass file path to your existing script
    try:
        subprocess.run(
            ["python", "../Model/app.py", input_path],
            check=True
        )
    except subprocess.CalledProcessError:
        return jsonify({"error": "Model failed"}), 500

    # assuming your model saves output here
    output_path = os.path.join(OUTPUT_FOLDER, "colorized_output.jpg")

    if not os.path.exists(output_path):
        return jsonify({"error": "Output not found"}), 500

    return send_file(output_path, mimetype="image/jpeg")


if __name__ == "__main__":
    app.run(debug=True)
