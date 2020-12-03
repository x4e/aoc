#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define ulong unsigned long

#define xLen 31
#define yLen 323

char* readFile(char* name) {
	FILE* fp = fopen(name, "rb");
	fseek(fp, 0, SEEK_END);
	long fsize = ftell(fp);
	fseek(fp, 0, SEEK_SET);
	
	char* string = (char*)malloc(fsize + 1);
	
	char* currentString = string;
	
	char* line = NULL;
	size_t len = 0;
	ssize_t nread;
	while ((nread = getline(&line, &len, fp)) != -1) {
		int bytesRead = nread * sizeof(char) - 1;
		memcpy(currentString, line, bytesRead);
		currentString += bytesRead;
	}
	
	fclose(fp);
	
	return string;
}

bool get(char* text, int x, int y) {
	x %= xLen;
	return text[(y * 31) + x] == '#';
}

ulong countTrees(char* text, int right, int down) {
	ulong trees = 0;
	int x = 0;
	int y = 0;
	
	while (y < yLen) {
		if (get(text, x, y)) {
			trees += 1;
		}
		x += right;
		y += down;
	}
	return trees;
}

ulong task1(char* text) {
	return countTrees(text, 3, 1);
}

ulong task2(char* text) {
	int slopes[5][2] = {{1,1}, {3,1}, {5,1}, {7,1}, {1,2}};
	
	ulong product = 1;
	for (int slope = 0; slope < 5; slope++) {
		product *= countTrees(text, slopes[slope][0], slopes[slope][1]);
	}
	return product;
}

void main() {
	char* text = readFile("input.txt");
	printf("Task1: %lu\n", task1(text));
	printf("Task2: %lu\n", task2(text));
}
