#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define MAX_ARG 64
#define MAX_CWD_LEN 256 



void simple_shell(){
	char *line = NULL;
	size_t size;

	while(1){
	  /*Print the prompt and the user-pid, read in user input*/	
	  printf("$(pid=%d): ", getpid());
	  fflush(stdout);
	  getline(&line, &size, stdin);

	  /*Replace \n with \0*/
	  line[strlen(line)-1] = '\0';

	  if (strcmp(line, "exit")==0) {
		break;
	  }
	  else if (strncmp(line, "cd ", 3) == 0) {
		/*chdir is a built in function*/
		chdir(line + 3);
	  }
	  else {
        	system(line);
	  }
	  free(line);
	  line = NULL;
	}
    /*free line on exit*/
    free(line);
}








void fork_chain(int n){
	pid_t childpid = 0;
        int i;
	for (i=1; i<n; i++) {
	   if((childpid = fork())){
		printf("My PID is: %d\n", getpid());
		break;
	   }else if(i==n-1){
		printf("My PID is: %d\n", getpid());
		sleep(10);
		exit(0);
	   }
    }
    
	waitpid(childpid, NULL, WUNTRACED);
}

void fork_fan(int n){
	pid_t childpid[n];
	int i;
	printf("PARENT PID: %d\n", getpid());
	for (i=1; i<n; i++) {
	   if( (childpid[i] = fork()) <= 0)
	   {
           printf("CHILD PID: %d, MY PARENT PID IS: %d\n", getpid(), getppid());
           sleep(10);
           exit(0);
	   }
    }	
    for(i=1; i<n; i++)
		waitpid(childpid[i], NULL, WUNTRACED);
}


int main()
{
	simple_shell();
	/*If time permits, show to the students how to create a fork chain*/
	//fork_chain(5);
	/*If time permits, show to the students how to create a fork fan*/
        //fork_fan(5);
	return 0;
}
