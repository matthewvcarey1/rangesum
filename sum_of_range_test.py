import unittest
from rangesum import sum_of_range


class RangeTest(unittest.TestCase):
    def test_range_sum(self):
        sizes = [2, 101, 157, 123456, 10000001]
        for size in sizes:
            val = 0
            for i in range(size):
                val += i
            self.assertEqual(val, sum_of_range(size))


if __name__ == '__main__':
    unittest.main()
