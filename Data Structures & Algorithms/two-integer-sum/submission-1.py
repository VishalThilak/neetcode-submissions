class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            antecedent = target - nums[i]
            if antecedent in map:
                return [map[antecedent], i]
            
            map[nums[i]] = i
