def Syntax(string):

    status = "0"
    classes = ["hexadecimal", "number", "decimalNum", "str", "bool"]

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
        elif string[i] == "минус":
            if status == "equal" or (status == "decimalNum" or status == "number"):
                status = "minus"
            else:
                return 0
        elif string[i] == "плюс":
            if status == "decimalNum" or status == "number":
                status = "plus"
            else:
                return 0
        elif string[i] == "ЦЕЛОЕ":
            if status == "плюс" or status == "minus" or status == "equal" or status == "dollar":
                status = "number"
            else:
                return 0
        elif string[i] == "доллар":
            if status == "equal":
                status = "dollar"
            else:
                return 0
        #Не уверен, что могу складывать строки для своего варианта /-_-|
        elif string[i] == "СТРОКОВАЯ КОНСТАНТА":
            if status == "equal":
                status = "str"
            else:
                return 0

        # elif string[i] == "ВЕЩЕСТВЕННАЯ КОНСТАНТА":
        #     if status == ""
        # elif string[i] == "ЛОГКОНСТ_TRUE":
        #     if status == "equal":
        #         status = "bool"
        #     else:
        #         return 0
        elif string[i] == "тчкзпт":
            if status in classes: #переделать
                status = "end"
            else:
                return 0

    if status == "end":
        return 1
