# Импортирование основных модулей
from file_manager import*
from transliteration import tansliteration as trl
from lexerBlock import*

string = data_input()
lexems = trl(string)
words = Lexer(lexems)
