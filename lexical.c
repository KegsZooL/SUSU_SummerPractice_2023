#define _CRT_SECURE_NO_WARNINGS
#define MAX_LEN_WORD 50

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "transliteration.h"

char** lexical(char** lexemes)
{
    int len = 0;
    while (lexemes[len] != NULL)
        len++;

    char** resultWords = malloc(len * sizeof(char*));
    char word[MAX_LEN_WORD];
    int count = 0;

    for (int i = 0; i < len; i++)
    {
        if (strcmp(lexemes[i] + 1, "буква") == 0)
        {
            int j = i;

            while (strcmp(lexemes[j] + 1, "буква") == 0)
            {
                word[j] = lexemes[j][0];
                j++;
            }
            word[j] = '\0';

            resultWords[count] = malloc(strlen(word) * sizeof(char));
            resultWords[count + 1] = malloc(strlen("идентификатор") * sizeof(char));

            strcpy(resultWords[count], word);
            strcpy(resultWords[(count++) + 1], "идентификатор");

            i = j;
        }
        else if (strcmp(lexemes[i] + 1, "пробел"))
        {   

            resultWords[count] = malloc(2 * sizeof(char));
            resultWords[count + 1] = malloc(strlen("пробел") * sizeof(char));

            resultWords[count] = lexemes[i];
            strcpy(resultWords[(count++) + 1], lexemes[i + 1]);

            break;
        }
    }

    for (int i = 0; i < count; i++)
        printf("%s - %s", resultWords[i], resultWords[i+1]);
  
    return resultWords;
}

  /*    else if(strcmp(lexemes[i] + 1, "цифра"))
		{
		}
		else if(strcmp(lexemes[i] + 1, "пробел"))
		{
		}
		else if (strcmp(lexemes[i] + 1, "равно"))
		{
		}
		else if (strcmp(lexemes[i] + 1, "одинкавыч"))
		{
		}
		else if (strcmp(lexemes[i] + 1, "тире"))
		{
		}
		else if (strcmp(lexemes[i] + 1, "доллар"))
		{
		}*/