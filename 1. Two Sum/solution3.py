class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if not isinstance(nums, list) or not isinstance(target, int) or isinstance(target, bool):
            raise TypeError
        for num in nums:
            if not isinstance(num, int):
                raise TypeError
        
        hash = {}  # Хэш-таблица для хранения числа и его индекса
        
        for i, num in enumerate(nums):
            finded = target - num
            if finded in hash:
                return [hash[finded], i]
            hash[num] = i

        return []
