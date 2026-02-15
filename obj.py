import numpy as np
import math
class camera():
    def __init__(self,X: float,Y: float,Z: float,X_Rotate: float,Y_Rotate: float,Z_Rotate: float,Focal_Length: float):
        self.position=np.array([X,Y,Z])
        self.rotation=np.array([X_Rotate,Y_Rotate,Z_Rotate])
        self.Focal_Length=Focal_Length
    def get_position(self):
        return self.position
    def get_rotation(self):
        return self.rotation
    def get_focal_length(self):
        return self.Focal_Length
class point():
    def __init__(self,X: float=0,Y: float=0,Z: float=0):
        self.main=np.array([X,Y,Z])
        self.projection=np.array([0,0])
    def render(self,camera: camera):
        relative=self.main-camera.get_position()
        rotation=camera.get_rotation
        Focal_Length=camera.get_focal_length()
        rad=math.radians(rotation(0))
        c = math.cos(rad)
        s = math.sin(rad)
        rotation_matrix = np.array([
            [1, 0, 0],
            [0, c, -s],
            [0, s, c]
        ])
        relative=rotation_matrix@relative
        rad=math.radians(rotation(1))
        c = math.cos(rad)
        s = math.sin(rad)
        rotation_matrix = np.array([
            [c, 0, s],
            [0, 1, 0],
            [-s, 0, c]
        ])
        relative=rotation_matrix@relative
        rad=math.radians(rotation(2))
        c = math.cos(rad)
        s = math.sin(rad)
        rotation_matrix = np.array([
            [c, -s, 0],
            [s, c, 0],
            [0, 0, 1]
        ])
        relative=rotation_matrix@relative
        self.projection=np.array([Focal_Length*relative[0]/relative[2],Focal_Length*relative[1]/relative[2]])
        return self.projection
def object():
    def __init__(self,offset: float=0):
        self.main=[]
        self.offset=offset
    def Add_Point(self,point: point):
        self.main.append(point)
    def Count(self):
        return len(self.main)
    def __len__(self):
        return len(self.main)



        

