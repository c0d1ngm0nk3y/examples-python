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

    def test_invalid_row(self):
        state = State(3, 3)
        self.assertEqual(None, state.get_cell(3, 0))

    def test_invalid_column(self):
        state = State(3, 3)
        self.assertEqual(None, state.get_cell(0, 3))

    def test_get_dimensions_2_3(self):
        state = State(2, 3)
        self.assertEqual((2, 3), state.get_dimensions())

    def test_get_dimensions_5_1(self):
        state = State(5, 1)
        self.assertEqual((5, 1), state.get_dimensions())


if __name__ == '__main__':
    unittest.main()
