class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c1=0
        c2 =0
        while c1 < len(s) and c2 < len(t):
            if s[c1] == t[c2]:
                c1+=1
            c2+=1
        return c1 == len(s)
        