class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_group = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = sorted(s)
            anagrams_group[tuple(sorted_s)].append(s)
        for value in anagrams_group.values():
            result.append(value)

        return result