import unittest
from solution2 import Solution

class TestSolution(unittest.TestCase):
    def test_correct_value(self):
        
        datalist = [
            [
                ([2, 7, 11, 15], 9), 
                [0, 1]
            ],
            [
                ([3, 2, 4], 6),
                [1, 2]
            ],
            [
                ([3, 3], 6),
                [0, 1]
            ],
            [
                ([-1, -2, -3], -5),
                [1, 2]
            ]
        ]

        for data in datalist:
            nums, target = data[0][0], data[0][1]
            result = Solution().twoSum(nums, target)

            self.assertIsInstance(result, list)
            for obj in result:
                self.assertIsInstance(obj, int)
            self.assertEqual(result, data[1])
    
    def test_no_solutions(self):
        
        datalist = [
            [
                ([2, 7, 11, 15], 100), 
                []
            ],
            [
                ([3, 2, 4], -1),
                []
            ],
            [
                ([3, 3], 4),
                []
            ],
            [
                ([], 10),
                []
            ]
        ]

        for data in datalist:
            nums, target = data[0][0], data[0][1]
            result = Solution().twoSum(nums, target)

            self.assertIsInstance(result, list)
            self.assertEqual(len(result), 0)
    
    def test_incorrect_types(self):
        datalist = [
            (True, 100), 
            ('str', 100),
            (342, 100),
            (['str', [], False], 100),
            ([1, 2, 3], 'str'),
            ([1, 2, 3], True)
        ]

        for data in datalist:
            with self.assertRaises(TypeError) as context:
                Solution().twoSum(data[0], data[1])


if __name__ == '__main__':
    unittest.main()
