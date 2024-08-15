class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop()+stack.pop())
            elif token == '-':
                stack.append(-stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                result = abs(b)//abs(a)
                if a * b < 0:
                    result = -result
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()
            