from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return index

haystack = "sadbutsadday"
needle = "day"
sol = Solution()
print(sol.strStr(haystack, needle))
