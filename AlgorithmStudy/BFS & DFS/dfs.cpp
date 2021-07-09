#include <iostream>
#include <vector>

using namespace std;

bool visited[9];
vector<int> graph[] = {{}, 
				{2,3,8}, 
				{1, 7},
				{1, 4, 5},
				{3, 5},
				{3, 4},
				{7},
				{2, 6, 8},
				{1, 7}};

void dfs(int x){
	visited[x] = true;
	cout << x << ' ';
	for(int i=0;i<graph[x].size();i++){
		int y = graph[x][i];
		if(!visited[y]) dfs(y); // 방문하지 않은 노드라면 그 노드먼저 처리하고 돌아온다.
	}
}

int main() {
    
	// DFS logic 
    dfs(1);
}