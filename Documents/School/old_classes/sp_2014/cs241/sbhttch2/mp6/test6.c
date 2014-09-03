/* 
 * CS 241
 * The University of Illinois
 */

#define _GNU_SOURCE
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

#include "libmapreduce.h"

#define CHARS_PER_INPUT 30000
#define INPUTS_NEEDED 10

static const char *long_key = "long_key";

/* Takes input string and maps the longest
 * word to the key, long_key.
 */
void map(int fd, const char *data)
{
	char* tempWord = malloc(2000);
	char* maxWord = malloc(2000);
	unsigned int max = 0;
	char cur;
	char* d_string = strdup(data);
	int i = 0;
	int j = 0;
	tempWord[0] = d_string[0];
	cur = tempWord[0];
	while (cur != NULL) {
		while (isalpha(cur)) {
			j++;
			i++;
			tempWord[j] = d_string[i];
			cur = tempWord[j];
		}
		i++;
		cur = d_string[i];
		tempWord[j] = '\0';
		if(strlen(tempWord) > max) {
			strcpy(maxWord, tempWord);
			max = strlen(tempWord);
		}
		memset(tempWord, '\0', strlen(tempWord)+1);
		j = 0;
		tempWord[j] = cur;
	}
	
	char* filestr[1000];
	int length = sprintf(filestr, "%s: %s\n", long_key, maxWord);
	write(fd, filestr, length);
	close(fd);
	free(tempWord);
	free(maxWord);
}

/* Takes two words and reduces to the longer of the two
 */
const char *reduce(const char *value1, const char *value2)
{
	char* reduced = malloc(2000);
	if (strlen(value1) > strlen(value2)) {
		strcpy(reduced, value1);
	}
	else {
		strcpy(reduced, value2);
	}
	return reduced;
}


int main()
{
	FILE *file = fopen("alice.txt", "r");
	char s[1024];
	int i;

	char **values = malloc(INPUTS_NEEDED * sizeof(char *));
	int values_cur = 0;
	
	values[0] = malloc(CHARS_PER_INPUT + 1);
	values[0][0] = '\0';

	while (fgets(s, 1024, file) != NULL)
	{
		if (strlen(values[values_cur]) + strlen(s) < CHARS_PER_INPUT)
			strcat(values[values_cur], s);
		else
		{
			values_cur++;
			values[values_cur] = malloc(CHARS_PER_INPUT + 1);
			values[values_cur][0] = '\0';
			strcat(values[values_cur], s);
		}
	}

	values_cur++;
	values[values_cur] = NULL;
	
	fclose(file);

	mapreduce_t mr;
	mapreduce_init(&mr, map, reduce);

	mapreduce_map_all(&mr, (const char **)values);
	mapreduce_reduce_all(&mr);
	
	const char *result_longest = mapreduce_get_value(&mr, long_key);

	if (result_longest == NULL) { printf("MapReduce returned (null).  The longest word was not found.\n"); }
	else { printf("Longest Word: %s\n", result_longest); free((void *)result_longest); }

	mapreduce_destroy(&mr);

	for (i = 0; i < values_cur; i++)
		free(values[i]);
	free(values);


	return 0;
}
