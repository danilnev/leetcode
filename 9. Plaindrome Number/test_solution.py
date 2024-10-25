import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_correct_values(self):
        
        datalist = [
            121,
            565,
            234432,
            1000001,
            11,
            777,
            0,
            1
        ]

        for data in datalist:
            result = Solution().isPalindrome(data)

            self.assertIsInstance(result, bool)
            self.assertTrue(result)

    def test_incorrect_values(self):

        datalist = [
            12,
            -141,
            123123,
            745,
            10,
            -5
        ]

        for data in datalist:
            result = Solution().isPalindrome(data)

            self.assertIsInstance(result, bool)
            self.assertFalse(result)
    
    def test_incorrect_types(self):

        datalist = [
            'str',
            True,
            3.28,
            [1, 2, 3],
            {'1': 1}
        ]

        for data in datalist:
            with self.assertRaises(TypeError) as context:
                Solution().isPalindrome(data)


if __name__ == '__main__':
    unittest.main()