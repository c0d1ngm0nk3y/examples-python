from gameoflife.data.State import State

def from_string(rows, columns, string):
    state = State(rows, columns)
    for row in xrange(0, rows):
        for column in xrange(0, columns):
            index = row * columns + column
            char = string[index]
            if char == State.CELL_ALIVE:
                state.set_alive(row, column)
    return state

def from_file(filename):
    return filename
