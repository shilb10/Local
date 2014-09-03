/*
 * Jay Patel
 * 7/2/2014
 * CS 255
 */
#include <iostream> 
#include <iomanip> 
using namespace std; 

int main() {
int weights[] = {0,0,0,0,0,0};
cout << "Enter weight AB: ";
cin >> weights[0];
cout << "Enter weight AC: ";
cin >> weights[1];
cout << "Enter weight AD: ";
cin >> weights[2];
cout << "Enter weight BC: ";
cin >> weights[3];
cout << "Enter weight BD: ";
cin >> weights[4];
cout << "Enter weight CD: ";
cin >> weights[5];

int possibleSums[] = {0,0,0,0,0,0};
possibleSums[0] = weights[1] + weights[3] + weights[4];
possibleSums[1] = weights[1] + weights[5] + weights[4];
possibleSums[2] = weights[0] + weights[3] + weights[5];
possibleSums[3] = weights[0] + weights[4] + weights[5];
possibleSums[4] = weights[2] + weights[5] + weights[3];
possibleSums[5] = weights[2] + weights[4] + weights[3];

int min = possibleSums[0] + 1;
int index = 0;
int max = -1;
int same = 0;
for (int i = 0; i < 6; i++)
{
	if (min == possibleSums[i])
	{
		same++;
	}
	if (min > possibleSums[i])
	{
		min = possibleSums[i];
		index = i;
	}
	if (max < possibleSums[i])
	{
		max = possibleSums[i];
	}
}
if (same > 0)
{
	cout << "More than one minimal path available." << endl;
}
cout << "Minimal path shown below. Path length differs from maximal path by: " << max - min << "." << endl;
cout << min << endl;
switch (index) {
	case (0):
		cout << "A -> C -> B -> D" << endl;
		break;
	case (1):
		cout << "A -> C -> D -> B" << endl;
		break;
	case (2):
		cout << "A -> B -> C -> D" << endl;
		break;
	case (3):
		cout << "A -> B -> D -> C" << endl;
		break;
	case (4):
		cout << "A -> D -> C -> B" << endl;
		break;
	default:
		cout << "A -> D -> B -> C" << endl;
		break;
}
return 0;
}