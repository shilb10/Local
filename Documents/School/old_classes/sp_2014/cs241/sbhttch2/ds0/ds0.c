#include <stdio.h>
#include <string.h>

/* struct mystruct{ */
/*   char a[4]; */
/*   int b; */
/* }; */

struct mystruct{
  char a[5];
  int b;
};

int main(){
  
  char *str1 = malloc(7);
  strcpy(str1,"hello");
  char str2[7] = "world!";

  /* What would happen ? */
  /* strcpy(str1, str2); */
  strcat(str1, str2);
  printf("%s\n",str1);
  /* free(str1); */

  char *str_buf = (char *)malloc(5);
  strcat(str_buf,"123");
  printf("%s\n",str_buf);


  char * tmp_a = "Hello World!";
  char tmp_b [] = "Hello World!";
  char tmp_c [13] = "Hello World!";
  /* tmp_a[5] = 'a';  */
  tmp_b[1] = 'b';
  temp_c[4] = 'x';

  /* magic_number in hex: */
  /* 0 21 69 68 */
  /* \0 ! i h */
  int magic_number = 2189672;
  printf("%s\n",(char *)&magic_number);

  printf("%d\n",sizeof(struct mystruct));

  return 0;
}
