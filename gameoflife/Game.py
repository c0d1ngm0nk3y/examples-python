from gameoflife.data.State import State

def next_generation(state):
    (rows, columns) = state.get_dimensions()
    next_state = State(rows, columns)

    for row in xrange(0, rows):
        for column in xrange(0, columns):
            count = state.count_alive_neighbours(row, column)
            if count < 2:
                pass
            elif (count == 2 or count == 3) and state.is_alive(row, column):
                next_state.set_alive(row, column)
            elif count == 3:
                next_state.set_alive(row, column)
            else:
                pass

    return next_state
