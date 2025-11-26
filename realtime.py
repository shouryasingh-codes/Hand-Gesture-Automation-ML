import cv2
import mediapipe as mp
import pickle
import time
import os
import pyautogui

model = pickle.load(open("guestre_model.pkl", "rb"))

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)

last_gesture = None  
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        handlm = result.multi_hand_landmarks[0]

        mp.solutions.drawing_utils.draw_landmarks(frame, handlm, mp_hands.HAND_CONNECTIONS)

        lm_list = []
        wrist_x = handlm.landmark[0].x
        wrist_y = handlm.landmark[0].y
        wrist_z = handlm.landmark[0].z

        for lm in handlm.landmark:
            lm_list.append(lm.x - wrist_x)
            lm_list.append(lm.y - wrist_y)
            lm_list.append(lm.z - wrist_z)

        prediction = model.predict([lm_list])[0]


        if prediction == 0:                     # VICTORY
            text = "VICTORY"
            color = (0, 255, 0)

            if last_gesture != 0:              # changed to victory
                os.system("start firefox")      # action ONCE
            last_gesture = 0                   # lock gesture

        elif prediction == 1:                   # FIST
            text = "FIST"
            color = (255, 0, 0)

            if last_gesture != 1:              # changed to fist
                os.system("start https://chatgpt.com")
            last_gesture = 1

        else:                                   # OPEN
            text = "OPEN"
            color = (0, 0, 255)

            if last_gesture != 2:              # changed to open
                os.system("taskkill /im firefox.exe /f")
            last_gesture = 2

        # UI box
        cv2.rectangle(frame,(30,30),(200,90),color,-1)
        cv2.putText(frame,text,(40,70),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
