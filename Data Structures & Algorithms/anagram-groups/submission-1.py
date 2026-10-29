class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for s in strs:
            key = tuple(sorted(s))
            if key in map:
                map[key].append(s)
            else:
                map[key] = [s]

        result = []
        for value in map.values():
            result.append(value)

        return result
        