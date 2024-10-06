class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        if not isinstance(nums, list) or not isinstance(target, int) or isinstance(target, bool):
            raise TypeError
        for num in nums:
            if not isinstance(num, int):
                raise TypeError
        
        for i in range(0, len(nums)):
            num = nums[i]
            finded = target - num
            if finded in nums and finded != num:
                return [i, nums.index(finded)]
            elif finded in nums and nums.count(finded) > 1:
                nums.pop(i)
                return [i, nums.index(finded) + 1]
        
        return []
