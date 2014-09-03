#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Calculates a value (c) based on the input parameters (a, b) and prints
 * out the result.
 *
 * @param a
 *     Input parameter a.
 *
 * @param b
 *     Input parameter b.
 */
void one(const int a, const int b)
{
	int c = (a * a) + (b * b);

	printf("%d^2 + %d^2 = %d\n",a,b,c);
}


/**
 * Checks if the input parameter is a passing grade and prints out if
 * the grade is passing.
 *
 * @param grade
 *     The grade to check.
 */
void two(const int grade)
{
	if (grade > 70)
	{
		printf("You passed!\n");
	}
}


/**
 * Assigns a pointer (int *p) the value of a stack variable (int x).
 */
void three()
{
	int x = 4;
	int *p = &x;

	printf("The value of p is: %d\n", *p);
}


/**
 * Prints out a specific message based on if the number is
 * between 0 and 1 (exclusive).
 *
 * @param value
 *     Value to test.
 */
void four(const float value)
{
	if (0 < value && value < 1)
	{
		printf("The value is between zero and one.\n");
	}
	else
	{
		printf("The value is not between zero and one.\n");
	}
}


/**
 * Prints out a specific message based on if the two input parameters
 * are equal.
 *
 * @param x
 *     First input parameter.
 *
 * @param y
 *     Second input parameter.
 */
void five(const int x, const int y)
{
	if (x == y)
	{
		printf("x and y are equal.\n");
	}
	else
	{
		printf("x and y are different.\n");
	}
}


/**
 * Returns a new pointer (float *p) which contains the value of the
 * input pointer (int *x).
 *
 * @param x
 *     Input parameter, whose value will be returned as a (float *).
 *
 * @returns
 *     A new pointer, allocated on the heap and not freed, that
 *     contains the value of the input parameter.
 */
float * six(const int *x)
{
	float *p = (float *) malloc(sizeof(float));
	*p = (float) *x;
	return p;
}


/**
 * Takes two inputs, a and b such that (a < b), and makes a and b equal
 * via a while-loop.  Prints out their value before returning.
 * 
 * @param a
 *     Input parameter a, where a < b.
 *
 * @param b
 *     Input parameter b, where b > a.
 */
void seven(int a, const int b)
{
	while (a != b)
	{
		a++;
	}

	printf("%d is now equal to %d\n", a, b);
}


/**
 * Constructs a C-string, character by character, and prints out the full
 * string "Hello".
 */
void eight()
{
	char *s = (char *)malloc(6);

	s[0] = 'H';
	s[1] = 'e';
	s[2] = 'l';
	s[3] = 'l';
	s[4] = 'o';
	s[5] = '\0';
	printf("%s\n", s);

	free(s);
}


/**
 * Assigns a pointer (float *p) a numeric value (12.5).
 */
void nine()
{
	float *p = (float *)malloc(sizeof(float));
	*p = 12.5;

	printf("The value of p is: %f\n", *p);
	free(p);
}


/**
 * Reset the value of x to zero.
 *
 * @param x
 *     Pointer to reset to 0.
 */
void ten(int *x)
{
	*x = 0;
}


/**
 * Concatenates the strings "Hello " and "World!" together, and
 * prints the concatenated string.
 */
void eleven()
{
	char s[13] = "Hello ";
	strcat(s, "World!");
	printf("%s\n", s);
}


/**
 * Creates an array of values containing the values {0.0, 0.1, ..., 0.9}.
 */
void twelve()
{
	float *values = (float *)malloc(10*sizeof(float));

	int i, n = 10;
	for (i = 0; i < n; i++)
		values[i] = ((float)i) / n;

	for (i = 0; i < n; i++)
		printf("%f ", values[i]);
	printf("\n");
	
	free(values);
}


/**
 * Creates a 2D array of values and prints out the values on the diagonal.
 */
void thirteen()
{
	int i, j = 0;
	int ** values =(int **)malloc(10 * sizeof(int *));
	for (i = 0; i < 10; i++)
	{
		values[i] = (int *)malloc(10 * sizeof(int));
		for (j = 0; j < 10; j++)
		{
			values[i][j] = i * j;
		}
	}

	for (i = 0; i < 10; i++)
		printf("%d ", values[i][i]);
	printf("\n");
	
	for (i = 0; i < 10; i++)
	{
		free(values[i]);
	}
	
	free(values);
}


/**
 * Prints out a specific string based on the input parameter (s).
 *
 * @param s
 *     Input parameter, used to determine which string is printed.
 */
void fourteen(const char *s)
{
	if(strcmp(s,"blue") == 0)
	{
		printf("Orange and BLUE!\n");
	}
	else if(strcmp(s,"orange") == 0)
	{
		printf("ORANGE and blue!\n");
	}
	else
	{
		printf("orange and blue!\n");
	}
}


/**
 * Prints out a specific string based on the input parameter (value).
 *
 * @param value
 *     Input parameter, used to determine which string is printed.
 */
void fifteen(const int value)
{
	switch (value)
	{
		case 1:
		{
			printf("You passed in the value of one!\n");
			break;
		}

		case 2:
		{
			printf("You passed in the value of two!\n");
			break;
		}
			

		default:
		{
			printf("You passed in some other value!\n");
			break;
		}
	}
}


/**
 * Returns a newly allocated string on the heap with the value of "Hello".
 * This should not be freed.
 *
 * @returns
 *     A newly allocated string, stored on the heap, with the value "Hello".
 */
char * sixteen()
{
	char *s = malloc(6);
	strcpy(s, "Hello");
	return s;
}	


/**
 * Prints out the radius of a circle, given its diameter.
 *
 * @param d
 *     The diameter of the circle.
 */
void seventeen(const int d)
{
	printf("The radius of the circle is: %f.\n", ((float) d)/2);
}


/**
 * Manipulates the input parameter (k) and prints the result.
 *
 * @param k
 *     The input parameter to manipulate.
 */
void eighteen(int k)
{
	k = k * k;
	k += k;
	k *= k;
	k -= 1;

	printf("Result: %d\n", k);
}


/**
 * @brief
 *     Clears the bits in "value" that are set in "flag".
 *
 * This function will apply the following rules to the number stored
 * in the input parameter "value":
 * (1): If a specific bit is set in BOTH "value" and "flag", that
 *      bit is NOT SET in the result.
 * (2): If a specific bit is set ONLY in "value", that bit IS SET
 *      in the result.
 * (3): All other bits are NOT SET in the result.
 *
 * Examples:
 *    clear_bits(value = 0xFF, flag = 0x55): 0xAA
 *    clear_bits(value = 0x00, flag = 0xF0): 0x00
 *    clear_bits(value = 0xAB, flag = 0x00): 0xAB
 *
 * @param value
 *     The numeric value to manipulate.
 *
 * @param flag
 *     The flag (or mask) used in order to clear bits from "value".
 */
void clear_bits(long int value, long int flag)
{
	long int testval = value;
	int index = 0;
	while(testval != 0)
	{
		testval = testval >> 1;
		index++;
	}
	int bits[index];
	int flagbits[index];
	long int temp = 0;

	int i = index - 1;
	

	for(i; i >= 0; i--)
	{
		bits[i] = value & 1;
		value = value >> 1;
	}

	for(i = index - 1; i >= 0; i--)
	{
		flagbits[i] = flag & 1;
		flag = flag >> 1;
	}

	for(i = 0; i < index; i++)
	{
		if(flagbits[i] == bits[i] && bits[i] == 1)
		{
			temp = temp << 1;
		}
		else if(bits[i] == 1 && flagbits[i] == 0)
		{
			temp  = temp << 1;
			temp |= 1;
		}
		else
		{
			temp = temp << 1;
		}
	}
	
	value = temp;
}
