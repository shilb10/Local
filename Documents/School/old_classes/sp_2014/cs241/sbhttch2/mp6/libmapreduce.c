/** @file libmapreduce.c */
/* 
 * CS 241
 * The University of Illinois
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/select.h>
#include <pthread.h>
#include <string.h>
#include <assert.h>
#include <unistd.h>
#include <sys/wait.h>
#include <poll.h>
#include <sys/epoll.h>

#include "libmapreduce.h"
#include "libds/libds.h"


static const int BUFFER_SIZE = 2048;  /**< Size of the buffer used by read_from_fd(). */

int num;
int** pipefds;
pthread_t thread;
char** buffer; 
/**
 * Adds the key-value pair to the mapreduce data structure.  This may
 * require a reduce() operation.
 *
 * @param key
 *    The key of the key-value pair.  The key has been malloc()'d by
 *    read_from_fd() and must be free()'d by you at some point.
 * @param value
 *    The value of the key-value pair.  The value has been malloc()'d
 *    by read_from_fd() and must be free()'d by you at some point.
 * @param mr
 *    The pass-through mapreduce data structure (from read_from_fd()).
 */
static void process_key_value(const char *key, const char *value, mapreduce_t *mr)
{
	const char* val = datastore_get(mr->ds, key, &(mr->rev));
	if(val != NULL) {
		char* temp = (char*)mr->reduce(val, value);
		mr->rev = datastore_update(mr->ds, key, temp, mr->rev);
		free((char*)temp);
	}
	else {
		mr->rev = datastore_put(mr->ds, key, value);
	}
	free((char*)key);
	free((char*)value);
	free((char*)val);
}


/**
 * Helper function.  Reads up to BUFFER_SIZE from a file descriptor into a
 * buffer and calls process_key_value() when for each and every key-value
 * pair that is read from the file descriptor.
 *
 * Each key-value must be in a "Key: Value" format, identical to MP1, and
 * each pair must be terminated by a newline ('\n').
 *
 * Each unique file descriptor must have a unique buffer and the buffer
 * must be of size (BUFFER_SIZE + 1).  Therefore, if you have two
 * unique file descriptors, you must have two buffers that each have
 * been malloc()'d to size (BUFFER_SIZE + 1).
 *
 * Note that read_from_fd() makes a read() call and will block if the
 * fd does not have data ready to be read.  This function is complete
 * and does not need to be modified as part of this MP.
 *
 * @param fd
 *    File descriptor to read from.
 * @param buffer
 *    A unique buffer associated with the fd.  This buffer may have
 *    a partial key-value pair between calls to read_from_fd() and
 *    must not be modified outside the context of read_from_fd().
 * @param mr
 *    Pass-through mapreduce_t structure (to process_key_value()).
 *
 * @retval 1
 *    Data was available and was read successfully.
 * @retval 0
 *    The file descriptor fd has been closed, no more data to read.
 * @retval -1
 *    The call to read() produced an error.
 */
static int read_from_fd(int fd, char *buffer, mapreduce_t *mr)
{
	/* Find the end of the string. */
	int offset = strlen(buffer);

	/* Read bytes from the underlying stream. */
	int bytes_read = read(fd, buffer + offset, BUFFER_SIZE - offset);
	if (bytes_read == 0)
		return 0;
	else if(bytes_read < 0)
	{
		fprintf(stderr, "error in read.\n");
		return -1;
	}

	buffer[offset + bytes_read] = '\0';

	/* Loop through each "key: value\n" line from the fd. */
	char *line;
	while ((line = strstr(buffer, "\n")) != NULL)
	{
		*line = '\0';

		/* Find the key/value split. */
		char *split = strstr(buffer, ": ");
		if (split == NULL)
			continue;

		/* Allocate and assign memory */
		char *key = malloc((split - buffer + 1) * sizeof(char));
		char *value = malloc((strlen(split) - 2 + 1) * sizeof(char));

		strncpy(key, buffer, split - buffer);
		key[split - buffer] = '\0';

		strcpy(value, split + 2);

		/* Process the key/value. */
		process_key_value(key, value, mr);

		/* Shift the contents of the buffer to remove the space used by the processed line. */
		memmove(buffer, line + 1, BUFFER_SIZE - ((line + 1) - buffer));
		buffer[BUFFER_SIZE - ((line + 1) - buffer)] = '\0';
	}

	return 1;
}


/**
 * Initialize the mapreduce data structure, given a map and a reduce
 * function pointer.
 */
void mapreduce_init(mapreduce_t *mr, 
                    void (*mymap)(int, const char *), 
                    const char *(*myreduce)(const char *, const char *))
{
	mr->map = mymap;
	mr->reduce = myreduce;
	datastore_t* ds = malloc(sizeof(datastore_t));
	mr->ds = ds;
	datastore_init(mr->ds);	
}

void* thread_poll(void* temp) {
	mapreduce_t* mr = (mapreduce_t*) temp;
	int i = 0;
	while (i < num) {	
		struct epoll_event event;
		memset(&event, 0, sizeof(struct epoll_event));
		epoll_wait(mr->epoll_fd, &event, 1, -1);
		int j = 0;
		for (j; j < num; j++) {
			if(event.data.fd == pipefds[j][0]) {
				if(!read_from_fd(event.data.fd, buffer[j], mr)) {
					i++;
					epoll_ctl(mr->epoll_fd, EPOLL_CTL_DEL, event.data.fd, &event);
				}
				break;	
			}
		} 
	}
	return NULL;
}

/**
 * Starts the map() processes for each value in the values array.
 * (See the MP description for full details.)
 */
void mapreduce_map_all(mapreduce_t *mr, const char **values)
{
	num = 0;
	while (values[num] != NULL) {
		num++;
	}
	pipefds = malloc(num*sizeof(int*));
	int i = 0;
	for (i; i < num; i++) {
		pipefds[i] = malloc(2*sizeof(int));
		pipe(pipefds[i]);
	}
	int epoll_fd = epoll_create(num);
	mr->epoll_fd = epoll_fd;
	struct epoll_event event[num];
	memset(event, 0, sizeof(struct epoll_event)*num);
	i = 0;
	for (i; i < num; i++) {
		if (!fork()) {
			int j = 0;
			for (j; j < num; j++) {
				close(pipefds[i][0]);
			}
			mr->map(pipefds[i][1], values[i]);
			exit(0);
		}
		else {
			close(pipefds[i][1]);
		}
		event[i].events = EPOLLIN;
		event[i].data.fd = pipefds[i][0];
		epoll_ctl(epoll_fd, EPOLL_CTL_ADD, pipefds[i][0], &event[i]);
	}
	buffer = malloc(sizeof(char*)*num);
	i = 0;
	for (i; i < num; i++) {
		buffer[i] = malloc(BUFFER_SIZE + 1);
		buffer[i][0] = '\0';
	}
	pthread_create(&thread, NULL, thread_poll, (void*)mr);
}




/**
 * Blocks until all the reduce() operations have been completed.
 * (See the MP description for full details.)
 */
void mapreduce_reduce_all(mapreduce_t *mr)
{
	pthread_join(thread, NULL);
}


/**
 * Gets the current value for a key.
 * (See the MP description for full details.)
 */
const char *mapreduce_get_value(mapreduce_t *mr, const char *result_key)
{
	return datastore_get(mr->ds, result_key, NULL);
}


/**
 * Destroys the mapreduce data structure.
 */
void mapreduce_destroy(mapreduce_t *mr)
{
	int i = 0;
	while(i < num) {
		free(buffer[i]);
		free(pipefds[i]);
		i++;
	}
	free(pipefds);
	free(buffer);
	datastore_destroy(mr->ds);
	free(mr->ds);
}
