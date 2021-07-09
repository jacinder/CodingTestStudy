#include <vector>
#include <iostream>
using namespace std;

vector<bool> visited(9, false);
int ** map;
int row, col;

int bfs(){
	int count = 0;
	int x = 0;
	int y = 0;

	while( x<col-1 || y<row-1 ){
		
		if(map[x][y+1] && y<row-1){
			y++;
			count++;
		}
		else if(map[x+1][y] && x<col-1){
			x++;
			count++;
		}
	}
	return count;
}

int main(){
	// get input: col, row
	scanf("%d %d",&row, &col);
	
	// alocation mold
	map = (int**)malloc(sizeof(int)*row);
	for(int i=0;i<row;i++) map[i] = (int*)malloc(sizeof(int)*col);
	
	// declare & initialize input
	char temp[col+1];
	temp[0] = '\n';
	int count = 0;
	
	// get input: initial graph
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			scanf("%1d",&map[i][j]);
		}

	}

	// find connected component
	int result = bfs();

	cout << result << '\n';

}