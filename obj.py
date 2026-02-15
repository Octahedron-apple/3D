import numpy as np
class camera():
    def __init__(X: float,Y: float,Z: float,X_Rotate: float,Y_Rotate: float,Z_Rotate: float,Focal_Length: float):
        self.position=np.array([X,Y,Z])

class point():
    def __init__(X: float=0,Y: float=0,Z: float=0):
        self.main=np.array([X,Y,Z])
        self.projection=np.array([0,0])
    def render(camera: camera):

