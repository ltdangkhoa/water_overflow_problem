
def hello_world():
    return 'Hello world'

class Glass:
    
    def __init__(self, capacity, fill):
        self.capacity = capacity
        self.fill = fill

    def isFull(self):
        if self.fill >= self.capacity:
            return True
        return False

def water_overflow(k, i, j):
    capacity = 250
    glass = [[Glass(capacity=capacity, fill=0) for i in range(k)] for j in range(k)]
    remain = k*1000
    glass[0][0] = remain
    row = 0
    while row < 5:
        for _j in range(row):
            _i = row - 1
            if glass[_i][_j].isFull():
                glass[_i][_j].fill = capacity
                remain =  remain - capacity
                glass[_i + 1][_j].fill = remain / 2
                glass[_i + 1][_j + 1].fill = remain / 2

        row += 1

    return glass[i][j].fill

