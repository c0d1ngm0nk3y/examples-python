from __future__ import absolute_import
import unittest
from gameoflife.data.State import State


class StateTest(unittest.TestCase):
    def test_empty_state_begin(self):
        state = State(2, 2)
        self.assertTrue(state.is_dead(0, 0))

    def test_empty_state_end(self):
        state = State(3, 3)
        self.assertTrue(state.is_dead(2, 2))

    def test_get_dimensions_2_3(self):
        state = State(2, 3)
        self.assertEqual((2, 3), state.get_dimensions())

    def test_get_dimensions_5_1(self):
        state = State(5, 1)
        self.assertEqual((5, 1), state.get_dimensions())

    def test_set_alive_1_3(self):
        state = State(5, 5)
        state.set_alive(1, 3)
        self.assertTrue(state.is_alive(1, 3))

    def test_set_alive_2_4(self):
        state = State(5, 5)
        state.set_alive(2, 4)
        self.assertTrue(state.is_alive(2, 4))

    def test_invalid_row(self):
        state = State(5, 5)
        self.assertFalse(state.is_alive(5, 1))
        self.assertFalse(state.is_dead(5, 1))

    def test_invalid_column(self):
        state = State(5, 5)
        self.assertFalse(state.is_alive(1, 5))
        self.assertFalse(state.is_dead(1, 5))


if __name__ == '__main__':
    unittest.main()
