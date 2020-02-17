from ctypes import *

class POINT(Structure):
    _fields_= [("x", c_int),("y", c_int)]

def quadrant(point:Structure):
    if (point.x>0 and point.y>0):
        return 1
    elif(point.x<0 and point.y<0):
        return 3
    elif(point.x<0 and point.y>0):
        return 2
    elif(point.x>0 and point.y<0):
        return 4
    else:
        return "point falls on axis."
