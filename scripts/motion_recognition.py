import cv2
import mediapipe as mp
import numpy as np
import csv


def body_recognition():
        win_name = "camera window"     
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        cap = cv2.VideoCapture(0)
        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        # Setup mediapipe instance
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
        
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
      
                # Make detection
                results = pose.process(image)
    
                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
                # Extract landmarks
                try:
                    landmarks = results.pose_landmarks.landmark 
                    print(landmarks)
                except Exception as e:
                        print(str(e))
                        pass
                # Render detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,12), thickness=2, circle_radius=4), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=4) 
                                     )               
                cv2.imshow( win_name, image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
        cap.release()
        cv2.destroyAllWindows()

body_recognition()