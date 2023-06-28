#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include "file_manager.h"

int main()
{
	char** test = data_input();

	for (int i = 0; i < strlen(test); i++)
	{
		if (strcmp(test[i], "true") == 0)
			data_output(1);
		else
			data_output(0);
		free(test[i]);
	}

	free(test);
	return 0;
}