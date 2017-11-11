from array import array

class State(object):
    CELL_DEAD = "."
    CELL_ALIVE = "*"

    CELL_DEAD_INT = 46
    CELL_ALIVE_INT = 47

    def __init__(self, rows=0, columns=0):
        self.rows = rows
        self.columns = columns
        self.field = array('b', self.CELL_DEAD * rows * columns)

    def __eq__(self, other):
        return self.field.__eq__(other.field)

    def __ne__(self, other):
        return not self.__eq__(other)

    def _get_cell(self, row, column):
        if not self._check_coordinates(row, column):
            return None
        i = row * self.columns + column
        return self.field[i]

    def is_dead(self, row, column):
        value = self._get_cell(row, column)
        return value == self.CELL_DEAD_INT

    def is_alive(self, row, column):
        value = self._get_cell(row, column)
        return value == self.CELL_ALIVE_INT

    def _check_coordinates(self, row, column):
        return (-1 < row < self.rows) and (-1 < column < self.columns)

    def get_dimensions(self):
        return (self.rows, self.columns)

    def set_alive(self, row, column):
        i = row * self.columns + column
        self.field[i] = self.CELL_ALIVE_INT

    def count_alive_neighbours(self, row, column):
        count = 0
        for n_row in xrange(row - 1, row + 2):
            for n_column in xrange(column - 1, column + 2):
                if self.is_alive(n_row, n_column):
                    count += 1

        if self.is_alive(row, column):
            count -= 1
        return count
