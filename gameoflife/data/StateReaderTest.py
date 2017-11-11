from __future__ import absolute_import
import unittest
from gameoflife.data.StateReader import from_string

class StateReaderTest(unittest.TestCase):
    def test_from_string_size(self):
        state = from_string(2, 3, "......")
        self.assertEqual((2, 3), state.get_dimensions())

    def test_from_string_alive_row(self):
        state = from_string(3, 2, "..*...")
        self.assertTrue(state.is_alive(1, 0))

    def test_from_string_alive_column(self):
        state = from_string(2, 3, "..*...")
        self.assertTrue(state.is_alive(0, 2))


if __name__ == '__main__':
    unittest.main()
