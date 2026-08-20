class Solution(object):
    def generateParenthesis(self, n):
        if n == 0:
            return []
            
        queue = [('', 0, 0)]
        result = []
        
        while queue:
            current, open_count, close_count = queue.pop(0)
            
            if len(current) == 2 * n:
                result.append(current)
                continue
                
            if open_count < n:
                queue.append((current + '(', open_count + 1, close_count))
                
            if close_count < open_count:
                queue.append((current + ')', open_count, close_count + 1))
                
        return result
