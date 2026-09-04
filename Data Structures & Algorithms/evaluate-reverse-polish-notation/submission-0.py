class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for i in tokens:
            if i in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[i](a,b))
            else:
                stack.append(int(i))
                
        return stack[0]