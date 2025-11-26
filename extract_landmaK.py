import cv2
import mediapipe as mp
import csv 

file = open("fist_landmark_norm.csv", "a", newline="")
writer = csv.writer(file)


cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence = 0.7 , min_tracking_confidence = 0.7)



while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame , 1)

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handlm in result.multi_hand_landmarks:
            mp_draw = mp.solutions.drawing_utils
            mp_draw.draw_landmarks(frame,handlm,mp_hands.HAND_CONNECTIONS)
            b = ["VICTORY"]
            wrist_x = handlm.landmark[0].x
            wrist_y = handlm.landmark[0].y
            wrist_z = handlm.landmark[0].z
          
            for lm in handlm.landmark:
                
                rx = lm.x - wrist_x
                ry = lm.y - wrist_y
                rz = lm.z - wrist_z
                b.append(rx)
                b.append(ry)
                b.append(rz)
            writer.writerow(b)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break


file.close()
cap.release()
cv2.destroyAllWindows()
