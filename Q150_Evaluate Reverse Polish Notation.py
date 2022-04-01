class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = ('+', '-', '*', '/')
    #O(N) space
        stack = []
    
    #O(N) time
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    stack.append(first + second)
                elif token == '-':
                    stack.append(first-second)
                elif token == '*':
                    stack.append(first*second)
                elif token == '/':
                    stack.append(int(first/second))
        return(stack[0])
    
    ################################################################
    class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op = ('+', '-', '*', '/')
        res =[]
        for i in tokens:
            if i not in op:
                res.append(i)
            elif i == '+':
                x = int(res[-2])
                y = int(res[-1])
                res.pop(-1)
                res[-1] = x + y
            elif i == '-':
                x = int(res[-2])
                y = int(res[-1])
                res.pop(-1)
                res[-1] = x - y
            elif i == '*':
                x = int(res[-2])
                y = int(res[-1])
                res.pop(-1)
                res[-1] = x * y
            elif i == '/':
                state = 1
                x = int(res[-2])
                y = int(res[-1])
                res.pop(-1)
                if x < 0:
                    state = 1 - state
                if y < 0:
                    state = 1 - state
                if state:
                    res[-1] = int(x / y)
                else:
                    res[-1] = int(abs(x) / abs(y)) *(-1)
                
        return res[0]
