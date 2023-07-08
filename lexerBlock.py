from file_manager import* # Импортирование модуля работы с файлом для отвергания заведомо неправильной цепочки.
# Функция, которая выполняет лексический анализ каждой лексемы в списке arrStr и возвращает список результатов result_words.
def Lexer(arrStr):
    result_words, current_state, current_word, num16, arr = [], "start", "", list("ABCDEF"), arrStr #num16 - буквы, которые могут встречаться в 16-ричных числах
    arr.append(("@", "end")) # Добавление в конец двумерного массива ("@", "end") для корректного прохода по всем лексемам.

    for lexems in arr:
        if current_state == "start": #Начальное состояние
            if lexems[0].isalpha():
                current_state = "char"
                current_word += lexems[0]
            elif lexems[0].isdigit():
                current_state = "number"
                current_word += lexems[0]
            elif lexems[0] == "=":
                current_state = "start"
                result_words.append((lexems[0], "равно"))
            elif lexems[0] == "$":
                current_state = "dollar"
                current_word += lexems[0]
            elif lexems[0] == "-":
                current_state = "znak"
                current_word += lexems[0]
            elif lexems[0] == "+":
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
            elif lexems[1] == "ошибка":
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
            elif lexems[0] == "\'":
                current_state = "quote1"
                current_word += lexems[0]
            elif lexems[0] == ";":
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "char": #Обработка идентификаторов
            if lexems[0].isalpha() or lexems[0].isdigit():
                current_word += lexems[0]
            else:
                result_words.append((current_word, "ИДЕНТ"))
                current_state = "start"
                current_word = ""
        elif current_state == "number": #Обработка чисел
            if lexems[0].isdigit():
                current_word += lexems[0]
            elif lexems[0] == "E": #Если в цепочке встречается символ "E",то статус меняется для проверки числа в экспоненциальной записи.
                current_word += lexems[0]
                current_state = "expNum"
            elif lexems[0] == ";":
                result_words.append((current_word, "ЦЕЛОЕ"))
                current_state = "end"
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "equal":
            current_state = "start"
            current_word = ""
        elif current_state == "dollar": #Если в цепочке встречается символ "$",то статус меняется для проверки 16-ричной константы.
            if lexems[0].isdigit() or lexems[0] in num16:
                current_state = "hexNum"
                current_word += lexems[0]
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "hexNum":#Обработка 16-ричных констант.
            if lexems[0].isdigit() or lexems[0] in num16:
                current_word += lexems[0]
            elif lexems[0] == ";":
                result_words.append((current_word, "16-РИЧ"))
                current_state = "end"
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "quote1": #Открывающая кавычка строковой константы
            if lexems[0].isdigit() or lexems[0].isalpha():
                current_state = "str"
                current_word += lexems[0]
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "str":
            if lexems[0].isdigit() or lexems[0].isalpha():
                current_word += lexems[0]
            elif lexems[0] == "\'":
                current_word += lexems[0]
                current_state = "quote2"
                result_words.append((current_word, "СТРКОНСТ"))
            else:
                print("\nОшибка в лексике") #Если после открывающей кавыч. не встречается закр. кавычка,то это ошибка.
                data_output(0)
                exit(0)
        elif current_state == "quote2":
            if lexems[0] == ";":
                current_state = "end"
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "znak":
            if lexems[0].isdigit():
                current_word += lexems[0]
                current_state = "number"
            elif lexems[0] == "E": #Если после "-" идёт "E", то статус меняется на "expNum" для обработки экспоненциальной запись числа.
                current_word += lexems[0]
                current_state = "expNum"
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "expNum":
            if lexems[0].isdigit():
                current_word += lexems[0]
                current_state = "expNum"
            elif lexems[0] == "-":
                current_word += lexems[0]
                current_state = "expNum2"
            elif lexems[0] == ";":
                result_words.append((current_word, "ВЕЩКОНСТ"))
                current_state = "end"
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "expNum2": #Если после "-" не идет число, то это ошибка в лексике (Например: 1E-)
            if lexems[0].isdigit():
                current_word += lexems[0]
                current_state = "expNum"
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "end": #Обработка конца цепочки
            if current_word != "":
                result_words.append((';', "тчкзпт"))
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)

    return result_words
