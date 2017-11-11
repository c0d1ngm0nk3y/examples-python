from gameoflife.data.State import State

def next_generation(state):
    (rows, columns) = state.get_dimensions()
    next_state = State(rows, columns)
    return next_state
