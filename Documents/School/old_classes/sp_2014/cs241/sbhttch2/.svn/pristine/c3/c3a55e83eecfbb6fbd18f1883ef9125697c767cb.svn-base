/** @file server.c */

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <pthread.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <signal.h>
#include <queue.h>
#include <assert.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/socket.h>

#include "queue.h"
#include "libhttp.h"
#include "libdictionary.h"

queue_t* connecs;
queue_t* threads;
int quit;
int socket_fd;

const char *HTTP_404_CONTENT = "<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1>The requested resource could not be found but may be available again in the future.<div style=\"color: #eeeeee; font-size: 8pt;\">Actually, it probably won't ever be available unless this is showing up because of a bug in your program. :(</div></html>";
const char *HTTP_501_CONTENT = "<html><head><title>501 Not Implemented</title></head><body><h1>501 Not Implemented</h1>The server either does not recognise the request method, or it lacks the ability to fulfill the request.</body></html>";

const char *HTTP_200_STRING = "OK";
const char *HTTP_404_STRING = "Not Found";
const char *HTTP_501_STRING = "Not Implemented";

/**
 * Processes the request line of the HTTP header.
 * 
 * @param request The request line of the HTTP header.  This should be
 *                the first line of an HTTP request header and must
 *                NOT include the HTTP line terminator ("\r\n").
 *
 * @return The filename of the requested document or NULL if the
 *         request is not supported by the server.  If a filename
 *         is returned, the string must be free'd by a call to free().
 */
char* process_http_header_request(const char *request)
{
	// Ensure our request type is correct...
	if (strncmp(request, "GET ", 4) != 0)
		return NULL;

	// Ensure the function was called properly...
	assert( strstr(request, "\r") == NULL );
	assert( strstr(request, "\n") == NULL );

	// Find the length, minus "GET "(4) and " HTTP/1.1"(9)...
	int len = strlen(request) - 4 - 9;

	// Copy the filename portion to our new string...
	char *filename = malloc(len + 1);
	strncpy(filename, request + 4, len);
	filename[len] = '\0';

	// Prevent a directory attack...
	//  (You don't want someone to go to http://server:1234/../server.c to view your source code.)
	if (strstr(filename, ".."))
	{
		free(filename);
		return NULL;
	}

	return filename;
}

void close_server() {
	int* cur_sock = NULL;
	pthread_t* cur_thread = NULL;
	close(socket_fd);

	cur_sock = queue_dequeue(connecs);
	while (cur_sock != NULL) {
		if (*cur_sock != -1) {
			shutdown(*cur_sock, SHUT_RDWR);
		}
		free(cur_sock);
		cur_sock = queue_dequeue(connecs);
	}
	free(connecs);

	cur_thread = queue_dequeue(threads);
	while (cur_thread != NULL) {
		pthread_join(*cur_thread, NULL);
		free(cur_thread);
		cur_thread = queue_dequeue(threads);
	}
	free(threads);
	quit = 1;
	exit(0);
}

void append_type(char* response, char* path) {
	const char* end = strrchr(path, '.');
	if (!strcmp(end, ".html")) {
		strcat(response, "Content-Type: text/html\r\n");
	}
	else if (!strcmp(end, ".css")) {
		strcat(response, "Content-Type: text/css\r\n");
	}
	else if (!strcmp(end, ".jpg")) {
		strcat(response, "Content-Type: image/jpeg\r\n");
	}
	else if (!strcmp(end, ".png")) {
		strcat(response, "Content-Type: image/png\r\n");
	}
	else {
		strcat(response, "Content-Type: text/plain\r\n");
	}
}

int append_connec(http_t* http, char* response) {
	if(!strcasecmp("Keep-Alive", http_get_header(http, "Connection"))) {
			strcat(response, "Connection: Keep-Alive\r\n\r\n");
			return 1;
	}
	else {
			strcat(response, "Connection: close\r\n\r\n");
			return 0;
	}	
}

void make_response(char* response, char* response_content_length, int status) {
	int len = 0;
	switch(status) {
		case 501:
			sprintf(response, "HTTP/1.1 %d %s\r\n", 501, "Not Implemented");
			strcat(response, "Content-Type: text/html\r\n");
			len = (int)strlen((char*)HTTP_501_CONTENT);
			sprintf(response_content_length, "Content-Length: %d\r\n", len);
			strcat(response, response_content_length);
			break;
		case 404:
			sprintf(response, "HTTP/1.1 %d %s\r\n", 404, "Not Found");
			strcat(response, "Content-Type: text/html\r\n");
			len = (int)strlen((char*)HTTP_404_CONTENT);
			sprintf(response_content_length, "Content-Length: %d\r\n", len);
			strcat(response, response_content_length);
			break;
		default:
			break;
	}
}

void* proc_req(void* temp) {
	int sock = *((int*)temp);

	while (!quit) {
		http_t *http = malloc(sizeof(http_t));
		if (http_read(http, sock) <= 0) {
			http_free(http);
			free(http);
			break;
		}

		char* filename = process_http_header_request(http_get_status(http));
		char* response = malloc(2048);
		char* response_content_length = malloc(2048);
		char* path = calloc(2048, sizeof(char));
		char* body = malloc(2048);
		size_t body_length;
		int keep_alive = 1;
		int status; 

		if (filename == NULL) {
			make_response(response, response_content_length, 501);
			keep_alive = append_connec(http, response);
			status = 501;
		}
		else {
			strcat(path, "web/");
			if (!strcmp(filename, "/")) {
				strcat(path, "index.html");
			}
			else {
				strcat(path, filename);
			}

			FILE* f_ptr = fopen(path, "r");
			if (f_ptr == NULL) {
				make_response(response, response_content_length, 404);
				keep_alive = append_connec(http, response);
				status = 404;
			}
			else {
				struct stat f;
				stat(path, &f);
				body_length = (int)f.st_size;
				body = realloc(body, body_length);
				body = memset(body, 0, body_length);
				fread(body, body_length, 1, f_ptr);
				sprintf(response, "HTTP/1.1 %d %s\r\n", 200, "OK");
				append_type(response, path);
				sprintf(response_content_length, "Content-Length: %d\r\n", (int)body_length);
				strcat(response, response_content_length);
				keep_alive = append_connec(http, response);
				status = 200;
				fclose(f_ptr);
			}
		}

		send(sock, (const void*)response, strlen(response), 0);
		switch(status){
			case 501:
				send(sock, (const void*)HTTP_501_CONTENT, strlen(HTTP_501_CONTENT),0);
				break;
			case 404:
				send(sock, (const void*)HTTP_404_CONTENT, strlen(HTTP_404_CONTENT),0);
				break;
			case 200:
				send(sock, (const void*)body, body_length, 0);
		}

		free(response);
		free(response_content_length);
		free(path);
		free(body);
		free(filename);
		http_free(http);
		free(http);
		if (!keep_alive) {
			break;
		}
	}
	return NULL;
}

// void* get_in_addr(struct sockaddr *sa) {
// 	if (sa->sa_family == AF_INET) {
// 		return &(((struct sockaddr_in*)sa)->sin_addr);
// 	}

// 	return &(((struct sockaddr_in6*)sa)->sin6_addr);
// }

int main(int argc, char **argv)
{
	signal(SIGPIPE, SIG_IGN);
	char* port = argv[1];
	
	int r;
	int flag = 1;
	struct addrinfo hints, *s_info, *p;
	struct sockaddr_storage in_addr;
	socklen_t sin_size;

	connecs = malloc(sizeof(queue_t));
	queue_init(connecs);
	threads = malloc(sizeof(queue_t));
	queue_init(threads);
	quit = 0;

	memset(&hints, 0, sizeof(struct addrinfo));
	hints.ai_family = AF_UNSPEC;
	hints.ai_socktype = SOCK_STREAM;
	hints.ai_flags = AI_PASSIVE;

	r = getaddrinfo(NULL, port, &hints, &s_info);
	if (r != 0) {
		fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(r));
		exit(1);
	}

	for (p = s_info; p != NULL; p = p->ai_next) {
		if ((socket_fd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
			perror("server: sock");
			continue;
		}

		if (setsockopt(socket_fd, SOL_SOCKET, SO_REUSEADDR, &flag, sizeof(int)) == -1) {
			perror("setsockopt");
			exit(1);
		}

		if (bind(socket_fd, p->ai_addr, p->ai_addrlen) == -1) {
		close(socket_fd);
		perror("bind()");
		continue;
		}

		break;
	}

	freeaddrinfo(s_info);

	if (listen(socket_fd, 10) != 0) {
		perror("listen()");
		exit(1);
	}

	signal(SIGINT, close_server);

	while (!quit) {
		sin_size = sizeof(in_addr);
		int* conn = malloc(sizeof(int));
		*conn = 0;
		queue_enqueue(connecs, conn);

		if ((*conn = accept(socket_fd, (struct sockaddr *)&in_addr, &sin_size)) >= 0) {
			pthread_t* thread = malloc(sizeof(pthread_t));
			queue_enqueue(threads, thread);
			pthread_create(thread, NULL, proc_req, (void*)conn);
		}
	}

	return 0;
}
