class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            op1, op2 = 0, 0
            if i in ('+', '*', '/', '-'):
                op2, op1= stack.pop(), stack.pop()
            match i:
                case '+':
                    stack.append(op1 + op2)
                case '*':
                    stack.append(op1 * op2)
                case '/':
                    stack.append(int(op1 / op2))
                case '-':
                    stack.append(op1 - op2)
                case _:
                    stack.append(int(i))
        return stack[0] if stack else int(tokens[0])