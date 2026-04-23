import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import math
import numpy as np

base = python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(
    base_options= base,
    num_hands= 2,
    min_tracking_confidence= 0.5,
    min_hand_detection_confidence= 0.5,
    min_hand_presence_confidence= 0.5
)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    r,fps = cap.read()
    if r == True:
        fps = cv2.flip(fps,1)
        fps = cv2.resize(fps,(400,400))
        rgb_fps = cv2.cvtColor(fps,cv2.COLOR_BGR2RGB)

        mp_fps = mp.Image(image_format=mp.ImageFormat.SRGB,data= rgb_fps)

        detection_result = detector.detect(mp_fps)

        if detection_result.hand_landmarks:
            for landmark in detection_result.hand_landmarks:
                for j in landmark:
                    x = int(j.x * fps.shape[1])
                    y = int(j.y * fps.shape[0])

                    #cv2.circle(fps,(x,y),5,(0,0,255),-1)

                    connections = mp.solutions.hands.HAND_CONNECTIONS
                    for connection in connections:
                        start = connection[0]
                        end = connection[1]
                        
                        start_pt = landmark[start]
                        end_pt = landmark[end]

                        pt1 = (int(start_pt.x * fps.shape[1]),int(start_pt.y * fps.shape[0]))
                        pt2 = (int(end_pt.x * fps.shape[1]),int(end_pt.y * fps.shape[0]))

                        cv2.line(fps,pt1,pt2,(255,255,255),3,4)

                    d1 = landmark[4]
                    d2 = landmark[8]
                    
                    x1,y1 = (int(d1.x * fps.shape[1]),int(d1.y * fps.shape[0]))
                    x2,y2 = (int(d2.x * fps.shape[1]),int(d2.y * fps.shape[0]))

                    distance = math.sqrt(pow((x1 - x2),2) + pow((y1 - y2),2))
                    cv2.line(fps,(x1,y1),(x2,y2),(255,0,0),2,4)
                    cv2.putText(fps,f'Dist: {int(distance)}',(100,100),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2,4)
                    img = cv2.imread("images_videos\scenary.webp")
                    
                    scale = np.interp(distance,[20,160],[0.5,2.0])
                    h,w = img.shape[0],img.shape[1]
                    new_h = int(h * scale)
                    new_w = int(w * scale)
                    
                    img1 = cv2.resize(img,(new_h,new_w))
                    cv2.imshow("image",img1)

        cv2.imshow("capture",fps)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break
detector.close()
cap.release()
cv2.destroyAllWindows()

