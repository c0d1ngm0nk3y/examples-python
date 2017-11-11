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
    file_in = open(filename, "r")
    line = file_in.readline()
    sizes = line.split()
    rows = int(sizes[0])
    columns = int(sizes[1])
    string = ""
    for line in file_in.readlines():
        string += line.strip()

    state = from_string(rows, columns, string)

    file_in.close()
    return state
