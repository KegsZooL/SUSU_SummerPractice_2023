def classify_symbol(symbol): #Классификация спец.символа
    if symbol == '$':
        return "доллар"
    elif symbol == ';':
        return "тчкзпт"
    elif symbol == '=':
        return "равно"
    elif symbol == '\'':
        return "одинкавыч"
    elif symbol == ' ':
        return "пробел"
    elif symbol == '.':
        return "точка"
    elif symbol == '-':
        return "тире"
def tansliteration(string):
     alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") #Список алфавита
     numbers = list("0123456789") #Список цифр
     sym = ['$', ';', '=', '\'', ' ', '-', '.'] #Список спец.символов

     arrSymbols = [] #Создаем список, куда будем помещать символы с их классами
     i = 0
     while i < len(string):
         if string[i] in alphabet:
             alp = (string[i], "буква")
             arrSymbols.append(alp)
         elif string[i] in numbers:
             num = (string[i], "цифра")
             arrSymbols.append(num)
         elif string[i] in sym:
             spec = (string[i], classify_symbol(string[i]))
             arrSymbols.append(spec)
         else:
             err = (string[i], "ошибка")
             arrSymbols.append(err)
             print(f"Недопустимый символ {string[i]}")
         i += 1

     return arrSymbols


