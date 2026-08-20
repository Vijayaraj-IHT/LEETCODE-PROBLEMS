class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        diff = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return current_sum
                
                if abs(current_sum - target) < abs(diff - target):
                    diff = current_sum
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return diff
