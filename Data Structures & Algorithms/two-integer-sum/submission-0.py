class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        integers = {}
        for i in range(len(nums)):
            if nums[i] in integers:
                return [integers.get(nums[i]), i]
            else:
                integers[target - nums[i]] = i

        