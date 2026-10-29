class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = []
        for num in nums:
            if num not in list:
                list.append(num)
            else:
                return True
        return False