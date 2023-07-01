from file_manager import data_input, data_output
from transliteration import tansliteration as trl
from lexerBlock import Lexer


string = data_input()
lexems = trl(string)
l = Lexer(lexems)

print(lexems)



print(l, '\n')