# Импортирование основных модулей
from file_manager import*
from transliteration import tansliteration as trl
from lexerBlock import*
from identifical import*
from syntax import*

string = data_input()
lexems = trl(string)
words = Lexer(lexems)
str = identification(words)
result = Syntax(str)
data_output(result)
