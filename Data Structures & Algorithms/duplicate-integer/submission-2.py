class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeats = []

        for n in nums:
            if n in repeats:
                return True
            repeats.append(n)
        
        return False

        