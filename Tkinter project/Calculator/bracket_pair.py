class BracketPair:

    def __init__(self, expression = None):
        self.expression = expression

    def pair(self):
        inv_expression = self.expression[::-1]
        length = len(self.expression)
        bracket_enter = True
        bracket_close = True
        index = 0
        index_len = 0
        brackets_enter = list()
        brackets_close = list()
        while bracket_enter:
            index = self.expression[index:length].find("(")
            if index != -1:
                index = index_len + index + 1
                index_len = index
                brackets_enter.append(index-1)
            else:
                bracket_enter = False
        index = 0
        index_len = 0
        while bracket_close:
            index = inv_expression[index:length].find(")")
            if index != -1:
                index = index_len + index + 1
                index_len = index
                brackets_close.append(length - index)
            else:
                bracket_close = False
        brackets_enter = brackets_enter[::-1]
        x = len(brackets_close)
        y = len(brackets_enter)
        if x == y:
            enter_paired = list()
            close_paired = list()
            brackets_pair = list()
            loop = 0
            enter_paired = [False] * x
            close_paired = [False] * x
            for index, item in enumerate(brackets_enter):
                loop += 1
                count = 0
                num = 0
                for idx, itm in enumerate(brackets_close):
                    num += 1
                    if item < itm and num < x:
                        pass
                    elif item > itm:
                        num = 0
                        while enter_paired[index] == False:
                            count += 1
                            if close_paired[idx - count]:
                                pass
                            else:
                                brackets_pair.append([item, brackets_close[idx - count]])
                                close_paired[idx - count] = True
                                enter_paired[index] = True
                    elif num == x:
                        num = 0
                        while enter_paired[index] == False:
                            if close_paired[idx - count]:
                                pass
                            else:
                                brackets_pair.append([item, brackets_close[idx - count]])
                                close_paired[idx - count] = True
                                enter_paired[index] = True
                            count += 1
            return brackets_pair.copy()
        else:
            return False