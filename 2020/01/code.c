#include <stdlib.h>
#include <stdio.h>

#define bool int
#define true 1
#define false 0

#define arr(type, len) (type*)malloc(sizeof(type) * len)

#define desiredSum 2020

int numLines(FILE* fp) {
	int out = 0;
	
	bool validLine = false;
	char c;
	while (c = getc(fp)) {
		if (c == EOF) break;
		else if (c >= '0' && c <= '9') {
			validLine = true;
		}
		else if (c == '\n') {
			if (validLine) out += 1;
			validLine = false;
		}
	}
	
	return out;
}

void parseNums(FILE* fp, int* buf) {
	int y = 0;
	int x = 0;
	
	char* line = arr(char, 5);
	char c;
	while (c = getc(fp)) {
		if (c == EOF) break;
		else if (c >= '0' && c <= '9') {
			line[x] = c;
			x += 1;
		}
		else if (c == '\n') {
			line[x] = 0;
			x = 0;
			
			buf[y] = atoi(line);
			y += 1;
		}
	}
}

int task1(int* nums, int size) {
	for (int i = 0; i < size; i++) {
		for (int i2 = 0; i2 < size; i2++) {
			int num1 = nums[i];
			int num2 = nums[i2];
			if (num1 + num2 == desiredSum) {
				return num1 * num2;
			}
		}
	}
	printf("Failed to solve");
	exit(1);
}

int task2(int* nums, int size) {
	for (int i = 0; i < size; i++) {
		for (int i2 = 0; i2 < size; i2++) {
			for (int i3 = 0; i3 < size; i3++) {
				int num1 = nums[i];
				int num2 = nums[i2];
				int num3 = nums[i3];
				if (num1 + num2 + num3 == desiredSum) {
					return num1 * num2 * num3;
				}
			}
		}
	}
	printf("Failed to solve");
	exit(1);
}

void main() {
    FILE* fp;
	
	fp = fopen("input.txt","r");
	int lines = numLines(fp);
	fclose(fp);
	
	int* nums = arr(int, lines);
	fp = fopen("input.txt","r");
	parseNums(fp, nums);
	fclose(fp);
	
	printf("Task1: %d\n", task1(nums, lines));
	printf("Task2: %d\n", task2(nums, lines));
	
	exit(0);
}
