import sys


class Glass:

    def __init__(self, capacity, fill):
        self.capacity = capacity
        self.fill = fill

    def __repr__(self):
        if self.isFull():
            return str("|▇|")
        elif self.fill >= self.capacity/2:
            return str("|▅|")
        elif self.fill > 0 and self.fill < self.capacity/2:
            return str("|▂|")
        return str("|_|")

    def isFull(self):
        if self.fill >= self.capacity:
            return True
        return False

    def overFill(self):
        return self.fill - self.capacity


def hello_world():
    return 'Hello world'


def water_overflow(k):
    capacity = 250
    remain = k*1000
    max_row = remain//capacity
    glasses = [[Glass(capacity=capacity, fill=0) for i in range(j+1)] for j in range(max_row)]
    glasses[0][0].fill = remain
    row = 0
    while remain > capacity:
        for _j in range(row):
            _i = row - 1
            if glasses[_i][_j].isFull():
                over_fill = glasses[_i][_j].overFill()
                glasses[_i][_j].fill = capacity
                glasses[_i + 1][_j].fill += over_fill / 2
                glasses[_i + 1][_j + 1].fill += over_fill / 2
                remain -= capacity

        row += 1

    return glasses


if __name__ == '__main__':

    total_water = int(sys.argv[1])
    find_row = int(sys.argv[2])
    find_position = int(sys.argv[3])
    illustrate = bool(sys.argv[4])

    glasses = water_overflow(total_water)
    if illustrate:
        row_reverse = len(glasses)
        for row in glasses:
            row_glasses = []
            for glass in row:
                row_glasses.append(str(glass))
            print(" "*row_reverse, "".join(row_glasses))
            row_reverse -= 1

    find_level = glasses[find_row][find_position].fill

    print('When pouring {}L of water, the level of glass in row {} at pos {} is {}ml'.format(total_water, find_row, find_position, find_level))
