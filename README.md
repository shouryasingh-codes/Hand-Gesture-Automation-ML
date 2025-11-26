💻 Hand Gesture Controlled Automation (Python + ML + MediaPipe)

This project lets me control my PC using just hand gestures in front of a webcam.
No mouse. No keyboard. Just ✌️👊🖐️ and boom — automation.

I wanted to build something that works live and reacts instantly.
And yes — it actually works.

✋ Gestures & Actions (Real-Time)
Gesture	Action
✌️ Victory	Opens Chrome
👊 Fist	Opens ChatGPT
🖐️ Palm	Closes Chrome

Note: Each gesture triggers an action only once. Holding it won't spam.

⚙️ How It Works (Under the Hood)

Webcam captures live hand movement

MediaPipe tracks 21 hand landmarks

Coordinates are normalized (so position doesn't matter)

A RandomForest ML model predicts the gesture

Based on prediction, Python runs system-level commands (like opening Chrome)

Everything runs live using OpenCV —
Real-time input → real-time action.

🧠 What I Actually Faced

✌️ gesture was failing unless my hand was super close to camera
→ Fixed using wrist-based normalization

CSV files had header/index issues
→ Took some solid debugging to clean training data

Real-time loop was glitchy at first
→ Added frame wait + model output filtering

📁 Project Files (Cleaned & Functional)

realtime.py → Final live system

guesture_model.pkl → Trained model

extract_landmaK.py → Collects normalized landmark data

evaluate.py → Trains & evaluates ML model

*_landmark_norm.csv → Normalized data

🛠️ Tech Stack

Python

MediaPipe Hands

OpenCV

Scikit-Learn

🔥 What I Learnt

Real-time ML system building

Landmark normalization logic

Using RandomForest for classification

Practical issues in gesture control

Automating system using pure Python

And yeah — debugging hell and coming out alive 💀💪

🙋‍♂️ Made by
Shourya Singh
Built from scratch, tested in pain, now running smooth 😎
