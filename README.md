📌 Gesture-Controlled Image Zoom using MediaPipe Tasks API
🚀 Overview

This project implements a real-time gesture-based image zoom system using hand tracking.
By measuring the distance between the thumb tip (landmark 4) and index fingertip (landmark 8), the system dynamically zooms an image in or out—just like a touchscreen pinch gesture, but using only a webcam.

🎯 Features
🤏 Pinch-to-zoom using hand gestures
🎥 Real-time hand tracking
📏 Distance-based dynamic scaling
⚡ Smooth and responsive interaction
🧠 Built using latest MediaPipe Tasks API
🛠️ Tech Stack
Python
OpenCV
NumPy
MediaPipe Tasks API
🧠 How It Works
Webcam captures live video
Hand landmarks are detected using MediaPipe
Distance between:
Thumb tip (4)
Index fingertip (8)
Distance is mapped to a scaling factor
Image is resized dynamically using OpenCV

⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/gesture-zoom-project.git
cd gesture-zoom-project
2. Install dependencies
pip install -r requirements.txt
▶️ Usage
python main.py
📸 Demo

👉 Add your demo video/GIF here
(Highly recommended for better visibility)

⚠️ Requirements
Webcam
Python 3.8+
hand_landmarker.task model file
🔥 Future Improvements
🎮 Add gesture-based panning
🔊 Add gesture-based volume control
🎨 UI enhancements
📱 Web-based implementation
