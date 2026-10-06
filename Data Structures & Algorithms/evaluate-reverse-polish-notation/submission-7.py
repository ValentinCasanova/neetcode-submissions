class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2 + op1)
                case '-':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2 - op1)
                case '*':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(op2 * op1)
                case '/':
                    op1 = stack.pop()
                    op2 = stack.pop()
                    stack.append(int(op2 / op1))
                case _:
                    stack.append(int(token))
        return stack.pop()
