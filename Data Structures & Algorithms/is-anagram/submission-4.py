class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        strings = {}
        for c in s:
            if c not in strings:
                strings[c] = 1
            else:
                strings[c] += 1

        for c in t:
            if c in strings:
                strings[c] -= 1
                if(strings[c] == 0):
                    del strings[c]
            else:
                return False
        return True
