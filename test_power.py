import unittest
from power import power


class power(unittest.TestCase):
    def test_power_works_successfully(self):


        self.assertEqual(power(3,4), 81)
        self.assertEqual(power(2,3), 8)


if __name__ == "__main__":
    unittest