from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return index

class KMPAlgorithm:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        pre = 0
        # LPS for needle
        for i in range(1, len(needle)):
            while pre > 0 and needle[pre] != needle[i]:
                pre = lps[pre-1]
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre
        # KMP main algorithm
        n = 0
        for j in range(len(haystack)):
            while n > 0 and needle[n] != haystack[j]:
                n = lps[n-1]
            if needle[n] == haystack[j]:
                n += 1
            if n == len(needle):
                return j - n + 1

        return -1


haystack = "sadbutsadday"
needle = "day"
sol = Solution()
print(sol.strStr(haystack, needle))


haystack = "sadbutabdabaabacababday"
needle = "abacabab"
sol = KMPAlgorithm()
print(sol.strStr(haystack, needle))