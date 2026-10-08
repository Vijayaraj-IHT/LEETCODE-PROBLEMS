class Solution(object):
    def postorder(self, root):
        if not root:
            return []
        
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                stack.extend(node.children)
                
        return res[::-1]
