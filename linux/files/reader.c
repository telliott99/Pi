// gcc reader.c -o reader && ./reader <filename>

#include<stdio.h>
#include<stdlib.h>

int count_nulls(unsigned char *buf, int size) {
  int count = 0;
  for (int j=0; j<size; j++){
    if (buf[j] == 0x00) {
      count += 1;
    }
  }
  return count;
}

int main(int argc, char ** argv){
  if (!(argc > 1)) {
    printf("need a filename\n");
    exit(1);
  }
  printf("%s\n", argv[1]);

  unsigned char buffer[16];
  FILE *ptr;
  ptr = fopen(argv[1],"rb");
  if (ptr==NULL) {
    fputs ("File error\n",stderr);
    exit(1);
  }

  int i, bytes_read, count, num_of_nulls;
  bytes_read = fread(buffer,sizeof(buffer),1,ptr);
  num_of_nulls = count_nulls(buffer, sizeof(buffer));
  count = 0;

  while (bytes_read != 0 && num_of_nulls != sizeof(buffer)) {
    for (i=0; i<sizeof(buffer); i++) {
      printf("%3x", buffer[i]);
    }
   count += sizeof(buffer);
   printf("%5i\n", count);
   bytes_read = fread(buffer,sizeof(buffer),1,ptr);
   num_of_nulls = count_nulls(buffer, sizeof(buffer));
  }

  if (bytes_read != 0) {
    // print the first line of nulls
    for (i=0; i<sizeof(buffer); i++) {
      printf("%3x", buffer[i]);
    }
    count += sizeof(buffer);
    printf("%5i\n", count);
  }
  return 0;
}
