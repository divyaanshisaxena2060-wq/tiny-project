from fastapi import FastAPI, UploadFile, File, HTTPException
import numpy as np
import cv2
from model import colorize_image

app = FastAPI()

# 👉 simple in-memory user store
users = {}

# ---------------- COLORIZE ----------------
@app.post("/colorize")
async def colorize(file: UploadFile = File(...)):

    # 📥 read image
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 🎨 model call
    output = colorize_image(img)

    # 📤 return image
    _, buffer = cv2.imencode('.jpg', output)

    return {
        "image_bytes": buffer.tobytes().hex()
    }