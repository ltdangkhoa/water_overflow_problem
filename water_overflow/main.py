import sys


class Glass:
    """
    Attributes
    ----------
    capacity : int
        the capacity of glass
    fill : float
        the level of water fill to the glass
    (default 0)

    Methods
    -------
    isFull()
        Check for the glass full filled

    overFill()
         Check for the glass over fill

    """

    def __init__(self, capacity, fill=0):
        """
        Parameters
        ----------
        capacity : int
            the capacity of glass
        fill : float
            the level of water fill to the glass
        (default 0)
        """
        self.capacity = capacity
        self.fill = fill

    def __repr__(self):
        if self.isFull():
            return "{0:^4}".format("\\▇/")
        elif self.fill >= self.capacity/2:
            return "{0:^4}".format("\\▅/")
        elif self.fill > 0 and self.fill < self.capacity/2:
            return "{0:^4}".format("\\▂/")
        return "{0:^4}".format("\\_/")

    def isFull(self) -> bool:
        """Check for the glass full filled

        If the glass filled water is equal or greater than the capacity return True, otherwise return False
        """
        if self.fill >= self.capacity:
            return True
        return False

    def overFill(self):
        """Check for the glass over fill

        Return the over fill of the glass
        """
        return self.fill - self.capacity


def hello_world():
    return 'Hello world'


def water_overflow(k):
    """Method to calculate the k(L) of water pouring to Pascal's triangle of glasses

    Return list of rows of glasses
    """
    capacity = 250
    remain = int(k*1000)
    max_row = remain//capacity
    glasses = [[Glass(capacity=capacity) for i in range(j+1)] for j in range(max_row)]
    glasses[0][0].fill = remain
    row = 0
    while row < max_row and remain > capacity:
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

    total_water = float(sys.argv[1])
    find_row = int(sys.argv[2])
    find_position = int(sys.argv[3])
    illustrate = bool(sys.argv[4])

    glasses = water_overflow(total_water)
    if illustrate:
        row_reverse = len(glasses) - 1
        for row in glasses:
            row_glasses = []
            for glass in row:
                row_glasses.append(str(glass))
            print("{0:^2}".format(" ")*row_reverse, "".join(row_glasses))
            row_reverse -= 1

    find_level = glasses[find_row][find_position].fill

    print('When pouring {}L of water, the level of glass in row {} at pos {} is {}ml'.format(total_water, find_row, find_position, find_level))
