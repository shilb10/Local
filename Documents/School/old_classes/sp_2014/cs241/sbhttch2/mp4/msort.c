/** @file msort.c */
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct segs
{
	int* arr;
	int size;

} segs;

int compFunc(const void* a, const void* b)
{
	return (*(int *)a - *(int *)b);
}

void *merge(void* _segment)
{
	segs * segment = (segs *)_segment;
	segs * nextSeg = (segs *)(segment + 1);
	int* newArr = (int *)malloc((segment->size + nextSeg->size)*sizeof(int));
	int i = 0;
	int j = 0;
	int k = 0;
	int dups = 0;
	while(k < nextSeg->size + segment->size)
	{
		if( i < segment->size && j < nextSeg->size)
		{
			if(segment->arr[i] < nextSeg->arr[j])
			{
				newArr[k] = segment->arr[i];
				i++;
				k++;
			}
			else if(segment->arr[i] > nextSeg->arr[j])
			{
				newArr[k] = nextSeg->arr[j];
				j++;
				k++;
			}
			else
			{
				newArr[k] = segment->arr[i];
				i++;
				k++;
				dups++;
			}
		}
		else if(i < segment->size)
		{
			newArr[k] = segment->arr[i];
			i++;
			k++;
		}
		else if(j < nextSeg->size)
		{
			newArr[k] = nextSeg->arr[j];
			j++;
			k++;
		}
	}
	fprintf(stderr, "Merged %d and %d elements with %d duplicates.\n", segment->size, nextSeg->size, dups);
	free(segment->arr);
	free(nextSeg->arr);

	segment->arr = newArr;
	segment->size = i + j;
	return 0;
}

void *sort(void* segment)
{
	segs * sortSeg = (segs *)segment;
	if(sortSeg->size == 0)
	{
		return 0;
	}
	qsort(sortSeg->arr, sortSeg->size, sizeof(int), &compFunc);
	fprintf(stderr, "Sorted %d elements.\n", sortSeg->size);
	return 0;
}

int main(int argc, char **argv)
{
	int segment_count = 1;
	if(argv[1] != NULL)
	{
		segment_count = atoi(argv[1]);
	}
	pthread_t *threads = malloc(sizeof(pthread_t)*segment_count);
	int buffSize = 1024;
	char* buffStr = (char*)malloc(buffSize);
	char* curline;

	int* list = (int*)malloc(10*sizeof(int));
	int listLength = 10;
	int i = 0;

	while(fgets(buffStr, buffSize, stdin))
	{
		curline = buffStr;
		curline[strlen(curline)-1] = 0;
		list[i] = atoi(curline);
		i++;
		if(listLength <= i)
		{
			list = realloc(list, 2*listLength*sizeof(int));
			listLength = 2*listLength;
		}
	}

	int values_per_segment;

	if(segment_count > 0)
	{
		if (i % segment_count == 0)
			values_per_segment = i / segment_count;
		else
			values_per_segment = (i / segment_count) + 1;
	}
	else
		values_per_segment = i;

	segs* segments = (segs*)malloc(segment_count*sizeof(segs));
	int j = 0;
	for(; j < segment_count; j++)
	{
		segments[j].arr =(int*)malloc(values_per_segment * sizeof(int));
	}
	j = 0;
	int k = 0;
	while(j < segment_count)
	{
		while(k < values_per_segment && (values_per_segment*j + k) < i)
		{
			segments[j].arr[k] = *(list + values_per_segment*j + k);
			k++;
		}
		segments[j].size = k;
		k = 0;
		j++;
	}
	j = 0;
	int res;
	for(; j < segment_count; j++)
	{
		res = pthread_create(&threads[j],NULL, sort, (void *)&segments[j]);
	}
	j = 0;
	for(; j < segment_count; j++)
	{
		res = pthread_join(threads[j],NULL);
	}

	//Handle the merge.
	//int nextSegSizes = segment_count/2 + (segment_count % 2);
	int numSegs = segment_count;
	int numThreads = segment_count;
	int merges = 0;
	// threads = realloc(threads, numThreads*sizeof(pthread_t));
	// segs* nextSegs = malloc(nextSegSizes*sizeof(segs));
	// j = 0;
	// for(; j < segment_count/2; j++)
	// {
	// 	nextSegs[j].arr = segments[2*j].arr;
	// 	nextSegs[j].size = segments[2*j].size;
	// }
	// if(j < numSegs)
	// {
	// 	nextSegs[j].arr = segments[segment_count - 1].arr;
	// 	nextSegs[j].size = segments[segment_count - 1].size;
	// }
	for(; merges < (segment_count/2 + (segment_count % 2)); merges++)
	{
		numThreads = numSegs/2;
		j=0;
		for(; j < numThreads; j++)
		{
			res = pthread_create(&threads[j], NULL, merge, (void *)&segments[2*j]);
		}

		j=0;
		for(; j < numThreads; j++)
		{
			res = pthread_join(threads[j],NULL);
		}
		j=0;
		for(; j < numThreads; j++)
		{
			segments[j].arr = segments[2*j].arr;
			segments[j].size = segments[2*j].size;
		}
		if((numSegs % 2) == 1)
		{
			segments[j].arr = segments[numSegs-1].arr;
			segments[j].size = segments[numSegs - 1].size;
		}
		numSegs = (numSegs/2 + (numSegs % 2));
	}
	//merge(segments);
	j=0;
	for(; j < i; j++)
	{
		printf("%d\n",segments[0].arr[j]);
	}

//free everything
	j = 0;
	// for(; j < segment_count; j++)
	// {
	// 	free(segments[j].arr);
	// }
	free(segments->arr);
	free(threads);
	free(segments);
	free(list);
	free(buffStr);




	// segs* seg1 = malloc(2*sizeof(segs));
	// seg1[0].arr = malloc(10*sizeof(int));
	// seg1[0].size = 10;
	// seg1[1].arr = malloc(10*sizeof(int));
	// seg1[1].size = 10;
	// int i = 0;
	// for(; i < 10; i++)
	// {
	// 	seg1[0].arr[i] = 2*i;
	// 	seg1[1].arr[i] = 3*i - 2;
	// }
	// merge((void *)seg1);
	// i = 0;
	// for(; i < 20; i++)
	// {
	// 	printf("%d\n", seg1[0].arr[i]);
	// }
	// i = 0;
	// for(; i < 2; i++)
	// {
	// 	free(seg1[i].arr);
	// }
	// free(seg1);
	return 0;
}
