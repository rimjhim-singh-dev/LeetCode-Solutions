class Solution:
     def longestPalindrome(self, s: str) -> str:
        # Check substrings starting from the longest possible length down to 1
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                substring = s[start : start + length]
                
                # Check if the substring is a palindrome using slicing
                if substring == substring[::-1]:
                    return substring
        return ""
