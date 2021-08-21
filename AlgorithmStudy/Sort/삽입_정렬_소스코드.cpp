#include <bits/stdc++.h>
using namespace std;

int main() {
	int target[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
	int len = sizeof(target)/sizeof(int);
	
    // insertion sort target in ascending order
	for(int i=1;i<len;i++){
		for(int j=i;j>0;j--){
            if(target[j]<target[j-1]){
                swap(target[j], target[j-1]);
            }
            else break;
        }
	}

    // print sorted target
	for(int i=0;i<len;i++)
		cout << target[i] << ' ';
	
	return 0;
}