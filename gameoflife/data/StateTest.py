from __future__ import absolute_import
import unittest
from gameoflife.data.State import State


class StateTest(unittest.TestCase):
    def test_empty_state_begin(self):
        state = State(2, 2)
        self.assertEqual(State.CELL_DEAD, state.get_cell(0, 0))

    def test_empty_state_end(self):
        state = State(3, 3)
        self.assertEqual(State.CELL_DEAD, state.get_cell(2, 2))


if __name__ == '__main__':
    unittest.main()
