import numpy as np

class Filter:
    def __init__(self, map):
        self.map = map
    
    def update_coords(self, markers):
        return 5

class Reverse_mapping(Filter):
    def __init__(self, map):
        Filter.__init__(self, map)
    
    def update_coords(self, markers, frame):
        #should return a tupe of three numbers (x, y, theta) and a map with the position
        #drawn on it, fitted in the image of the same size as frame

        drawn_position = np.zeros_like(frame)

        return (3, 4, 5), drawn_position