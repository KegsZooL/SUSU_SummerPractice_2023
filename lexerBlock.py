from file_manager import*
def Lexer(arrStr):
    result_words, current_state, current_word, num16, arr = [], "start", "", list("ABCDEF"), arrStr
    arr.append(("@", "end"))

    for lexems in arr:
        if current_state == "start":
            if lexems[0].isalpha():
                current_state = "char"
                current_word += lexems[0]
            elif lexems[0].isdigit():
                current_state = "number"
                current_word += lexems[0]
            elif lexems[0] == "=":
                current_state = "equal"
                result_words.append((lexems[0], "равно"))
            elif lexems[0] == "$":
                current_state = "dollar"
                result_words.append((lexems[0], "доллар"))
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
                current_state = "singleQuote1"
                current_word += lexems[0]
            elif lexems[0] == ";":
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "char":
            if lexems[0].isalpha() or lexems[0].isdigit():
                current_word += lexems[0]
            else:
                result_words.append((current_word, "ИДЕНТ"))
                current_state = "start"
                current_word = ""
        elif current_state == "number":
            if lexems[0].isdigit():
                current_word += lexems[0]
            elif lexems[0] == "E":
                current_word += lexems[0]
                current_state = "expNum"
            elif lexems[0] == ";":
                result_words.append((current_word, "ЦЕЛОЕ"))
                result_words.append((lexems[0], "тчкзпт"))
                return result_words
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "equal":
                current_state = "start"
                current_word = ""
        elif current_state == "dollar":
            if lexems[0].isdigit() or lexems[0] in num16:
                current_state = "hexNum"
                current_word += lexems[0]
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "hexNum":
            if lexems[0].isdigit() or lexems[0] in num16:
                current_word += lexems[0]
            elif lexems[0] == ";":
                result_words.append((current_word, "16-РИЧ"))
                result_words.append((lexems[0], "тчкзпт"))
                return result_words
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "singleQuote1":
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
                current_state = "singleQuote2"
                result_words.append((current_word, "СТРКОНСТ"))
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "singleQuote2":
            if lexems[0] == ";":
                result_words.append((lexems[0], "тчкзпт"))
                return result_words
            else:
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "znak":
            if lexems[0].isdigit():
                current_word += lexems[0]
                current_state = "number"
        elif current_state == "expNum":
            if lexems[0].isdigit():
                current_word += lexems[0]
                current_state = "expNum"
            elif lexems[1] == "знак":
               current_word += lexems[0]
               current_state = "znak1"
            elif lexems[0] == ";":
                print("\nОшибка в лексике")
                data_output(0)
                exit(0)
        elif current_state == "znak1":
            if lexems[0].isdigit():
                current_word += lexems[0]
                current_state = "znak1"
            else:
                result_words.append((current_word, "ВЕЩКОНСТ"))
                result_words.append((lexems[0], lexems[1]))
                return result_words
    return result_words
