#include <bits/stdc++.h>
using namespace std;

bool check(int h, int m, int s){
	if(s%10==3 || s/10==3 || m%10==3 || m/10==3 || h%10 == 3 || h/10 == 3)
		return true;
	return false;
}

int main() {
	int N, count=0;
	scanf("%d", &N);
	for(int h=1;h<=N;h++){
		for(int m=1;m<60;m++){
			for(int s=1;s<60;s++){
				if(check(h,m,s)){
					count++;
				}
			}
		}
	}
	cout << count;
}