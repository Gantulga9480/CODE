class SignPriority:

    def __init__(self, expression = None, brackets_list = None):
        self.expression = expression
        self.brackets_list = brackets_list
        self.s_list = [["!", "!"], ["^", "^"],["×", "/"],["%", "%"], ["+", "-"]]

    def sign(self, bracket_index = None):
        bracket_list = self.brackets_list[bracket_index]
        sign_list = []
        for i in range(len(self.s_list)):
            bracket_hit = 0
            index = bracket_list[0] + 1
            while index < bracket_list[1]:
                char = self.expression[index]
                if bracket_hit > 0:
                    if char == ")":
                        bracket_hit -= 1
                    elif char == "(":
                        bracket_hit += 1
                    else:
                        pass
                else:
                    if char == "(":
                        bracket_hit += 1
                    else:
                        if char.isdigit():
                            pass
                        else:
                            if char == self.s_list[i][0]:
                                sign_list.append(char)
                            elif char == self.s_list[i][1]:
                                sign_list.append(char)
                            else:
                                pass
                index += 1
        if len(sign_list) == 0:
            return False
        else:
            return sign_list.copy()