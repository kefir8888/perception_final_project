from video_processing import Video_processor
from filters import Reverse_mapping
import cv2
import numpy as np

video_name = "data/markers.mp4"

cam = cv2.VideoCapture(video_name)

video_processor = Video_processor("data/calibration.yaml")

reverse_mapping_filter = Reverse_mapping("map.json")

while(True):
    success, frame = cam.read()
    
    
    if (success == False):
        print("reading failed")
        cam.release()
        cam = cv2.VideoCapture(video_name)
        
        continue
    orig = frame.copy()
    
    markers, frame = video_processor.process_frame(frame)
    new_coords, map_marked = reverse_mapping_filter.update_coords(markers, frame)

    map_marked = cv2.putText(frame, str(new_coords), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (255, 255, 0), 2, cv2.LINE_AA)

    output_frame = np.concatenate((orig, map_marked), axis=1)

    cv2.imshow("image&map", output_frame)

    key = cv2.waitKey(40) & 0xFF
    
    if (key == ord('q')):
        break

cam.release()
cv2.destroyAllWindows()
cv2.waitKey(10)