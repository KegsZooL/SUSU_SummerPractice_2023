from file_manager import*
def identification(words):

    arr = []

    keyWords = "const"
    banWords = ["and", "array", "as", "begin", "break",
                "case", "class", "xor", "constructor", "continue",
                "destructor", "div", "do", "downto", "else",
                "end", "exit", "external", "externalsync", "file",
                "finalization", "for", "forward", "function", "if",
                "in", "inherited", "intialization", "is", "mod",
                "not", "of", "or", "private", "procedure",
                "program", "property", "protected", "public", "record",
                "repeat", "set", "shl", "shr", "sizeof",
                "string", "then", "to", "type", "unit",
                "until", "uses", "var", "while", "with", "with"]

    for i in words:
        if i[0].lower() == "ИДЕНТИФИКАТОР":
            if i in banWords:
                arr.append("ОШИБКА")
                print("\nНЕДОПУСТИМЫЙ СИМВОЛ")

                data_output(0)
                exit(0)
        elif i[0].lower() == keyWords:
            arr.append("КЛСЛОВО_" + i[0].upper())
        else:
            arr.append(i[1])
    return arr
