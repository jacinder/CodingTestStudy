#include <iostream>
// #include <bits/stdc++.h>
#include <stack>
#include <queue>
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


void bfs(int start){

    queue<int> q;
    q.push(start);
    visited[start] = true;
    while(!q.empty()){

        int x = q.front();
        q.pop();
        cout << x << ' ';

        // push adjacent nodes into queue 
        for(int i=0;i<graph[x].size();i++){
            int y = graph[x][i];
            if(!visited[y]){
                q.push(y);
                visited[y] = true;
            }
        }
    }
}
int main(){
    bfs(1);
    return 0;
}