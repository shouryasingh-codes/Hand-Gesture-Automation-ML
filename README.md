Hand Gesture Controlled Automation (ML + MediaPipe + Python)

This is a simple project where I use a webcam, MediaPipe Hands,
and a custom trained ML model to recognize hand gestures
and control the system based on those gestures.

The main idea was to build something that works in real-time and
lets me perform basic actions without touching the keyboard or mouse.

💡 Gestures & Actions

I trained the model on 3 gestures:

Gesture	Action
✌️ Victory	Opens Chrome
✊ Fist	Opens ChatGPT website
🖐️ Open Palm	Closes Chrome

Each action runs only once when a new gesture appears.
Holding the gesture does not repeat the action.

🧠 How the system works

Camera captures my hand

MediaPipe extracts 21 hand landmarks

I normalized the landmarks wrt the wrist

A RandomForest model predicts the gesture

Based on the prediction, Python triggers system commands

The whole pipeline runs live using OpenCV.

📦 Project Files

realtime.py → Final real-time gesture automation code

guestre_model.pkl → Trained ML model

extract_landmaK.py → Landmark extraction script

evaluate.py → Model training & evaluation

*_landmark_norm.csv → Normalized landmark datasets

data_sheet/ → Gesture images (raw data)

🛠️ Tech Used

Python

MediaPipe Hands

OpenCV

Scikit-Learn

OS Automation (os / pyautogui)

🤝 What I learnt

Real-time ML model integration

Working with MediaPipe landmarks

Normalizing coordinate-based data

Training + evaluating simple ML models

Using Python for automation

Most importantly: debugging real-time systems

Author

Lucky Singh
