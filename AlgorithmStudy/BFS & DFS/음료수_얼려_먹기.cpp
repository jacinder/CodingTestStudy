#include <vector>
#include <iostream>
using namespace std;

vector<bool> visited(9, false);
int ** mold;
int row, col;

bool dfs(int i, int j){
	if( i<=-1 || i>=row || j<=-1 || j>=col ){
		return false;
	}

	if(mold[i][j]==0){
		mold[i][j] = 1;
		dfs(i-1,j);
		dfs(i+1,j);
		dfs(i,j-1);
		dfs(i,j+1);
		return true;
	}
	return false;
}

int main(){
	// get input: col, row
	scanf("%d %d",&row, &col);
	
	// alocation mold
	mold = (int**)malloc(sizeof(int)*row);
	for(int i=0;i<row;i++) mold[i] = (int*)malloc(sizeof(int)*col);
	
	// declare & initialize input
	char temp[col+1];
	temp[0] = '\n';
	int count = 0;
	
	// get input: initial graph
	for(int i=0;i<row;i++){
		scanf("%s", temp);
		for(int j=0;j<col;j++){
			mold[i][j] = int(temp[j])-'0';
			// 정수 한글자만 입력받는 법이 기억이 안나서 이렇게 해결했다ㅠ
			// scanf("%1d",&mold[i][j])
		}

	}

	// find connected component
	for(int i=0;i<row;i++){
		for(int j=0;j<col;j++){
			if (dfs(i,j) == true){
				count ++;
			}
		}
	}

	cout << count << '\n';

}