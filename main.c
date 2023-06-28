#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "file_manager.h"

int main()
{	
	system("chcp 1251");
	system("cls");
		
	char** data = data_input();

	if(data != NULL)
	{
		for (int i = 0; i < strlen(data); i++)
		{
			if (strcmp(data[i], "true") == 0)
				data_output(1);
			else
				data_output(0);
			printf("%s ", data[i]);
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
