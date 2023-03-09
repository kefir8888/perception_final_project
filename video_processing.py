import numpy as np
import cv2

#reference:
#https://github.com/GSNCodes/ArUCo-Markers-Pose-Estimation-Generation-Python

class Video_processor:
    def __init__(self, calibration_file):
        self.calibration_file = calibration_file
    
    def process_frame(self, frame):
        #should return a list of dicts like {"marker_id" : id, "tvec" : tvec, "rvec" : rvec}
        #and a frame with detected arucos drawn on it

        return 5, frame