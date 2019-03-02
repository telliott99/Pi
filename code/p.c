#include<stdio.h>

int main(int argc, char ** argv){
  char *msg = "hi\0";
  printf("%s", msg);
  if (argc > 1) 
    printf(" %s\n", argv[1]);
  else printf("\n");
  return 0;
}
