class Solution(object):
    def __init__(self):
        self.val = {
            '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz', '0':''
        }
        
    def letterCombinations(self, digits):
        if not digits:
            return []
            
        combinations = ['']
        
        for digit in digits:
            letters = self.val[digit]
            new_combinations = []
            
            for current_string in combinations:
                for letter in letters:
                    new_combinations.append(current_string + letter)
                    
            combinations = new_combinations
            
        return combinations
