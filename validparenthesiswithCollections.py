from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # T/S: O(n)
        d = {')':'(', '}':'{', ']':'['}
        stack = deque()
        for c in s:
            print('stack outer',stack)
            if c in d:
                print('c',c)
                print('stack',stack)
                if not stack or stack.pop() != d[c]:
                    return False
            else:
                stack.append(c)
            print('stack after',stack)        
        return not stack

p = Solution()
print(p.isValid("(){}") )         