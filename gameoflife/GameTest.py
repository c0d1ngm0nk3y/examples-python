from __future__ import absolute_import
import unittest
from gameoflife.Game import next_generation
from gameoflife.data.StateReader import from_string

class GameTest(unittest.TestCase):
    def test_dying(self):
        state = from_string(1, 3, ".*.")
        next_state = next_generation(state)

        self.assertFalse(next_state.is_alive(0, 1))


if __name__ == '__main__':
    unittest.main()
