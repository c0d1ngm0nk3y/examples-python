class State(object):
    CELL_DEAD = "."
    CELL_ALIVE = "*"

    def __init__(self, rows=0, columns=0):
        self.rows = rows
        self.columns = columns
        self.field = "." * rows * columns

    def get_cell(self, x_coord, y_coord):
        if not self._check_coordinates(x_coord, y_coord):
            return None
        i = x_coord * self.columns + y_coord
        return self.field[i]

    def _check_coordinates(self, x_coord, y_coord):
        return (x_coord < self.rows) and (y_coord < self.columns)

    def get_dimensions(self):
        return (self.rows, self.columns)