BG_ACC_WIDTH = 1620
BG_ACC_HEIGHT = 2160
WIDTH = 648
HEIGHT = 864

def getX(x):
    return x/BG_ACC_WIDTH * WIDTH
def getY(y):
    return y/BG_ACC_HEIGHT * HEIGHT

def normalizeDepth(depth):
    max = 1620 - 652
    return depth/max * 1.0

# left
# start 739, 652
# end 25, 2160

# middle 
# start 810, 652
# end middle, 2160

# right
# start 893, 652
# end 1509, 2160