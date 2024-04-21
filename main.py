import sys

class cords:
    def __init__(self, value) :
        self.x, self.y = x, y

argv, cordsa, cordsb = cords(sys.argv[1:2]), cords(sys.argv[3:4])

def froute(a, b, frames):
    defc, frate = [], []
    if not isinstance(a, list) and not isinstance (b, list) :
        assert False, "An error ocurred. Program terminated"
    
    for i in range(1) :
        defc.append(b[i] - a[i])
    
    for x in defc :
        frate.append(x / frames)



