/**
 * Jay Patel
 * CS 255
 * 07/26/2014
 **/

#include <iostream> 
using namespace std; 
 
class Euclid 
{ 
public: 
 int x, y; 
 int remainder; 
 Euclid() { x = 0, y = 0, remainder = 0;} 
 int findGCD(int a, int b) 
 { 
 int mx;
 int mn;
 if (a != b)
 {
 	mx = (a < b ? b : a);
 	mn = (a < b ? a : b);
 }
 else
 {
 	return a;
 }
 if (mx % mn == 0)
 {
 	return mn;
 }
 else
 {
 	return findGCD(mn, mx % mn);
 }
 } 
}; 
 
int main() 
{  
 int num1 = 0, num2 = 0; 
 Euclid e; 
 
 cout << "The Euclidean Algorithm" << endl; 
 
 cout << "enter the first positive integer" << endl; 
 cin >> e.x; 
 
 cout << "enter the second positive integer" << endl; 
 cin >> e.y; 
 
 cout << endl;

 int gcd = e.findGCD(e.x, e.y);
 cout << "The GCD of " << e.x << " and " << e.y <<  " is " <<  gcd << endl;
 cout << e.x << " = " << gcd << " x " << e.x/gcd << " + " << 0 << endl;
 cout << e.y << " = " << gcd << " x " << e.y/gcd << " + " << 0 << endl;
 return 0; 
} 
