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

void print_array(unsigned char *buf, int size, unsigned int counter) {
  for (int j=0; j<size; j++){
    printf("%3x", buf[j]);
  }
  printf("%13u\n", counter);
}

int main(int argc, char ** argv){
  if (!(argc > 1)) {
    printf("need a filename\n");
    exit(1);
  }
  printf("%s\n", argv[1]);
  
  FILE *ptr;
  ptr = fopen(argv[1],"rb");
  if (ptr==NULL) {
    fputs ("File error\n",stderr);
    exit(1);
  }
  
  unsigned char buffer[16];
  unsigned char prev_line[16];

  int i, nulls, prev_nulls, bytes_read, count;
  count = 0; 
  unsigned int byte_counter = 0;  // enough not to overflow?
  int n = sizeof(buffer);
  nulls = n;
  
  bytes_read  = fread(buffer,n,1,ptr);
  
  while (bytes_read  != 0) {
    byte_counter += n;  
      
    prev_nulls = nulls;
    nulls = count_nulls(buffer, n);
    
    if (nulls == n && prev_nulls != n) {
      count += 1;
    // then we're at a transition so print:
      print_array(prev_line, n, byte_counter - n);
      print_array(buffer, n, byte_counter);
    }

    // copy current line
    for (i=0; i<n; i++) {
      prev_line[i] = buffer[i];
    }
    // continue on to next line
    bytes_read = fread(buffer,n,1,ptr);
  }
  printf("%i found\n", count);
  return 0;
}
