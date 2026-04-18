# 🎨 Colorforge AI

## 📌 Overview
Colorforge AI is a web-based application that converts black and white images into colored images using AI-based processing.
It uses a deep learning model (Caffe) to automatically add realistic colors to grayscale images.


## 🚀 Features
- Convert black & white images to color
- Simple and user-friendly interface
- Fast image processing
- AI-powered colorization


## 🛠️ Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- Libraries: OS, Subprocess
- Model: Caffe Model


## ⚙️ How It Works
1. User uploads a black and white image
2. Image is processed through Flask backend
3. Backend uses Caffe model for colorization
4. Output colored image is generated and displayed


## 📂 Project Structure

```text
Colorizer/
│── Backend/
│   │── uploads/
│   └── backend1.py
│
│── Frontend/
│   └── frontend1.html
│
│── Model/
│   │── output/
│   │── app.py
│   │── colorization_deploy_v2.prototxt
│   │── colorization_release_v2.caffemodel
│   └── pts_in_hull.npy
