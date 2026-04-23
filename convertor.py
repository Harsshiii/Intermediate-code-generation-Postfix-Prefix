class ExpressionConverter:
    def __init__(self):
        self.precedence = {
            '+': 1, '-': 1,
            '*': 2, '/': 2,
            '^': 3
        }

    def is_operator(self, c):
        return c in self.precedence

    def infix_to_postfix(self, expression):
        stack = []
        output = []

        tokens = expression.split()

        for token in tokens:
            if token.isalnum():
                output.append(token)

            elif token == '(':
                stack.append(token)

            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # remove '('

            elif self.is_operator(token):
                while (stack and stack[-1] != '(' and
                       self.precedence.get(stack[-1], 0) >= self.precedence[token]):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return " ".join(output)

    def infix_to_prefix(self, expression):
        # Reverse expression
        tokens = expression.split()[::-1]

        # Swap brackets
        for i in range(len(tokens)):
            if tokens[i] == '(':
                tokens[i] = ')'
            elif tokens[i] == ')':
                tokens[i] = '('

        reversed_expr = " ".join(tokens)

        # Convert to postfix
        postfix = self.infix_to_postfix(reversed_expr)

        # Reverse postfix → prefix
        prefix = postfix.split()[::-1]

        return " ".join(prefix)


if __name__ == "__main__":
    converter = ExpressionConverter()

    expr = input("Enter infix expression (space-separated): ")

    postfix = converter.infix_to_postfix(expr)
    prefix = converter.infix_to_prefix(expr)

    print("\nPostfix Expression:", postfix)
    print("Prefix Expression :", prefix)