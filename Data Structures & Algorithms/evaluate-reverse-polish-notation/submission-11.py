class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            match i:
                case '+':
                    op2, op1 = stack.pop(), stack.pop()
                    stack.append(op1 + op2)
                case '-':
                    op2, op1 = stack.pop(), stack.pop()
                    stack.append(op1 - op2)
                case '*':
                    op2, op1 = stack.pop(), stack.pop()
                    stack.append(op1 * op2)
                case '/':
                    op2, op1 = stack.pop(), stack.pop()
                    stack.append(int(op1 / op2))
                case _:
                    stack.append(int(i))
        return stack[0]