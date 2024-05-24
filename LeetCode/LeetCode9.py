import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_str = ""
        flag = True
        for el in s:
            if el not in string.punctuation and el != " ":
                processed_str += el.lower()
        if len(processed_str) > 0:
            if len(processed_str) % 2 == 0:
                index = len(processed_str) // 2
                if processed_str[:index] != processed_str[index:][::-1]:
                    flag = False
            else:
                index = len(processed_str) // 2
                if processed_str[:index] != processed_str[index+1:][::-1]:
                    flag = False
        return flag


class SecondSolution:
    def isPalindrome(self, s: str) -> bool:
        processed_str = ""
        flag = False
        for el in s:
            if el not in string.punctuation and el != " ":
                processed_str += el.lower()
        if processed_str == processed_str[::-1]:
            flag = True
        return flag


class TwoPointerSolution:
    def isPalindrome(self, s: str) -> bool:
        pnt1 = 0
        pnt2 = len(s) - 1
        while pnt1 < pnt2:
            if not s[pnt1].isalnum():
                pnt1 += 1
            elif not s[pnt2].isalnum():
                pnt2 -= 1
            elif s[pnt1].lower() == s[pnt2].lower():
                pnt1 += 1
                pnt2 -= 1
            else:
                return False
        return True


s = "race e car"
sol = TwoPointerSolution()
print(sol.isPalindrome(s))