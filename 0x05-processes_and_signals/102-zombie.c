#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - keep parent process busy
 * @void: void
 * Return: 0
 */


int infinite_while(void);
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create Zoombie process
 * @void:void
 * Return:...
 */


int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid < 0)
		{
			perror("fork");
			exit(1);
		}
		else if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
}
