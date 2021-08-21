#include <iostream>
using namespace std;

int main() {
	int N, K, count=0;
	scanf("%d %d",&N, &K);
	while(1){
		if(N == 1){
			break;
		}
		
		if(N % K == 0){
			// 나눌 수 있으면 무조건 나눈다.
			// 이게 Greedy인 이유인듯?
			N = N/K;
		}
		else{
			N = N-1;
		}
		count++;
	}
	cout << count << '\n';
}