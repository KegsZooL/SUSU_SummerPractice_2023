def Syntax(string):
    status = "0"
    classes = ["number", "decimalNum", "str", "hexNum"]

    for i in range(len(string)):
        print(status)
        if "КЛСЛОВО_" in string[i][1]:
            if status == "0":
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
        elif string[i][1] == "знак":
            if status == "equal" or (status == "decimalNum" or status == "number"):
                status = "znak"
            else:
                return 0
        elif string[i][1] == "ЦЕЛОЕ":
            if status == "equal":
                status = "number"
            else:
                return 0
        elif string[i][1] == "16-РИЧ" and (string[i - 1][1] != "точка" and string[i + 1][1] != "точка"):
            if status == "dollar":
                status = "hexNum"
            else:
                return 0
        elif string[i][1] == "доллар" and (string[i - 1][1] != "точка" and string[i + 1][1] != "точка"):
            if status == "equal":
                status = "dollar"
            else:
                return 0
        elif string[i][1] == "СТРКОНСТ" and (string[i - 1][1] != "точка" and string[i + 1][1] != "точка"):
            if status == "equal":
                status = "str"
            else:
                return 0
        elif string[i][1] == "ВЕЩКОНСТ" and (string[i - 1][1] != "точка" and string[i + 1][1] != "точка"):
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
