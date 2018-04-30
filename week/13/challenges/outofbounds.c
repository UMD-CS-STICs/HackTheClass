#include <unistd.h>
#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 21
#define READ_SIZE 22

char pass[BUFFER_SIZE];
char flag[BUFFER_SIZE];
FILE* f;
int i;

int main()
{
  char buffer[BUFFER_SIZE];
  unsigned char valid = 0;

  f = fopen("pass","r");
  fgets(pass, BUFFER_SIZE, f);
  fclose(f);

  f = fopen("flag","r");
  fgets(flag, BUFFER_SIZE, f);
  fclose(f);

  for (i = 0; i < 3; i++)
  {
    printf("Enter password: ");
    fflush(stdout);
    read(STDIN_FILENO, buffer, READ_SIZE);

    if (strncmp(buffer, pass, 20) == 0) {
      printf("pass??");
      valid |= 1;
    }

    if (valid)
    {
      printf("Authenticated: %s\n", flag);
      return 0;
    }

    else if (strnlen(buffer, 20) != BUFFER_SIZE)
      printf("Password must be EXACTLY 20 characters\n");

    printf("Wrong password. %d more tries.\n", 2-i);

  }

  printf("INTRUDER ALERT!\n");
  return -1;
}

