class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if not isinstance(nums, list) or not isinstance(target, int) or isinstance(target, bool):
            raise TypeError
        for num in nums:
            if not isinstance(num, int):
                raise TypeError
        
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]
        
        return []
