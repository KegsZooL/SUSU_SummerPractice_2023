# Главная функция, которая выполняет лексический анализ списка строк arrStr.
# Dызывает функцию main() для анализа каждой лексемы в списке и возвращает список результатов resultWords.
def Lexer(arrStr):
    global word, numbers, num16, resultWords, specSymbols, id, arr

    word, numbers, num16, resultWords, specSymbols, id, arr = "", list("123456789"), list("ABCDEF"), [], \
        ("тчкзпт", "равно", "одинкавыч", "буква", "цифра", "точка", "плюс"), -1, arrStr

    arr.append(("@", "end"))  # Добавление в конец двумерного массива ("@", "end") для корректного завершения рекурсии.
    main()

    return resultWords

# Основная функция, которая анализирует тип текущей лексемы и вызывает соответствующую функцию проверки для обработки лексемы.
def main():
    global word, resultWords, id  # Заново объявляем некоторые переменные для их изменения.
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
    elif tmp == "минус":
        if arr[id + 1][1] == "цифра" or arr[id + 1][0] == "E":
            resultWords.append((arr[id][0], arr[id][1]))
            word = ""
            checkNum()
    # elif tmp == "минус":
    #     if arr[id + 1][1] == "цифра" or arr[id + 1][0] == "E":
    #         word += arr[id][0]
    #         checkNum()
        else:
            resultWords.append((arr[id][0], arr[id][1]))
            main()
    elif tmp == "плюс":
        if arr[id + 1][1] == "цифра" or arr[id + 1][1] == "доллар":
            resultWords.append((arr[id][0], arr[id][1]))
            word = ""
            main()
    elif tmp == "доллар":
        resultWords.append((arr[id][0], arr[id][1]))
        checkNum16()

# Функция для проверки буквенного символа.
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
        resultWords.append((word, "ИДЕНТИФИКАТОР"))
        word = ""
        main()
    elif tmp == "минус":
        if arr[id + 1][1] == "цифра" or arr[id + 1][0] == "E":
            word += arr[id][0]
            checkNum()
        else:
            resultWords.append((word, "ИДЕНТИФИКАТОР"))
            word = ""
            id -= 1
            main()
    elif tmp == "тчкзпт":
        resultWords.append((word, "ИДЕНТИФИКАТОР"))
        word = ""
        id -= 1
        main()
    elif tmp == "end":
        resultWords.append((word, "ИДЕНТИФИКАТОР"))

# Функция для проверки цифры.
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
    elif arr[id][0] == "E":  # Если встречается символ "E", то функция вызывает checkExponent() для проверки числа в экспоненциальной записи.
        word += arr[id][0]
        checkExponent()
    elif tmp in specSymbols:
        resultWords.append((word, "ЦЕЛОЕ"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "пробел":
        resultWords.append((word, "ЦЕЛОЕ"))
        word = ""
        main()
    elif tmp == "буква":
        word += arr[id][0]
        checkNum()
    elif tmp == "минус":
        resultWords.append((word, "ЦЕЛОЕ"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "end":
        resultWords.append((word, "ЦЕЛОЕ"))

# Функция для проверки 16-ричных констант
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
            resultWords.append((word, "ЦЕЛОЕ"))
            word = ""
        if tmp_1 != "пробел":
            resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp_1 == "минус":
        if word != "":
            resultWords.append((word, "ЦЕЛОЕ"))
            word = ""
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp_1 == "end":
        if word != "":
            resultWords.append((word, "ЦЕЛОЕ"))

# Функция для проверки строки, которая находится внутри одинарных кавычек.
# Функция продолжает анализ до тех пор, пока не встретит закрывающую одинарную кавычку.
def checkStr():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]

    if tmp == "буква" or tmp == "цифра":
        word += arr[id][0]
        checkStr()
    elif tmp == "одинкавыч":
        word += arr[id][0]
        resultWords.append((word, "СТРОКОВАЯ КОНСТАНТА"))
        word = ""
        main()
    elif tmp == "end":
        resultWords.append((word, "СТРОКОВАЯ КОНСТАНТА"))

# Это функция нужна, если в строке находиться вещественное число.
# Если тип является цифрой, функция продолжает анализ до тех пор, пока не встретит цифру или специальный символ. Если встречается символ "E", функция вызывает функцию checkExponent()
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
        resultWords.append((word, "ВЕЩЕСТВЕННАЯ КОНСТАНТА"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "end":
        resultWords.append((word, "ВЕЩЕСТВЕННАЯ КОНСТАНТА"))

# Эта функция нужна, если в строке находится экспоненциальная запись числа.
def checkExponent():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]

    if tmp == "цифра":
        word += arr[id][0]
        checkExponent()
    elif tmp == "минус" and arr[id + 1][1] == "цифра":
        word += arr[id][0]
        checkExponent()
    elif tmp in specSymbols:
        resultWords.append((word, "ВЕЩЕСТВЕННАЯ КОНСТАНТА"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "пробел":
        resultWords.append((word, "ВЕЩЕСТВЕННАЯ КОНСТАНТА"))
        word = ""
        main()
    elif tmp == "end":
        resultWords.append((word, "ВЕЩЕСТВЕННАЯ КОНСТАНТА"))
