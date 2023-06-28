#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "file_manager.h"
#include "transliteration.h"


int main()
{	
	system("chcp 1251");
	system("cls");

	char** data = data_input();

	if(data != NULL)
	{
		for (int i = 0; i < strlen(data); i++)
		{
			
			char** result = trl(data[i]);

			free(data[i]);
		}
	}
	else 
	{	
		printf("Ошибка чтения файла!\n");
		return 0;
	}

	free(data);
	return 0;
}
