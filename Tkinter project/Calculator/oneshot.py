class OneShot:

    def __init__(self, expression=None):
        self.expression = expression
        bracket = br.BracketPair(expression=self.expression)
        self.bracket_pair = bracket.pair()

    def one(self):
        # lst = list(self.expression)
        mode_list = list()
        if not self.bracket_pair:
            print("Bracket Error in one shot")
        else:
            mode_list = ["default"] * len(self.bracket_pair)

            for index, items in enumerate(self.bracket_pair):
                sign = []
                sign_hit = False
                i = items[0]
                if items[1] == len(self.expression) - 1:
                    pass
                else:
                    if self.expression[items[1] + 1] == "!":
                        pass
                while not sign_hit:
                    i -= 1
                    if self.expression[i] == "+" or self.expression[i] == "-" or self.expression[i] == "/" or self.expression[i] == "×" or self.expression[i] == "^" or self.expression[i] == "(":
                        sign_hit = True
                    else:
                        sign.append(self.expression[i])
                sign.reverse()
                sign = "".join(sign)
                if sign == "sqrt":
                    mode_list[index] = "sqrt"
                elif sign == "sin":
                    mode_list[index] = "sin"
                elif sign == "cos":
                    mode_list[index] = "cos"
                elif sign == "tan":
                    mode_list[index] = "tan"
                elif sign == "asin":
                    mode_list[index] = "sin"
                elif sign == "acos":
                    mode_list[index] = "cos"
                elif sign == "atan":
                    mode_list[index] = "tan"
                elif sign == "ln":
                    mode_list[index] = "ln"
                elif sign == "log":
                    mode_list[index] = "log"
            return mode_list.copy()
