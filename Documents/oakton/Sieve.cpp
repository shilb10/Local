#include <iostream>
using namespace std;

int main() {
	int n = 1000;
	int a[1000];
	int p = 2;
	a[0] = 1;
	for (int i = 1; i < n; i++) {
		a[i] = 1;
	}
	while (p*p <= n) {
		int j = 2*p;
		while (j < n) {
			a[j] = 0;
			j = j + p;
		}
		p++;
		while (a[p] != 1 && p*p <= n) {
			p++;
		}
	}
	cout << "Primes less than 1000:" << "\n**********************" << endl;
	for (int i = 2; i < n; i++) {
		if (a[i] == 1){
			cout << i << " ";
		}
	}	
	cout << endl;
	return 1;
}