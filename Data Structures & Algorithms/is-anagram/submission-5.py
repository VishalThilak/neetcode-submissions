class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # strings = {}
        # for c in s:
        #     if c not in strings:
        #         strings[c] = 1
        #     else:
        #         strings[c] += 1

        # for c in t:
        #     if c in strings:
        #         strings[c] -= 1
        #         if(strings[c] == 0):
        #             del strings[c]
        #     else:
        #         return False
        # return True
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
