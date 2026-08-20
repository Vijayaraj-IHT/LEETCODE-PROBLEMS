class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            check = target - nums[i]
            if check in nums:
                if i!=nums.index(check):
                    return list([i,nums.index(check)])
