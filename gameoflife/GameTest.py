from __future__ import absolute_import
import unittest
from gameoflife.Game import next_generation
from gameoflife.data.StateReader import from_string

class GameTest(unittest.TestCase):
    def test_dying_alone(self):
        state = from_string(1, 3, ".*.")
        next_state = next_generation(state)

        self.assertFalse(next_state.is_alive(0, 1))

    def test_not_dying_2(self):
        state = from_string(1, 3, "***")
        next_state = next_generation(state)

        self.assertTrue(next_state.is_alive(0, 1))

    def test_not_dying_3(self):
        state = from_string(2, 3, "***.*.")
        next_state = next_generation(state)

        self.assertTrue(next_state.is_alive(0, 1))

    def test_not_dying_3_variation(self):
        state = from_string(2, 3, ".*.***")
        next_state = next_generation(state)

        self.assertTrue(next_state.is_alive(1, 1))

    def test_dying_5(self):
        state = from_string(2, 3, "******")
        next_state = next_generation(state)

        self.assertFalse(next_state.is_alive(1, 1))

    def test_ressurrect_4(self):
        state = from_string(2, 3, "*.**.*")
        next_state = next_generation(state)

        self.assertTrue(next_state.is_alive(1, 1))


if __name__ == '__main__':
    unittest.main()
