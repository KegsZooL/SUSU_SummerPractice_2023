# Главная функция, которая выполняет лексический анализ списка строк arrStr.
# Вызывает функцию main() для анализа каждой лексемы в списке и возвращает список результатов resultWords.
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
        Char()
    elif tmp == "цифра":
        word += arr[id][0]
        Num()
    elif tmp == "одинкавыч":
        word += arr[id][0]
        Str()
    elif tmp == "пробел":
        main()
    elif tmp in specSymbols:
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "минус":
        if arr[id + 1][1] == "цифра" or arr[id + 1][0] == "E":
            resultWords.append((arr[id][0], arr[id][1]))
            word = ""
            Num()
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
        Num16()

# Функция для проверки буквенного символа.
def Char():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]

    if tmp == "буква":
        word += arr[id][0]
        Char()
    elif tmp == "цифра":
        word += arr[id][0]
        Char()
    elif tmp == "пробел":
        resultWords.append((word, "ИДЕНТ"))
        word = ""
        main()
    elif tmp == "минус":
        if arr[id + 1][1] == "цифра" or arr[id + 1][0] == "E":
            word += arr[id][0]
            Num()
        else:
            resultWords.append((word, "ИДЕНТ"))
            word = ""
            id -= 1
            main()
    elif tmp == "тчкзпт":
        resultWords.append((word, "ИДЕНТ"))
        word = ""
        id -= 1
        main()
    elif tmp == "end":
        resultWords.append((word, "ИДЕНТ"))

# Функция для проверки цифры.
def Num():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]

    if tmp == "цифра":
        word += arr[id][0]
        Num()
    elif arr[id][0] == "." and arr[id + 1][1] == "цифра":
        word += arr[id][0]
        Decimal()
    elif arr[id][0] == "E":  # Если встречается символ "E", то функция вызывает Exponent() для проверки числа в экспоненциальной записи.
        word += arr[id][0]
        Exponent()
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
        Num()
    elif tmp == "минус":
        resultWords.append((word, "ЦЕЛОЕ"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "end":
        resultWords.append((word, "ЦЕЛОЕ"))

# Функция для проверки 16-ричных констант
def Num16():
    global word, resultWords, id
    id += 1
    tmp = arr[id][0]
    tmp_1 = arr[id][1]

    err = ["пробел", "минус", "плюс", "буква"]

    if tmp in num16:
        word += arr[id][0]
        Num16()
    elif tmp_1 == "цифра":
        word += arr[id][0]
        Num16()
    elif tmp_1 in err: # Ошибка в лексике, если в цепочке после $ встречается недопустимый символ для 16-ричных чисел.
            resultWords.append((arr[id][0], "ОШИБКА"))
            Error()
    elif tmp_1 == "тчкзпт":
        resultWords.append((word, "ЦЕЛОЕ"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp_1 == "end":
        if word != "":
            resultWords.append((word, "ЦЕЛОЕ"))

# Функция для проверки строки, которая находится внутри одинарных кавычек.
# Функция продолжает анализ до тех пор, пока не встретит закрывающую одинарную кавычку.
def Str():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]

    if tmp == "буква" or tmp == "цифра":
        word += arr[id][0]
        Str()
    elif tmp == "одинкавыч":
        word += arr[id][0]
        resultWords.append((word, "СТРКОНСТ"))
        word = ""
        main()
    elif tmp == "end":
        resultWords.append((word, "СТРКОНСТ"))

# Это функция нужна, если в строке находиться вещественное число.
# Если тип является цифрой, функция продолжает анализ до тех пор, пока не встретит цифру или специальный символ. Если встречается символ "E", функция вызывает функцию Exponent()
def Decimal():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]
    if tmp == "цифра":
        word += arr[id][0]
        Decimal()
    elif arr[id][0] == "E":
        word += arr[id][0]
        Exponent()
    elif tmp in specSymbols:
        resultWords.append((word, "ВЕЩКОНСТ"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "end":
        resultWords.append((word, "ВЕЩКОНСТ"))

# Эта функция нужна, если в строке находится экспоненциальная запись числа.
def Exponent():
    global word, resultWords, id
    id += 1
    tmp = arr[id][1]

    if tmp == "цифра":
        word += arr[id][0]
        Exponent()
    elif tmp == "минус" and arr[id + 1][1] == "цифра":
        word += arr[id][0]
        Exponent()
    elif tmp in specSymbols:
        resultWords.append((word, "ВЕЩКОНСТ"))
        resultWords.append((arr[id][0], arr[id][1]))
        main()
    elif tmp == "пробел":
        resultWords.append((word, "ВЕЩКОНСТ"))
        word = ""
        main()
    elif tmp == "end":
        resultWords.append((word, "ВЕЩКОНСТ"))
def Error():
    print("\nОшибка в лексике")
