from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        q = deque()
        res = n + 1
        
        for i in range(n + 1):
            while q and prefix[i] - prefix[q[0]] >= k:
                res = min(res, i - q.popleft())
            while q and prefix[i] <= prefix[q[-1]]:
                q.pop()
            q.append(i)
            
        return res if res <= n else -1
