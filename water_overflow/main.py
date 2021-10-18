import sys

def hello_world():
    return 'Hello world'

class Glass:
    def __init__(self, capacity, fill):
        self.capacity = capacity
        self.fill = fill

    def __repr__(self):
        return str(self.fill)

    def isFull(self):
        if self.fill >= self.capacity:
            return True
        return False

    def overFill(self):
        return self.fill - self.capacity


def water_overflow(k, i, j):
    capacity = 250
    remain = k*1000
    max_row = remain//capacity
    glass = [[Glass(capacity=capacity, fill=0) for i in range(max_row)] for j in range(max_row)]
    glass[0][0].fill = remain
    row = 0
    while remain > capacity:
        for _j in range(row):
            _i = row - 1
            if glass[_i][_j].isFull():
                over_fill = glass[_i][_j].overFill()
                glass[_i][_j].fill = capacity
                glass[_i + 1][_j].fill += over_fill / 2
                glass[_i + 1][_j + 1].fill += over_fill / 2
                remain -= capacity

        row += 1

    return glass[i][j].fill


if __name__ == '__main__':
    total_water = int(sys.argv[1])
    find_row = int(sys.argv[2])
    find_position = int(sys.argv[3])
    level = water_overflow(total_water, find_row, find_position)
    print('When pouring {}L of water, the level of glass in row {} at pos {} is {}ml'.format(total_water, find_row, find_position, level))
