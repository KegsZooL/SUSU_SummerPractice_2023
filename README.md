Распознаватель заданной символьной цепочки. Символьная цепочка задается с помощью формул Бэкуса-Наура. Формулы Бэк-уса-Наура, определяющие нетерминальные цепочки:
<цепочка>::=CONST <идентификатор>=<значение>;
<идентификатор>::=<буква> | <идентификатор><буква> |
<идентификатор><цифра>
<буква>::=A | B | C | D | E | F | ... | Z
<цифра>::=0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<значение>::=<целая константа> | <логическая константа>
<целая константа>::=<целое со знаком> | <целое без знака>
<целое со знаком>::=<знак><целое без знака>
<знак>::=+ | -
<целое без знака>::=<цифра> | <целое без знака>
<логическая константа>::=TRUE | FALSE
