#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <semaphore.h>
#include <pthread.h>


/**
 * @define BUFFER_SIZE
 * @brief Size in bytes of the shared buffer
 *
 * This holds the size of the circular buffer shared between producer
 * and consumer
 */
#define BUFFER_SIZE 400

/**
 * @brief Thread specific informations for consumer and producer threads
 *
 * This structure is used to instruct the thread about where is the
 * shared buffer and the semaphore to use.
 */
typedef struct {
	/**
	 * @var buf
	 * @brief The shared buffer
	 *
	 * Producers will fill locations in this buffer, while
	 * consumers will read and print the bytes in the buffer.
	 */
	char * buf;

	/**
	 * @var buf_size
	 * @brief holds the size of the shared ring buffer
	 *
	 * This variable stores the size of the shared ring buffer
	 */
	int buf_size;

	/**
	 * @var open_sem
	 * @brief This semaphore holds the number of free locations
	 *
	 * This semaphore is used by the producer to produce a new
	 * byte in the shared buffer. It will be used by the consumer
	 * to notify that a byte has been consumed from the buffer.
	 */
	sem_t * open_sem;

	/**
	 * @var ready_sem
	 * @brief This semaphore holds the number of ready locations
	 *
	 * This semaphore is used by the producer to notify that a new
	 * byte in the shared buffer has been produced. It will be
	 * used by the consumer to understand that a byte can be
	 * consumed from the buffer.
	 */
	sem_t * ready_sem;
	
} arg_t;

/**
 * @brief Producer routine
 *
 * This is the routine for the producer. It produces one byte at a
 * time and puts it in the shared buffer.
 */
void * producer_thread(void * arg)
{
	/* This thread will perform a loop producing on the buffer
	 * if an available position   */
	int pos = 0;
	char line [] = "Product cs241 is giving out free Pebble smart watches!\n";
	int line_pos = 0;
	int line_len = strlen(line);
	arg_t * args = (arg_t *)arg;

	/* Producer loop */
	while(1){
		/* Wait for an open position */
		sem_wait(args->open_sem);
		/* Produce a character */
		args->buf[pos] = line[line_pos];
		/* Notify that a new position is available */
		sem_post(args->ready_sem);

		/* Update the position in the line */
		line_pos = (line_pos + 1) % line_len;
		/* Update the position in the buffer*/
		pos = (pos + 1) % args->buf_size;
		
		/* Sleep some time */
		sleep(1);
	}
	
	return NULL;
}

/**
 * @brief Consumerer routine
 *
 * This is the routine for the consumer. It consumes one byte at a
 * time from the shared buffer.
 */
void * consumer_thread(void * arg)
{
	/* This thread will perform a loop consuming from the buffer
	 * if a byte is available */
	int pos = 0;
	char read;
	arg_t * args = (arg_t *)arg;

	/* Consumer loop */
	while(1){
		/* Wait for a ready byte */
		sem_wait(args->ready_sem);
		/* Consume a character */
		read = args->buf[pos];
		/* Notify that a position has been consumed */
		sem_post(args->open_sem);

		/* Update the position in the buffer */
		pos = (pos + 1) % args->buf_size;
		/* Print the read character */
		printf("%c", read);
		fflush(stdout);
		
		/* Sleep some time */
		sleep(1);
	}
	
	return NULL;
}

/**
 * @brief Main routine
 *
 * The main will have to:
 * 1. Parse the parameters
 * 2. Initialize the semaphore
 * 3. Initialize the shared buffer
 * 4. Span producers and consumers
 * 
 * @param argc number of parameters
 * @param args command line parameters
 * @returns 0 on sucess, 1 on error
 */
int main( int argc, char ** args )
{
	
	/* Variable definition */
	char * buf = (char *)malloc(BUFFER_SIZE);
	arg_t * prod_args = (arg_t *)malloc(sizeof(arg_t));
	arg_t * cons_args = (arg_t *)malloc(sizeof(arg_t));
	sem_t open_sem;
	sem_t ready_sem;
	pthread_t producer, consumer;
	void * thexit;

	/* Initialize semaphores */
	sem_init(&open_sem, 0, 1);
	sem_init(&ready_sem, 0, 0);

	/* Initialize thread arguments */
	prod_args->buf = cons_args->buf = buf;
	prod_args->buf_size = cons_args->buf_size = BUFFER_SIZE;
	prod_args->open_sem = cons_args->open_sem = &open_sem;
	prod_args->ready_sem = cons_args->ready_sem = &ready_sem;
	
	/* Span threads */
	pthread_create(&producer, NULL, producer_thread, (void *)prod_args);
	pthread_create(&consumer, NULL, consumer_thread, (void *)cons_args);

	/* Wait for thread termination */
	pthread_join(producer, &thexit);
	pthread_join(consumer, &thexit);

	/* Return success */
	return 0;
	
}
