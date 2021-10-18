
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
    glass = [[0 for i in range(k)] for j in range(k)]
    capacity = 1 # try to solve with capacity as 1 unit for test cases
    remain = k
    glass[0][0] = remain
    row = 0
    while row < 5:
        for _j in range(row):
            _i = row - 1
            if glass[_i][_j] >= capacity:
                glass[_i][_j] = capacity
                remain =  remain - capacity
                glass[_i + 1][_j] = remain / 2
                glass[_i + 1][_j + 1] = remain / 2

        row += 1

    return glass[i][j]

