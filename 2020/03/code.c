#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

char *readFile(char *filename) {
	FILE *f = fopen(filename, "rt");
	fseek(f, 0, SEEK_END);
	long length = ftell(f);
	fseek(f, 0, SEEK_SET);
	char *buffer = (char *) malloc(length + 1);
	buffer[length] = '\0';
	fread(buffer, 1, length, f);
	fclose(f);
	return buffer;
}

bool** parse(char* input) {
	// count y axis
	int numY = 0;
	for (int i = 0; i >= 0; i++) {
		char c = input[i];
		if (c == 0) break;
		else if (c == '\n') numY += 1;
	}
	bool** out = (bool**)malloc(sizeof(bool*) * numY);
	
	for (int i = 0; i >= 0; i++
}

void main() {
	char* input = readFile("input.txt");
	bool** map = readFile(input);
}
