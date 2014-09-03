#include <stdio.h>
#include <stdlib.h>

/**
 * Compute the length of a string s.
 * @param s a string
 * @return the number of characters preceding the NULL terminator
 */
size_t strlen(const char *s)
{
  int len;
  for (len=0; *s; s++, len++);
  return len;
}

/**
 * Lexicographically compare strings s1 and s2.
 * @param s1 a string
 * @param s2 a string
 * @return an integer greater than, equal to, or less than zero if s1 is
 *         greater than, equal to, or less than s2, respectively.
 */
int strcmp(const char *s1, const char *s2)
{
  for (; *s1 && *s2 && *s1 == *s2; s1++, s2++);
  return *s1 - *s2;
}

/**
 * Copy the string s2 to s1 (including the terminating `\0').
 * @param s1 a mutable string
 * @param s2 a constant string
 * @return a pointer to s1
 */
char *strcpy(char *restrict s1, const char *restrict s2)
{
  char *p = s1;
  while ( *(p++) = *(s2++) );
  return s1;
}

/**
 * Append the string s2 to the end of the string s1.
 * @param s1 a mutable string
 * @param s2 a constant string
 * @return a pointer to s1
 */
char *strcat(char *restrict s1, const char *restrict s2)
{
  char *p=s1;
  while ( *p ) p++;
  while ( *(p++) = *(s2++) );
  return s1;
}

/**
 * Find the first occurence of (char)c in s.
 * The terminating NULL is considered part of the string, 
 * therefore if c is `\0', strchr should locate the 
 * terminating `\0'.
 * @param s a string
 * @param c a character to search for
 * @return a pointer to the located character or NULL if it could not be found
 */
char *strchr(const char *s, int c)
{
  while ( *s && *s != c ) s++;
  return (char *)(*s == c ? s : NULL);
}

/**
 * Find the last occurence of (char)c in s.
 * The terminating NULL is considered part of the string, 
 * therefore if c is `\0', strchr should locate the 
 * terminating `\0'.
 * @param s a string
 * @param c a character to search for
 * @return a pointer to the located character or NULL if it could not be found
 */
char *strrchr(const char *s, int c)
{
  const char *p = NULL;
  for (; *s; s++) if( *s == c ) p = s;

  return (char *)(c ? p : s);
}

/**
 * Find the first occurence of any character in the string s2 in s1.
 * @param s1 the string to search
 * @param s2 a string containing the characters to search for
 * @return the location of the character located or NULL if no character was found
 */
char *strpbrk(const char *s1, const char *s2)
{
  const char *p;
  for (;*s1; s1++)
    for (p=s2; *p; p++) if( *s1 == *p ) return (char *)s1;

  return NULL;
}

/**
 * Tokenize the string *stringp.
 * Locates in the string *stringp any character from the string 
 * delim, or the terminating '\0' and replaces it with '\0'.
 * The location of the next character after the delimiter character 
 * is stored in *stringp (or NULL if the end of the string was 
 * reached).  The original value of *stringp is returned.
 * @param stringp pointer to a string to tokenize
 * @param delim the delimiter characters
 * @return the original value of string p
 */
char *strsep(char **stringp, const char *delim)
{
  char *p;
  if ( (p = *stringp) && (*stringp = strpbrk(p, delim)) )
    *(*stringp)++ = '\0';

  return p;
}

