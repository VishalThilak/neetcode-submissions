class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for n in nums:
            map[n] = map.get(n, 0) + 1

        #sorted_elements = sorted(map.keys(), key=lambda x: map[x], reverse=True)

        freq = [[] for i in range(len(nums) + 1)]

        for key, value in map.items():
            freq[value].append(key)

        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                k -= 1
                if k == 0:
                    return result

        