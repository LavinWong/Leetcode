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
