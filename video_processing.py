import numpy as np
import cv2

import yaml

#reference:
#https://github.com/GSNCodes/ArUCo-Markers-Pose-Estimation-Generation-Python

class Video_processor:
    def __init__(self, calibration_file):
        self.calibration_file = calibration_file
        calib = yaml.load(open(calibration_file, 'r'), Loader=yaml.FullLoader)
        self.cameraMatrix = np.array(calib['camera_matrix']['data']).reshape(3, 3)
        self.distCoeffs = np.array(calib['distortion_coefficients']['data'])
        #rectification = np.array(calib['rectification_matrix']['data'])
        #shape = (calib['image_width'], calib['image_height'])
        #projection = np.array(calib['projection_matrix']['data']).reshape(3, 4)
        #distortion_model = calib['distortion_model']
        squareLength = 1
        self.objectPoints = np.array([[-squareLength / 2,  squareLength / 2, 0],
        [ squareLength / 2,  squareLength / 2, 0],
        [ squareLength / 2, -squareLength / 2, 0],
        [-squareLength / 2, -squareLength / 2, 0]])
        arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
        arucoParams = cv2.aruco.DetectorParameters()
        self.detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams)
    
    def process_frame(self, frame):
        #should return a list of dicts like {"marker_id" : id, "tvec" : tvec, "rvec" : rvec}
        #and a frame with detected arucos drawn on it
        corners, ids, _ = self.detector.detectMarkers(frame)
        res = []
        if corners is not None and ids is not None:
            for corners_, id_ in zip(corners, ids):
                retval, rvec, tvec = cv2.solvePnP(self.objectPoints, corners_, self.cameraMatrix, self.distCoeffs)
                
                if retval:
                    res+=[{"marker_id" : id_, "tvec" : tvec, "rvec" : rvec}]
                    cv2.drawFrameAxes(frame, self.cameraMatrix, self.distCoeffs, rvec, tvec, 1 )
        return res, frame