class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        
        # Iterate through the haystack up to the point where 
        # the remaining string is shorter than the needle
        for i in range(n - m + 1):
            # Check if the substring matches the needle
            if haystack[i : i + m] == needle:
                return i
                
        return -1
