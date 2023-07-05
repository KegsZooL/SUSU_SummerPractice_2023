def identification(words):

    arr = []
    keyWord = "const"
    pascaleWords = ["and", "array", "asm", "begin", "case", "const", "constructor",
                    "destructor", "div", "do", "downto", "else", "end", "fasle", "file",
                    "for", "function", "goto", "if", "implementation", "in",
                    "inherited", "inline", "interface", "label", "mod", "nil",
                    "not", "object", "of", "or", "packed", "procedure", "program",
                    "record", "reintroduce", "repeat", "self", "set", "shl", "shr",
                    "string", "then", "to", "true", "type", "unit", "until", "uses", "var",
                    "while", "with", "xor"]

    for i in words:
        if i[0].lower() == keyWord:
            arr.append((i[0], "КЛСЛОВО_" + i[0].upper()))
        elif i[0].lower() in pascaleWords:
            arr.append((i[0], "ПАСКАЛЬ_" + i[0].upper()))
            print(f"\nНедопустимое название переменной: {i[0].lower()}")
        else:
            arr.append((i[0], i[1]))
    return arr
