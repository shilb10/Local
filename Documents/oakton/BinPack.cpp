/**
 * Name: Jay Patel
 * Course: CSC 255
 * Date: 6/15/2014
**/


#include <iostream> 
using namespace std; 
 
class PackThis { 
 public: 
 //data member 
 int number; 
 //default constructor 
 PackThis() { number = 0;} 
 //member function 
 
 void TimeToPack() { 
 //declare and initialize variables 
 int giant = 0, large = 0, medium = 0, small = 0; 
 
 //commence the packing process 
 giant = int(number / 50); 
 cout << "Giant              " << giant << "         $"  << giant*50*5 << endl; 
 number = number - giant * 50; 
 large = int(number / 20); 
 cout << "Large              " << large << "          $"  << large*20*5 << endl; 
 number = number - large * 20; 
 medium = int(number / 5); 
 cout << "Medium             " << medium << "          $"  << medium*5*5 << endl;  
 small = number - medium * 5; 
 cout << "Small              " << small << "          $"  << small*1*5 << endl;  } 
};//end class 
 
int main() { 
 //declare and initialize variable(s) and object(s) 
 int n = 0; 
 char i = 0;
 PackThis p; 
 
 //request data from user 
 cout << "Sedgwick Specialty Services " << endl; 
 cout << "Number of Communicators to Ship: ";
 
 //read the data 
 cin >> n;

 cout << "\n" << endl;
 cout << "container type     number     total cost per container type" << endl;
 cout << "**************     ******     *****************************" << endl; 
 //class object updates data member 
 p.number = n; 
 //class object calls member function  
 p.TimeToPack(); 
 
 cout << "Press any key to continue . . .";
 cin >> i;
 return 0; 
 
}//end main 
