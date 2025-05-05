from typing import List

def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = operand1 + operand2
                stack.append(result)
            elif token == "-":
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = operand2 - operand1
                stack.append(result)
            elif token == "*":
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = operand1 * operand2
                stack.append(result)
            elif token == "/":
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = int(operand2 / operand1)
                stack.append(result)
            else:
                stack.append(int(token))
            
        return stack[0]