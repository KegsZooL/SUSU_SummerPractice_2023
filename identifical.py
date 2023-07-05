def identification(words):

    arr = []
    keyWord = "const"
    boolConst = ["true", "false"]
    pascaleWords = ["procedure", "program", "record", "reintroduce", #Полный список зарезервированных слов в языке Pascal
                    "function", "goto", "if", "implementation",
                    "constructor", "destructor", "div", "do",
                    "in", "inherited", "inline", "interface",
                    "unit", "until", "uses", "var", "while",
                    "and", "asm", "array", "begin", "case",
                    "downto", "else", "end", "file", "for",
                    "shr", "string", "then", "to", "type",
                    "object", "of", "or", "packed",
                    "repeat", "self", "set", "shl",
                    "label", "mod", "nil", "not",
                    "with", "xor"]

    for i in words:
        if i[0].lower() in pascaleWords:
            arr.append((i[0], "ПАСКАЛЬ_" + i[0].upper()))
            print(f"\nНедопустимое название переменной: {i[0].lower()}")
        elif i[0].lower() == keyWord:
            arr.append((i[0], "КЛСЛОВО_" + i[0].upper()))
        elif i[0].lower() in boolConst:
            arr.append(("ЛОГКОНСТ_" + i[0].upper()))
        else:
            arr.append((i[0], i[1]))
    return arr
