#define _CRT_SECURE_NO_WARNINGS
#define MAX_LEN_WORD 25
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const char* alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
const char* numbers = "0123456789";

// ������������� �������
const char* classifySymbol(char symbol)
{
    switch (symbol)
    {
    case '$': return "������";
    case ';': return "������";
    case '=': return "�����";
    case '\'': return "���������";
    case '-': return "����";
    case ' ': return "������";

    default: return "������";
    }
}

// �������������� ���������� ������� � ������� ������ (�������� ������)
char** trl(char* str)
{
    int length = strlen(str);
    char** arrSymbols = malloc(length * sizeof(char*));

    const char sym[] = { '$', ';', '=', '\'', '-', ' ' };
    const char* symbolClass = NULL;

    for (int i = 0; i < length; i++)
    {
        char symbol = str[i];

        if (strchr(alphabet, symbol))
            symbolClass = "�����";
        else if (strchr(numbers, symbol))
            symbolClass = "�����";
        else
        {
            int check = 0;
            for (int j = 0; j < sizeof(sym) / sizeof(sym[0]); j++)
            {
                if (sym[j] == symbol)
                {
                    symbolClass = classifySymbol(symbol);
                    check = 1;
                    break;
                }
            }
            if (check == 0)
                symbolClass = "������";
        }

        arrSymbols[i] = malloc(2 * sizeof(char));
        arrSymbols[i][0] = symbol;
        strcpy(arrSymbols[i] + 1, symbolClass);
    }

    return arrSymbols;
}