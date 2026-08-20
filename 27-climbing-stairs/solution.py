class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
            
        one_step_back = 2
        two_steps_back = 1
        current = 0
        
        for _ in range(3, n + 1):
            current = one_step_back + two_steps_back
            two_steps_back = one_step_back
            one_step_back = current
            
        return current
