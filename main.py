# Импортирование основных модулей
from file_manager import*
from transliteration import tansliteration as trl
from lexerBlock import*
from identifical import*

string = data_input()
lexems = trl(string)
words = Lexer(lexems)

x = identification(words)
