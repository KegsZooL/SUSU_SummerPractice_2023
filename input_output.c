#define _CRT_SECURE_NO_WARNINGS
#define MAX_WORD_LEN 100 // ������������ ����� ������

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* data_input(void)
{	
	system("chcp 1251");
	system("cls");

	FILE* fp = fopen("INPUT.txt", "r");

	if (fp == NULL)
	{
		printf("������ ������ �����!\n");
		return 0;
	}
	else
	{
		int countWords = 0;
		char word[MAX_WORD_LEN];
	
		//����������� ���������� ����� � �����
		while (fgets(word, MAX_WORD_LEN, fp) != NULL)
			countWords++;

		//��������� ������ ��� ������� ����������
		char** bufferWords = (char**)malloc(countWords * sizeof(char*));

		//������������ ������� ��������� �� NULL ��� �������������� �������� ��������� ��������
		for (int i = 0; i < countWords; i++)
			bufferWords[i] = NULL;
		
		//����������� ������� ����� � ������
		fseek(fp, 0, SEEK_SET);

		for(int i = 0; i < countWords; i++)
		{
			fgets(word, MAX_WORD_LEN, fp);
			word[strlen(word) - 1] = '\0';

			bufferWords[i] = malloc(MAX_WORD_LEN * sizeof(char));
			strcpy(bufferWords[i], word);
		}
		fclose(fp);
		return bufferWords;
	}
}

void data_output(int result)
{	
	FILE* fp = fopen("OUTPUT.txt", "a+");
	if (fp == NULL)
		return 0;

	if (result)
		fputs("ACCEPT\n", fp);
	else
		fputs("REJECT\n", fp);

	fclose(fp);
}
