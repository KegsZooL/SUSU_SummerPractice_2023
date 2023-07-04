from file_manager import*
def identification(words):

    arr = []
    keyWord =  "const"
    boolConst = ["true", "false"]
    pascaleWords = ["and", "array", "as", "begin", "break",
                "case", "class", "xor", "constructor", "continue",
                "destructor", "div", "do", "downto", "else",
                "end", "exit", "external", "externalsync", "file",
                "finalization", "for", "forward", "function", "if",
                "in", "inherited", "intialization", "is", "mod",
                "not", "of", "or", "private", "procedure",
                "program", "property", "protected", "public", "record",
                "repeat", "set", "shl", "shr", "sizeof",
                "string", "then", "to", "type", "unit", "until", "uses", "var",
                "while", "with"]

    for i in words:
        if i[0].lower() in pascaleWords:

            arr.append("ОШИБКА")
            print("\nНЕДОПУСТИМОЕ НАЗВАНИЕ ПЕРЕМЕННОЙ")
            data_output(0)
            exit(0)
        elif i[0].lower() == keyWord:
            arr.append("КЛСЛОВО_" + i[0].upper())
        elif i[0].lower() in boolConst:
            arr.append("ЛОГКОНСТ_" + i[0].upper())
        else:
            arr.append(i[1])
    return arr
