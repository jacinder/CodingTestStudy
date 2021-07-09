#include <vector>
#include <iostream>
using namespace std;

vector<bool> visited(9, false);
int map[201][201];
int row, col;

int bfs(){
	int count = 1;
	int y = 0;
	int x = 0;
		while(1){
			if(map[y][x+1]==1 && x<col-1){
				x++;
				count++;
			}
			else if(map[y+1][x]==1 && y<row-1){
				y++;
				count++;
			}
			else{
				break;
			}
		}
	
	return count;
}

int main(){
	// get input: col, row
	scanf("%d %d",&row, &col);

	// declare & initialize input
	int count = 0;
	int tmp = 0;
	
	// get input: initial graph
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			scanf("%1d",&tmp);
			map[i][j] = tmp;
		}
	}

	// find connected component
	int result = bfs();

	cout << result << '\n';

}