class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = 0
        mask = 0
        
        for i in range(30, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            
            potential_max = max_xor | (1 << i)
            for p in prefixes:
                if (p ^ potential_max) in prefixes:
                    max_xor = potential_max
                    break
                    
        return max_xor
