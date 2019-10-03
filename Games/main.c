#include <stdio.h>

int main(){

	char answer[50];
	printf("Do you want to play a game?\n");
	scanf("%s", answer);
	if (strcmp(answer, "no")){
		printf("Good, lets get started!\n");
		return 0;
	} else {
		printf("Sad, bye bye\n");
		return 0;
	}
}
