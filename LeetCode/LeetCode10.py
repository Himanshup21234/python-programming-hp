class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pnt2 = 0
        pnt1 = 0
        while (pnt1 <= len(s) - 1) and (pnt2 <= len(t) - 1):
            if s[pnt1] == t[pnt2]:
                pnt1 += 1
            pnt2 += 1
        return pnt1 == len(s)

s = ""
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s,t))

