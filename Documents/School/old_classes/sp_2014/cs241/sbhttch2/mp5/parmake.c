/** @file parmake.c */
#include <unistd.h>
#include <getopt.h>
#include <stdlib.h>
#include <stdio.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include "rule.h"
#include "parser.h"


queue_t* rules;
queue_t* ready;
queue_t* targs;

pthread_mutex_t m1;
pthread_mutex_t m2;
pthread_cond_t c1;

int checkRule(char* rule) {
	int i = 0;
	char* tempRule;
	while (i < targs->size) {
		tempRule = queue_at(targs, i);
		if (!strcmp(rule, tempRule)) {
			return 1;
		}
		i++;
	}
	return 0;
}

int checkRuleReady(char* rule) {
	int i = 0;
	int flag = 0;
	rule_t* tempRule;
	pthread_mutex_lock(&m1);
	for (i;i < ready->size; i++) {
		tempRule = queue_at(ready, i);
		if (!strcmp(rule, tempRule->target)) {
			flag = 1;
			break;
		}
	}
	pthread_mutex_unlock(&m1);
	return flag;
}

void runRule(rule_t* rule) {
	int i = 0;
	int retVal = 0;
	char* curCommand;
	for(i; i < rule->commands->size; i++) {
		curCommand = queue_at(rule->commands, i);
		retVal = system(curCommand);
		if(retVal != 0) {
			exit(1);
		}
	}
}

int checkDepReady(rule_t* rule) {
	int i = 0;
	char* elem;
	if (rule->deps->size == 0) {
		return 1;
	}
	for (i; i < rule->deps->size; i++) {
		elem = queue_at(rule->deps, i);
		if(checkRule(elem)) {
			if(!checkRuleReady(elem)) {
				return 0;
			}
		}
	}
	return 1;
}

int allFiles(rule_t* rule) {
	char* elem;
	if (rule->deps->size == 0) {
		return 0;
	}
	else {
		int i = 0;
		for (i; i < rule->deps->size; i++) {
			elem = queue_at(rule->deps, i);
			if(checkRule(elem)) {
				return 0;
			}
		}
		return 1;
	}
}

rule_t* getRule() {
	int i = 0;
	rule_t* tempRule;
	for (i; i < rules->size; i++) {
		tempRule = queue_at(rules, i);
		if(tempRule->deps->size == 0) {
			break;
		}
		else if (checkDepReady(tempRule)) {
			break;
		}
	}
	if (i == rules->size) {
		return NULL;
	}
	else {
		return queue_remove_at(rules, i);
	}
}

double compTime(char* f1, char* f2) {
	struct stat s1;
	struct stat s2;

	stat(f1, &s1);
	stat(f2, &s2);

	return difftime(s1.st_mtime, s2.st_mtime);
}

int compare(char* c1, char* c2) {
	if (compTime(c1, c1) > 0) {
		return 1;
	}
	else {
		return 0;
	}
}

void* ruleRunner(void* rule) {
	int i = 0;
	int j = 1;
	rule_t* tempRule;

	while (j > 0) {
		pthread_mutex_lock(&m2);
		j = rules->size;
		tempRule = getRule();
		while (tempRule == NULL) {
			j = rules->size;
			if (j > 0) {
				pthread_cond_wait(&c1, &m2);
			}
			else {
				break;
			}
			tempRule = getRule();
		}
		pthread_mutex_unlock(&m2);
		if (j == 0) {
			break;
		}
		if(allFiles(tempRule)) {
			if (access(tempRule->target, F_OK) == -1) {
				runRule(tempRule);
			}
			else {
				for (i; i < tempRule->deps->size; i++) {
					if (compare(queue_at(tempRule->deps, i), tempRule->target)) {
						runRule(tempRule);
						break;
					}
				}
			}
		}
		else {
			runRule(tempRule);
		}
		pthread_mutex_lock(&m1);
		queue_enqueue(ready, tempRule);
		pthread_cond_broadcast(&c1);
		pthread_mutex_unlock(&m1);
	}
	return NULL;
}

void parsed_new_target(char* target) {
	rule_t* rule = malloc(sizeof(rule_t));
	rule_init(rule);
	char* temp;
	temp = malloc(sizeof(char) * (strlen(target) + 1));
	strcpy(temp, target);
	rule->target = temp;
	queue_enqueue(rules, rule);
	queue_enqueue(targs, temp);
}

void parsed_new_dependency(char* target, char* dependency){
	int i = 0;
	rule_t* tempRule;
	while (i < queue_size(rules)){
		tempRule = queue_at(rules, i);
		if (!strcmp(tempRule->target, target)) {
			break;
		}
		i++;
	}
	char* newDep = malloc(sizeof(char)*(strlen(dependency) + 1));
	strcpy(newDep, dependency);
	queue_enqueue(tempRule->deps, newDep);
}

void parsed_new_command(char* target, char* command) {
	int i = 0;
	rule_t* tempRule;
	while (i < queue_size(rules)){
		tempRule = queue_at(rules, i);
		if (!strcmp(tempRule->target, target)) {
			break;
		}
		i++;
	}
	char* newCom = malloc(sizeof(char)*(strlen(command) + 1));
	strcpy(newCom, command);
	queue_enqueue(tempRule->commands, newCom);
}




/**
 * Entry point to parmake.
 */
int main(int argc, char **argv)
{
	rules = malloc(sizeof(queue_t));
	ready = malloc(sizeof(queue_t));
	targs = malloc(sizeof(queue_t));
	queue_init(rules);
	queue_init(ready);
	pthread_mutex_init(&m1, NULL);
	pthread_mutex_init(&m2, NULL);
	pthread_cond_init(&c1, NULL);

	char** targets = malloc(sizeof(char*)*100);
	char* mfile = malloc(1024);
	int numthreads = 1;
	int opt;

	while ((opt = getopt(argc, argv, "f:j:")) != -1) {
		switch (opt) {
		case 'f':
			if (optarg != 0){
				strcpy(mfile, optarg);
			}
			else{
				if (access("makefile", F_OK) != -1){
					strcpy(mfile, "makefile");
				}
				else if (access("Makefile", F_OK) != -1){
					strcpy(mfile, "Makefile");
				}
				else
					return -1;
			}
			//printf("%s\n", mfile);
			break;
		case 'j':
			if (atoi(optarg) > 0) {
				numthreads = atoi(optarg);
			}
			//printf("%d\n", numthreads);
			break;
		default: /* '?' */
			fprintf(stderr, "Usage: %s [-f makefile] [-j threads] [targets]\n", argv[0]);
			return -1;
		}
	}
	int i = 0;
	int j = 0;
	if (optind >= argc) {
		targets[i] = NULL;
	}
	else{
		while (optind < argc) {
			targets[i] = argv[optind];
			i++;
			optind++;
		}
		targets[i] = NULL;
	}
	int len = i;

	parser_parse_makefile(mfile, targets, parsed_new_target, parsed_new_dependency, parsed_new_command);


	pthread_t* threads = malloc(sizeof(pthread_t)*numthreads);
	for (i = 0; i < numthreads; i++) {
		pthread_create(&threads[i], NULL, ruleRunner, NULL);
	}

	for (i = 0; i < numthreads; i++) {
		pthread_join(threads[i], NULL);
	}

	i = 0;
	j = 0;
	rule_t* tempRule;
	char* tempChar;

	while((tempRule = (rule_t*)queue_dequeue(rules)) != NULL) {
		while((tempChar = (char*)queue_dequeue(tempRule->deps)) != NULL) {
			free(tempChar);
		}
		while((tempChar = (char*)queue_dequeue(tempRule->commands)) != NULL) {
			free(tempChar);
		}
		free(tempRule->target);
		rule_destroy(tempRule);
		free(tempRule);
	}
	tempRule = NULL;
	while((tempRule = (rule_t*)queue_dequeue(ready)) != NULL) {
		while((tempChar = (char*)queue_dequeue(tempRule->deps)) != NULL) {
			free(tempChar);
		}
		while((tempChar = (char*)queue_dequeue(tempRule->commands)) != NULL) {
			free(tempChar);
		}
		free(tempRule->target);
		rule_destroy(tempRule);
		free(tempRule);;
	}
	for (i; i < len; i++){
		free(targets[i]);
	}
	queue_destroy(rules);
	queue_destroy(ready);
	free(rules);
	free(ready);
	free(targets);
	free(mfile);
	free(threads);
	return 0;
}
