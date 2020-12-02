#include <stdlib.h>
#include <stdio.h>

#define bool int
#define true 1
#define false 0

#define arr(type, len) (type*)malloc(sizeof(type) * len)

int numLines(FILE* fp) {
	int out = 0;

	bool validLine = 0;
	char c;
	while (true) {
		c = getc(fp);
		if (c == EOF) break;
		else if (c >= '-' && c <= 'z') validLine = true;
		else if (c == '\n') {
			if (validLine) out += 1;
			validLine = false;
		}
	}

	return out;
}

typedef struct Entry {
	int min;
	int max;
	char c;
	char* pass;
	int pass_len;
} Entry;

void parseEntries(FILE* fp, Entry* buf) {
	int y = 0;
	
	char* line;
	size_t line_len;
	ssize_t chars;
	while ((chars = getline(&line, &line_len, fp)) != -1) {
		// format: "min-max c: pass"
		
		int x = 0;
		Entry* entry = &buf[y];

		// min
		for (; x < chars; x++) {
			if (line[x] == '-') {
				line[x] = 0;
				entry->min = atoi(line);
				break;
			}
		}
		
		// max
		x += 1;
		char* maxStart = line + (sizeof(char) * x);
		for (; x < chars; x++) {
			if (line[x] == ' ') {
				line[x] = 0;
				entry->max = atoi(maxStart);
				break;
			}
		}
		
		x += 1;
		entry->c = line[x];
		
		x += 3;
		int pass_len = chars - 1 - x;
		char* pass = arr(char, pass_len);
		for (int p = 0; p < pass_len; p++) {
			pass[p] = line[x + p];
		}
		entry->pass = pass;
		entry->pass_len = pass_len;

		y += 1;
	}
	if(line) free(line);
}

int task1(Entry* entries, int numEntries) {
	int valid = 0;
	
	for (int x = 0; x < numEntries; x++) {
		Entry* entry = &entries[x];
		
		int count = 0;
		for (int y = 0; y < entry->pass_len; y++) {
			if (entry->pass[y] == entry->c) {
				count += 1;	
			}
		}
		if (count >= entry->min && count <= entry->max) {
			valid += 1;
		}
	}
	
	return valid;
}

int task2(Entry* entries, int numEntries) {
	int valid = 0;
	
	for (int x = 0; x < numEntries; x++) {
		Entry* entry = &entries[x];
		
		int min = entry->min - 1;
		int max = entry->max - 1;
		char c = entry->c;
		
		if (entry->pass_len > max && ((entry->pass[min] == c) != (entry->pass[max] == c))) {
			valid += 1;
		}
	}
	
	return valid;
}


void main() {
	FILE* fp;
	
	fp = fopen("input.txt", "r");
	int lines = numLines(fp);
	fclose(fp);

	Entry* entries = arr(Entry, lines);
	fp = fopen("input.txt", "r");
	parseEntries(fp, entries);
	fclose(fp);
	
	printf("Task1: %d\n", task1(entries, lines));
	printf("Task2: %d\n", task2(entries, lines));
	
	exit(0);
}
