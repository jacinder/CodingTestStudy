// 다시 풀어봐야하는 문제
#include <bits/stdc++.h>
using namespace std;
int n;
vector<int> arr;

int main() {
	// 공포도가 n이라면, n명 이상으로 구성한 모험가 그룹에 참여
	// 최대 몇 개의 모험가 그룹을 만들 수 있는가?
	scanf("%d", &n);
	for(int i=0;i<n;i++){
		int x;
		scanf("%d", &x);
		arr.push_back(x); // vetor 사용법.
	}
	sort(arr.begin(), arr.end()); // vector stl로 정렬가능.

    // 1 2 2 2 3
	// 1 | 2 2 | 2 3 3 |
	int result = 0; // 총 길드의 수
	int cnt = 0; // 현재 길드에 포함된 모험가의 수
	for(int i=0;i<n;i++){ 
		cnt += 1; 
		if(cnt >= arr[i]){ // 길드 결성! 
			result += 1; 
			cnt = 0; 
		}
	}
	cout << result << '\n'; 
}