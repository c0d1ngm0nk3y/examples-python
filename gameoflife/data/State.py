class State(object):
    CELL_DEAD = "."
    CELL_ALIVE = "*"

    def __init__(self, rows=0, columns=0):
        self.rows = rows
        self.columns = columns
        self.field = "." * rows * columns

    def get_cell(self, x_coord, y_coord):
        i = x_coord * self.columns + y_coord
        return self.field[i]
