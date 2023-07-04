def Syntax(string):

    status = "0"
    classes = ["hexadecimal", "number", "decimalNum", "expNum"]

    for i in range(len(string)):
        if "КЛСЛОВО_" in string[i]:
            if status == "0":
                status = "keyword"
            else:
                return 0
        elif string[i] == "ИДЕНТИФИКАТОР":
            if status == "keyword":
                status = "identification"
            else:
                return 0
        elif string[i] == "равно":
            if status == "identification":
                status = "equal"
            else:
                return 0
        elif string[i] == "доллар":
            if status == "equal":
                status = "dollar"
            else:
                return 0
        elif string[i] == "ЦЕЛОЕ":
            if status == "dollar":
                status = "hexadecimal"
            elif status == "equal":
                status = "number"
            else:
                return 0
        # elif string[i] == "ВЕЩЕСТВЕННАЯ КОНСТАНТА":
        #     if status == "equal":
        #
        #     else:
        #         return 0
        elif string[i] == "тчкзпт":
            if status in classes:
                status = "end"
            else:
                return 0
        elif status == "end":
            return 0
    return 0