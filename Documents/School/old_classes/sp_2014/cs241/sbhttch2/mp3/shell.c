/** @file shell.c */
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include "log.h"


log_t Log;

int countWhite(char* line){
	unsigned int i = 0;
	unsigned int c = 0;
	for(i = 0; i  < strlen(line); i++)
	{
		if(line[i] == ' ')
		{
			c++;
		}
	}
	return c + 1;
}

/**
 * Starting point for shell.
 */
int main(){
	int bytesRead = 0;
	size_t  bytes;
	char *buffer;
	size_t bufferSize;
	char *line = NULL;
	int currdir;
	unsigned int i;
	int flag = 1;
	
	log_init(&Log);
    while(1)
	{
		bufferSize = 200;
		buffer = (char*)malloc(bufferSize);
		printf("(pid=%d)%s$ ", getpid(), getcwd(buffer, bufferSize));
		free(buffer);
		bytesRead = getline(&line, &bytes, stdin);
		line[strlen(line)-1] = '\0'; 
		
		if (strcmp(line, "exit") == 0)
		{
			break;
		}
		if(bytesRead > 0)
		{
			flag = 1;
			while(flag)
			{
				if(line[0] == 'c' && line[1] == 'd')
				{
					printf("Command executed by pid=%d\n", getpid());
					log_push(&Log , line);
					currdir = chdir(&(line[3]));
					if(currdir != 0)
					{
						printf("%s: No such file or directory\n",&(line[3]));
					}
					flag = 0;
				}
				else if(strncmp(line, "!#", 2) == 0)
				{
					printf("Command executed by pid=%d\n", getpid());
					for(i=0; i < Log.size; i++)	
					{
						printf("%s\n", Log.stack[i]);
					}
					flag = 0;
				}
				else if(line[0] == '!' && line[1] != '#')
				{
					printf("Command executed by pid=%d\n", getpid());
					char* templine = log_search(&Log, &(line[1]));
					if(templine == NULL)
					{	
						flag = 0;
						printf("No Match\n");
					}
					else
					{
						printf("%s matches %s\n", &(line[1]), templine);
						line = realloc(line, strlen(templine)+1);
						memset(line, '\0', strlen(line));
						strcpy(line, templine);
					}
				}
				else
				{
					log_push(&Log,line);
					int child_status;
					pid_t pid = fork();
					if(pid == 0)				//Handle child process
					{
						char* templine2 = (char*)malloc(strlen(line)+1);
						strcpy(templine2, line);
						char** array = (char**)malloc(sizeof(char*)*(countWhite(line) + 1));
						i = 0;
						unsigned int j = 1;
						array[0] = templine2;
						
						while(templine2[i] != '\0')
						{
							if(templine2[i] == ' ')
							{
								templine2[i] = '\0';
								array[j] = templine2 + i + 1;
								j++;
							}
							i++;
						}
						array[countWhite(line)] = NULL;
						
						printf("Command executed by pid=%d\n", getpid());
						if(line[0] != '/')
						{
							if(execvp(array[0], &array[0]) == -1)
							{
							printf("%s: not found\n",line);
							}
						}
						else
						{
							if(execv(array[0], &array[0]) == -1)
							{
							printf("%s: not found\n",line);
							}
						}
						free(templine2);
						free(array);
						exit(0);
					}
					else
					{
						wait(&child_status);
						flag = 0;
					}
				}


				if(flag == 0)
				{
					free(line);
					line = NULL;
				}
			}
		}
	}
	free(line);
	log_destroy(&Log);
	return 0;
}
