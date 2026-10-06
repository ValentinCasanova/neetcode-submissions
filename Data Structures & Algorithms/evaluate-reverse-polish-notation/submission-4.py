class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                op2, op1 = stack.pop(), stack.pop()
                match token:
                    case '+':
                        stack.append(int(op1) + int(op2))
                    case '-':
                        stack.append(int(op1) - int(op2))
                    case '/':
                        stack.append(int(int(op1) / int(op2)))
                    case '*':
                        stack.append(int(op1) * int(op2))
            else:   
                stack.append(token)
        return int(stack.pop())