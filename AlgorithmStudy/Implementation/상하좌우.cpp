#include <bits/stdc++.h>
using namespace std;


int main() {
	int N, dx=0, dy=0, x=1, y=1;
	char map[101];
	scanf("%d",&N);
	for(int i=0;i<N;i++){
		scanf("%s",&map[i]);
	}

	for(int i=0;i<N;i++){
		if(map[i] == 'R'){
			dx = 1;
		}
		else if(map[i] == 'L'){
			dx = -1;
		}
		else if(map[i] == 'U'){
			dy = -1;
		}
		else{
			dy = 1;
		}
		if(x+dx<=N && 0<x+dx && y+dy<=N && 0<y+dy){
			x += dx;
			y += dy;
		}
		dx = 0;
		dy = 0;
	}

	cout << x << ' ' << y;
}