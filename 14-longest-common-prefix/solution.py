class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Handle the case where the list is empty
        if not strs:
            return ""
        
        # Sort the strings alphabetically
        strs.sort()
        
        # Take the first and the last strings in the sorted list
        first = strs[0]
        last = strs[-1]
        
        ans = ""
        # Compare characters of the first and last string
        # Use min length to avoid index out of bounds
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
            
        return ans
