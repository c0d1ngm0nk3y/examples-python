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

    def _get_cell(self, x_coord, y_coord):
        if not self._check_coordinates(x_coord, y_coord):
            return None
        i = x_coord * self.columns + y_coord
        return self.field[i]

    def is_dead(self, x_ccord, y_coord):
        value = self._get_cell(x_ccord, y_coord)
        return value == self.CELL_DEAD_INT

    def is_alive(self, x_ccord, y_coord):
        value = self._get_cell(x_ccord, y_coord)
        return value == self.CELL_ALIVE_INT

    def _check_coordinates(self, x_coord, y_coord):
        return (x_coord < self.rows) and (y_coord < self.columns)

    def get_dimensions(self):
        return (self.rows, self.columns)

    def set_alive(self, x_coord, y_coord):
        i = x_coord * self.columns + y_coord
        self.field[i] = self.CELL_ALIVE_INT
