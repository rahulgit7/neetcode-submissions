class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # length = {}
        # for i in range(len(s)):
        #     length[s[i]] = length.get(s[i], 0) + 1
        #     length[t[i]] = length.get(t[i], 0) - 1
        # for val in length.values():
        #     if val != 0 :
        #         return False
            
        # return True
        if len(s) != len(t):
            return False
        from collections import Counter
        s_counter = Counter(s)
        t_counter = Counter(t)
        for k in s_counter:
            if s_counter[k] != t_counter[k]:
                return False
        return True
                


        

