/** @file part1.c */

/*
 * Machine Problem #0
 * CS 241 Fall2013
 */

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#include "part2-functions.h"

/**
 * (Edit this function to print out the ten "Illinois" lines in part2-functions.c in order.)
 */
int main()
{
	first_step(81);
	
	int* sec;
	int x = 132;
	sec = &x;
	second_step(sec);

	int** third;
	x = 8942;
	sec = &x;
	third = &sec;
	double_step(third);	

	sec =(int *) 0;
	strange_step(sec);
	
	char arr[4] = {0,0,0,0};
	empty_step(arr);
	
	char twos[4] = {'u','u','u','u'};
	two_step(twos,twos);

	three_step(twos, twos+2, twos+4);

	char f8[2] = {0,0};
	char s8[3] = {0,0,f8[1]+8};
	char t8[4] = {0,0,0,s8[2]+8};
	step_step_step(f8,s8,t8);
	
	x = 2;
	char* var9;
	var9 = (char*)&x;
	it_may_be_odd(var9,x);
	
	char b[4] = {1,0x11,0,0};
	void* o = b;
	the_end(o,b);

	
	
	return 0;
}
