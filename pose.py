import cv2
import numpy as np
import mediapipe as mp
import pickle

def calc_angle(a,b,c):
    # Code for calc_angle function

 def detect_poses():
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    left_flag = None
    left_count = 0
    right_flag = None
    right_count = 0
    cap = cv2.VideoCapture(0)
    pose = mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.5)
    while cap.isOpened():
        # Code for detect_poses function
       cap.release()
       cv2.destroyAllWindows()
       return (left_count, right_count)

if __name__ == "__main__":
    counts = detect_poses()
    print(counts)
    with open("pose_detection.pkl", "wb") as f:
        pickle.dump(detect_poses, f)
