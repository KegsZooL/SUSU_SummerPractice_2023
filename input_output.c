#define _CRT_SECURE_NO_WARNINGS
#define MAX_WORD_LEN 100 // Максимальная длина строки

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//Функция считывает символы из потока и возвращает буфер, содержащий исходную строку из файла.
char* data_input(void)
{	
	FILE* fp = fopen("INPUT.txt", "r");

	if (fp != NULL)
	{
		char* word = malloc(MAX_WORD_LEN * sizeof(char));

		fgets(word, MAX_WORD_LEN, fp);
		word[strlen(word) - 1] = '\0';

		fclose(fp);
		return word;
	}
	else
		return NULL;
}

//Функциия принимает result, в зависимости от которой в файл output.txt выводится ACCEPT или REJECT.
void data_output(int result)
{	
	FILE* fp = fopen("OUTPUT.txt", "a+");

	if (result)
		fputs("ACCEPT\n", fp);
	else
		fputs("REJECT\n", fp);
	fclose(fp);
}
