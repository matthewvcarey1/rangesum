import unittest
from rangesum import sum_of_range


class RangeTest(unittest.TestCase):
    def test_range_sum(self):
        sizes = [2, 101, 157, 123456, 10000001]
        starts = [-3, 4 ,6, 0, 22, 550]
        for size in sizes:
            for start in starts:
                val = 0
                change = 0
                if start != 0:
                    change = start
                    start = 0
                num_range = list(range(size))
                if change != 0:
                    length = len(num_range)
                    i = 0
                    while i < len(num_range):
                        num_range[i] += change
                        i += 1
                for i in num_range:
                   val += i
                self.assertEqual(val, sum_of_range(num_range))


if __name__ == '__main__':
    unittest.main()
