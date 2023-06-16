class Solution:
    def isValid(self, s: str) -> bool:
        open = []
        b=True
        if len(s) == 1:
            return False
        for i in s:
            if (i == '(' or i == '[' or i == '{'):
                open.append (i)
            elif open and (i == ')' or i == ']' or i == '}' ):
                if i ==')' and open[-1]=='(':
                    open.pop()
                    continue
                elif i == '}' and open[-1]=='{':
                    open.pop()
                    continue
                elif i == ']' and open[-1]=='[':
                    open.pop()
                    continue
                else:
                    return False
            else: 
                return False
        else:
            if  open==[]:
                return True
            else:
                return False

p = Solution()
print(p.isValid("()({)}") ) 
