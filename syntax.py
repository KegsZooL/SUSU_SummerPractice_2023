def Syntax(string):

    status = "0"
    classes = ["hexadecimal", "number", "decimalNum", "str", "bool", "minus"]

    for i in range(len(string)):
        print(status)
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
        elif string[i] == "ВЕЩЕСТВЕННАЯ КОНСТАНТА":
            if status == "equal":
                status = "decimalNum"
            else:
                return 0
        elif string[i] == "СТРОКОВАЯ КОНСТАНТА":
            if status == "equal":
                status = "str"
            else:
                return 0
        elif string[i] == "ЛОГКОНСТ_TRUE":
            if status == "equal":
                status = "bool"
            else:
                return 0
        elif string[i] == "минус":
            if status == "equal" and string[i + 1] == "ВЕЩЕСТВЕННАЯ КОНСТАНТА":
                status = "minus"
            else:
                return 0
        elif string[i] == "тчкзпт":
            if status in classes:
                status = "end"
            else:
                return 0

    if status == "end":
        return 1
