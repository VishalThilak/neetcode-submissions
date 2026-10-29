class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeats = set()

        for n in nums:
            if n in repeats:
                return True
            repeats.add(n)
        
        return False

        