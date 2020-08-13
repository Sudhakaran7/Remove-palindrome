class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == '':
            return 0
        def isPalindrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l  = 1
                r -= 1
            return True
        return 1 if isPalindrome(s) else 2

val=Solution()
S=input()
print(val.removePalindromeSub(S))
