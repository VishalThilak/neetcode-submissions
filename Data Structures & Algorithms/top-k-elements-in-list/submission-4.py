class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)
        result = []
        map = {}

        for n in nums:
            map[n] = map.get(n, 0) + 1

        sorted_elements = sorted(map.keys(), key=lambda x: map[x], reverse=True)


            
        
        return sorted_elements[:k]