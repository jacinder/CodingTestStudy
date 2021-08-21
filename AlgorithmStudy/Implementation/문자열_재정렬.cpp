#include <bits/stdc++.h>
using namespace std;

int main() {
	char input[10001];
	int num = 0;
	vector<char> alphabet;
	scanf("%s",input);
	for(int i=0;i<strlen(input);i++){
		// 만약 숫자라면
		if(input[i]<'A'){
			num += input[i]-'0';
		}
		//만약 문자라면 (only capital case)
		else{
			alphabet.push_back(input[i]);
		}
	}
	sort(alphabet.begin(), alphabet.end());
	for(int i=0;i<alphabet.size();i++){
		cout << alphabet[i];
	}
	cout << num;
}