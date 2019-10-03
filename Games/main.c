#include <stdio.h>

int main(){

	char answer[50];
	int points = 0;
	printf("Do you want to play a game?\n");
	scanf("%s", answer);
	if (strcmp(answer, "no")){
		printf("Good, lets get started!\n");
		
	} else {
		printf("Sad, bye bye\n");
		return 0;
	}

	
	printf("I am going to ask you question. If you answer correct you get a point, if not you don't\n");
	getchar();
	printf("First question: What is the name of Batmans butler?\n");
	scanf("%s", answer);
	if (strcmp(answer, "Alfred") == 0 || strcmp(answer, "Alfred Pennyworth") == 0 || strcmp(answer, "alfred") == 0){
		printf("Correct! Good job\n");
		points++;
	} else {
		printf("Wrong, his name is Alfred Pennyworth\n");
	}
	return 0;
}
