#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * loop_infinite - manage zombie process through infinite while
 * Void: no parameters to be entered
 * Return: 0 in case of success
 */
int loop_infinite(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 * Void: no arguments to be enetered
 * Return: 0 in case of success
 */
int main(void)
{
	pid_t small_pid;
	int process_numbers;

	for (process_numbers = 1; process_numbers < 6; process_numbers++)
	{
		small_pid = fork();
		if (small_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", small_pid);
			sleep(1);
		}
		else
		{
			exit(0);
		}
	}
	loop_infinite();
	return (0);
}
