import unittest
import random

from GenerateBBSTArray import GenerateBBSTArray


class GenerateBBSTArrayTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(GenerateBBSTArray([0]), [0])
        self.assertEqual(GenerateBBSTArray([3, 5, 2]), [3, 2, 5])
        self.assertEqual(
            GenerateBBSTArray([75, 62, 84, 37, 25, 50, 20]),
            [50, 25, 75, 20, 37, 62, 84],
        )


if __name__ == "__main__":
    unittest.main()
