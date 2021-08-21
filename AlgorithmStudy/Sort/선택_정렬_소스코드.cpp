#include <bits/stdc++.h>
using namespace std;

int main() {
	int target[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
	int len = sizeof(target)/sizeof(int);
	
    // selection sort target in ascending order
	for(int i=0;i<len;i++){
		int min_idx = i;
		for(int j=i+1;j<len;j++){
			if(target[min_idx]>target[j]) min_idx = j;
		}
		swap(target[i],target[min_idx]);
	}

    // print sorted target
	for(int i=0;i<len;i++)
		cout << target[i] << ' ';
	
	return 0;
}