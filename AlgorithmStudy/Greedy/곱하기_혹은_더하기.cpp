#include <iostream>
#include <cstring>
using namespace std;

int main() {
	char S[21];
	int result = 0;
    // 처음에 result를 1로 지정했는데, 문제 조건없이 임의로 주는 것은 위험하다.
    // 문제 조건에 알맞는 초기값을 설정할 수 있도록 한다.
    // 이 문제에서 적절한 초기값은 문자열의 첫번째 값이다.
	scanf("%s",S);
	for(int i=0;i<strlen(S);i++){
		int temp = int(S[i])-'0';
		cout << "temp: " << temp << '\n';
		if(result == 0 || temp == 0 || temp == 1){
			result += temp;
		}
		else{
			result *= temp;	
		}
	}

	cout << result << '\n';
	
}