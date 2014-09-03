#include <iostream> 
using namespace std; 
 
//Base class that contains data member and accessors and pure 
//virtual function that is implemented in the derived classes 
 
class Convert { 
protected: 
 double val1, val2;//data members 
public: 
 Convert(double i)//constructor to initialize variable to convert 
 { val1 = i; } 
 double getconv()//accessor for converted value 
 { return val2; } 
 double getinit()//accessor for the initial value 
 { return val1; } 
 virtual void compute() = 0;//function to implement in derived 
}; 

class L_To_G : public Convert 
//derived class 
{ 
public: 
 L_To_G(double i) : Convert(i) { } 
 //implementation of virtual function 
 void compute() 
 { 
 val2 = val1 / 3.7854; 
 //conversion assignment statement 
 } 
};

class K_To_M : public Convert
{
public:
	K_To_M(double i) : Convert(i) { }
	void compute()
	{
		val2 = val1/1.60934;
	}
};

class M_To_F : public Convert
{
public:
	M_To_F(double i) : Convert(i) { }
	void compute()
	{
		val2 = val1*3.28084;
	}
};

class C_To_F : public Convert
{
public:
	C_To_F(double i) : Convert(i) { }
	void compute()
	{
		val2 = val1*9/5 + 32;
	}
};

int main() 
{ 
 //declare and initialize variables 
 char again = 'y'; 
 int c = 0; 
 double num = 0; 
 
 //declare pointer object(s) 
 Convert *p; 
 
 //display menu and perform selection 
 while (again == 'y') 
 { 
 cout <<" Please enter a number to convert: "; 
 cin >> num; 
 cout << endl; 
 cout << "\nWhat would you like to convert? \n\n" 
 << " '1' for Liters to Gallons.\n" 
 << " '2' for Kilometers to Miles.\n" 
 << " '3' for Meters to Feet.\n" 
 << " '4' for Celcius to Fahrenheit.\n"; 
 cin >> c; 
 cout << "\n"; 
 
 switch (c) 
 { 
 case 1: 
 { 
 p = &L_To_G(num); 
 p->compute(); 
 cout << num << " liters is " << p->getconv() 
 << " gallons " ; 
 cout << endl; 
 break; 
 }
 case 2:
 { 
 p = &K_To_M(num); 
 p->compute(); 
 cout << num << " kilometers is " << p->getconv() 
 << " miles " ; 
 cout << endl; 
 break; 
 }
 case 3:
 { 
 p = &M_To_F(num); 
 p->compute(); 
 cout << num << " meters is " << p->getconv() 
 << " feet " ; 
 cout << endl; 
 break; 
 }
 case 4:
 { 
 p = &C_To_F(num); 
 p->compute(); 
 cout << num << " degrees celcius is " << p->getconv() 
 << " degrees fahrenheit " ; 
 cout << endl; 
 break; 
 }
 default: 
 cout << "The number is out of range.\n"; 
 break; 
 }//end switch 
 cout << "\nDo you want to convert again? (y or n)"; 
 cin >> again; 
 }//end while 
 return 0; 
}//end main 
