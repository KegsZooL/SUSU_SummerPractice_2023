def Syntax(string):
    status = "start"
    classes = ["number", "decimalNum", "str", "hexNum"]

    for i in range(len(string)):
        print(string[i][1])
        if "КЛСЛОВО_" in string[i][1]:
            if status == "start":
                status = "keyword"
            else:
                return 0
        elif string[i][1] == "ИДЕНТ":
            if status == "keyword":
                status = "identification"
            else:
                return 0
        elif string[i][1] == "равно":
            if status == "identification":
                status = "equal"
            else:
                return 0
        elif string[i][1] == "знак": #После равно может идти отрицательный знак перед вещественным числом или перед обычным числом
            if status == "equal" or (status == "decimalNum" or status == "number"):
                status = "znak"
            else:
                return 0
        elif string[i][1] == "ЦЕЛОЕ":
            if status == "equal":
                status = "number"
            else:
                return 0
        elif string[i][1] == "16-РИЧ":
            if status == "equal":
                status = "hexNum"
            else:
                return 0
        elif string[i][1] == "СТРКОНСТ":
            if status == "equal":
                status = "str"
            else:
                return 0
        elif string[i][1] == "ВЕЩКОНСТ":
            if status == "equal" or status == "znak":
                status = "decimalNum"
            else:
                return 0
        elif string[i][1] == "тчкзпт":
            if status in classes:
                status = "end"
            else:
                return 0
    if status == "end":
        return 1
    return 0
