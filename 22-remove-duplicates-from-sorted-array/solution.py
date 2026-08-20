from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Pointer for the position of the last unique element found
        slow = 0
        
        # Iterate through the array with a fast pointer
        for fast in range(1, len(nums)):
            # If we find a new unique element
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        # The number of unique elements is index + 1
        return slow + 1
