class Solution(object):
    def isValid(self, s)->bool:
        bracaket_map={'):'(,'}:'{',']':'['}
        stack=[]
        for char in s:
        if char in bracket_map:
        top_element=stack.pop() if stack else'#'
        if brackert_map[char]
        !=top_element:
        return false
        else:
          stack.apppend(char)
        return not stack
        print(isValid("()"))
        print(isValid("()[]{}"))
        print(isValid("(]"))
        print(isValid("([)]"))
        print(isValid("{[]}"))
        
        
        """
        :type s: str
        :rtype: bool
        """
        pass







    



  

