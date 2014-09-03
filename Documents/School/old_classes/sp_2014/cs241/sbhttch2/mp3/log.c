/** @file log.c */
#include <stdlib.h>
#include <string.h>
#include "log.h"

/**
 * Initializes the log.
 *
 * You may assuem that:
 * - This function will only be called once per instance of log_t.
 * - This function will be the first function called per instance of log_t.
 * - All pointers will be valid, non-NULL pointer.
 *
 * @returns
 *   The initialized log structure.
 */
void log_init(log_t *l) {
	l->stack = (char**)malloc(300*(sizeof(char*)));
	l->size = 0;
}

/**
 * Frees all internal memory associated with the log.
 *
 * You may assume that:
 * - This function will be called once per instance of log_t.
 * - This funciton will be the last function called per instance of log_t.
 * - All pointers will be valid, non-NULL pointer.
 *
 * @param l
 *    Pointer to the log data structure to be destoryed.
 */
void log_destroy(log_t* l) {
	unsigned int i = 0;
	for(; i < l->size; i++)
	{
		free(l->stack[i]);
	}
	free(l->stack);
	//free(l);
}

/**
 * Push an item to the log stack.
 *
 *
 * You may assume that:
* - All pointers will be valid, non-NULL pointer.
*
 * @param l
 *    Pointer to the log data structure.
 * @param item
 *    Pointer to a string to be added to the log.
 */
void log_push(log_t* l, const char *item) {
	if(l->size > sizeof(l->stack)/sizeof(char*))
	{
		char** tempStack = (char**)malloc(2*(l->size)*sizeof(char*));
		unsigned int i = 0;
		for(; i < l->size; i++)
		{
			tempStack[i] = l->stack[i];
		}
		free(l->stack);
		l->stack = tempStack;
	}
	char* tempstring = (char*)malloc(strlen(item) + 1);
	memset(tempstring, '\0', strlen(item));
	strcpy(tempstring, item);			
	(l->stack)[l->size] = tempstring;
	(l->size)++;
}

/**
 * Preforms a newest-to-oldest search of log entries for an entry matching a
 * given prefix.
 *
 * This search starts with the most recent entry in the log and
 * compares each entry to determine if the query is a prefix of the log entry.
 * Upon reaching a match, a pointer to that element is returned.  If no match
 * is found, a NULL pointer is returned.
 *
 *
 * You may assume that:
 * - All pointers will be valid, non-NULL pointer.
 *
 * @param l
 *    Pointer to the log data structure.
 * @param prefix
 *    The prefix to test each entry in the log for a match.
 *
 * @returns
 *    The newest entry in the log whose string matches the specified prefix.
 *    If no strings has the specified prefix, NULL is returned.
 */
char *log_search(log_t* l, const char *prefix) {
    int flag = 0;
	int i = l->size - 1;			
	for(; i >=0; i--)
	{
		if(strncmp(l->stack[i], prefix, strlen(prefix)) != 0)
		{
			flag = 1;
		}
		
		if(flag == 0)
		{
			return l->stack[i];
		}
		
		flag = 0;
	}
	return NULL;
}
