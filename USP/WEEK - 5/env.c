#include<stdio.h>

int main(int argc, char *argv[]) {
   int i;
   char **ptr;
   extern char **environ;
   
   printf("\n\nStart success\n\n");
   
   for(ptr=environ;*ptr!=0;ptr++)
      printf("%s\n",*ptr);
      
      printf("\n\nEnd success\n\n");

   return 0;
}
