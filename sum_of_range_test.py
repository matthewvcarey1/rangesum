import unittest
from rangesum import sum_of_range


class RangeTest(unittest.TestCase):
    def test_range_sum(self):
        sizes = [2, 101, 157, 123456, 10000001]
        for size in sizes:
            val = 0
            num_range = range(size)
            for i in num_range:
                val += i
            self.assertEqual(val, sum_of_range(num_range))
        val = 0
        num_range = [1,2,3,4]
        for i in num_range:
            val += i
        self.assertEqual(val, sum_of_range(num_range))
        val = 0
        num_range = [2,3,4,5]
        for i in num_range:
            val += i
        self.assertEqual(val, sum_of_range(num_range))

if __name__ == '__main__':
    unittest.main()
