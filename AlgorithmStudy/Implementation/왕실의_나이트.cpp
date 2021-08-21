#include <bits/stdc++.h>
using namespace std;

int main() {
	char position[10];
	int count = 0;
	scanf("%s",position);
	int x = position[0]-'a'+1;
	int y = position[1]-'0';

	int dx[8] = {2,2,-2,-2,1,-1,1,-1};
	int dy[8] = {1,-1,1,-1,2,2,-2,-2};
	
	for(int i=0;i<8;i++){
		if(0<x+dx[i] && x+dx[i]<9 && 0<y+dy[i] && y+dy[i]<9)
			count++;
	}
	cout << count;
	
}