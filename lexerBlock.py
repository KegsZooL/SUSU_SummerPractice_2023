def Lexer(arrStr):
    global word, numbers, num16, resultWords, specSymbols, id, arr

    word, numbers, num16, resultWords, specSymbols, id, arr = "", list("123456789"), list("ABCDEF"), [], \
        ("тчкзпт", "равно", "одинкавыч", "буква", "цифра", "точка"), -1, arrStr

    arr.append(("@", "end"))
    main()

    return resultWords

def main():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]
    if tmp == "буква":
        word += arr[id][0]
        checkChar()
    elif tmp == "цифра":
        word += arr[id][0]
        checkNum()
    elif tmp == "одинкавыч":
        word += arr[id][0]
        checkStr()
    elif tmp == "пробел":
        main()
    elif tmp in specSymbols:
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "тире":
        if arr[id + 1][1] == "цифра" or arr[id + 1][0] == "E":
            word += arr[id][0]
            checkNum()
        else:
            resultWords.append((arr[id][0], arr[id][1]))
            main()
    elif tmp == "доллар":
        resultWords.append((arr[id][0], arr[id][1]))
        checkNum16()

def checkChar():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]

    if tmp == "буква":
        word += arr[id][0]
        checkChar()
    elif tmp == "цифра":
        word += arr[id][0]
        checkChar()
    elif tmp == "пробел":
        resultWords.append((word, "идентификатор"))
        word = ""
        main()
    elif tmp == "тире":
        if arr[id + 1][1] == "цифра" or arr[id + 1][0] == "E":
            word += arr[id][0]
            checkNum()
        else:
            resultWords.append((word, "идентификатор"))
            word = ""
            id -= 1
            main()
    elif tmp == "end":
        resultWords.append((word, "идентификатор"))

def checkNum():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]

    if tmp == "цифра":
        word += arr[id][0]
        checkNum()
    elif arr[id][0] == "." and arr[id + 1][1] == "цифра":
        word += arr[id][0]
        checkDecimal()
    elif arr[id][0] == "E":
        word += arr[id][0]
        checkExponent()
    elif tmp in specSymbols:
        resultWords.append((word, "целое"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "тире":
        resultWords.append((word, "целое"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "end":
        resultWords.append((word, "целое"))

def checkNum16():
    global word, resultWords, id
    id += 1
    tmp = arr[id][0]
    tmp_1 = arr[id][1]

    if tmp in num16:
        word += arr[id][0]
        checkNum16()
    elif tmp_1 == "цифра":
        word += arr[id][0]
        checkNum16()
    elif tmp_1 in specSymbols or tmp_1 == "пробел":
        if word != "":
            resultWords.append((word, "16-ричная константа"))
            word = ""
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp_1 == "тире":
        if word != "":
            resultWords.append((word, "16-ричная константа"))
            word = ""
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp_1 == "end":
        if word != "":
            resultWords.append((word, "16-ричная константа"))

def checkStr():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]

    if tmp == "буква" or tmp == "цифра":
        word += arr[id][0]
        checkStr()
    elif tmp == "одинкавыч":
        word += arr[id][0]
        resultWords.append((word, "строка"))
        word = ""
        main()
    elif tmp == "end":
        resultWords.append((word, "строка"))

def checkDecimal():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]
    if tmp == "цифра":
        word += arr[id][0]
        checkDecimal()
    elif arr[id][0] == "E":
        word += arr[id][0]
        checkExponent()
    elif tmp in specSymbols:
        resultWords.append((word, "вещественная константа"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "end":
        resultWords.append((word, "вещественная константа"))

def checkExponent():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]

    if tmp == "цифра":
        word += arr[id][0]
        checkExponent()
    elif tmp == "тире" and arr[id + 1][1] == "цифра":
        word += arr[id][0]
        checkExponent()
    elif tmp in specSymbols:
        resultWords.append((word, "вещественная константа"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "end":
        resultWords.append((word, "вещественная константа"))
