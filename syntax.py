def Syntax(string):

    status = "0"
    classes = ["number", "decimalNum", "str"]
    znak = ["minus", "plus"]

    for i in range(len(string)):
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
        elif string[i][1] == "минус":
            if status == "equal" or (status == "decimalNum" or status == "number"):
                status = "minus"
            else:
                return 0
        elif string[i][1] == "плюс":
            if status == "decimalNum" or status == "number":
                status = "plus"
            else:
                return 0
        elif string[i][1] == "ЦЕЛОЕ":
            if status in znak or status == "equal" or status == "dollar":
                status = "number"
            else:
                return 0
        elif string[i][1] == "доллар":
            if status == "equal":
                status = "dollar"
            else:
                return 0
        #Не уверен, что не могу складывать строки для своего варианта /-_-|
        elif string[i][1] == "СТРКОНСТ":
            if status == "equal":
                status = "str"
            else:
                return 0
        elif string[i][1] == "ВЕЩКОНСТ":
            if status == "equal" or status in znak:
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
