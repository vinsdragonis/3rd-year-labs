#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>
#include<string.h>
#include<fcntl.h>
#include<sys/stat.h>
#include<errno.h>


int main(int argc,char *argv[])
{

   int fd;
   char buf[256];
   
   if(argc!=2 && argc!=3) {
      printf("USAGE %s <file> [<arg>]\n",argv[0]);
      return 0;
   }

   mkfifo(argv[1],S_IFIFO|S_IRWXU|S_IRWXG|S_IRWXO);

   if(argc==2) {
      fd=open(argv[1],O_RDONLY|O_NONBLOCK);
      
      while(read(fd,buf,sizeof(buf))>0)
         printf("%s",buf);
   } else {
      fd=open(argv[1],O_WRONLY);
      write(fd,argv[2],strlen(argv[2]));
   }
   
   close(fd);
}
