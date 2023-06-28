#define _CRT_SECURE_NO_WARNINGS
#define MAX_WORD_LEN 100 // Максимальная длина строки

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* data_input(void)
{	
	FILE* fp = fopen("INPUT.txt", "r");

	if (fp != NULL)
	{
		int countWords = 0;
		char word[MAX_WORD_LEN];

		//Определение количества строк в файле
		while (fgets(word, MAX_WORD_LEN, fp) != NULL)
			countWords++;

		//Выделение памяти для массива указателей
		char** bufferWords = (char**)malloc(countWords * sizeof(char*));

		//Иницилизация каждого указателя на NULL для предотвращения хранения случайных значений
		for (int i = 0; i < countWords; i++)
			bufferWords[i] = NULL;

		//Перемещение каретки файла в начало
		fseek(fp, 0, SEEK_SET);

		for (int i = 0; i < countWords; i++)
		{
			fgets(word, MAX_WORD_LEN, fp);
			word[strlen(word) - 1] = '\0';

			bufferWords[i] = malloc(MAX_WORD_LEN * sizeof(char));
			strcpy(bufferWords[i], word);
		}
		fclose(fp);
		return bufferWords;
	}
	else
		return NULL;
}

void data_output(int result)
{	
	FILE* fp = fopen("OUTPUT.txt", "a+");

	if (result)
		fputs("ACCEPT\n", fp);
	else
		fputs("REJECT\n", fp);
	fclose(fp);
}
