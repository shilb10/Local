//Sammy Student Programmer
/**
 * Name: Jay Patel
 * Date: 6/21/2014
 * Course: CS255
 **/
 
#include <iostream> 
#include <string> 
using namespace std; 
 
class Telephone { 
 
 private: 
 
 string firstName, lastName, month; 
 float localCell, longCell, localReg, longReg; 
 float pastDue; 
 //class data members 
 
 public: 
 
 Telephone() { 
 firstName = ""; 
 lastName = ""; 
 month = ""; 
 localCell = 0; 
 longCell = 0; 
 localReg = 0; 
 longReg = 0; 
 } //class constructor 
 
 string getName() { 
 return firstName + " " + lastName; 
 } //returns customer name 
 string getMonth() { 
 return month; 
 } //returns the billing month 
 float calcCell() { 
 return (longCell + localCell) * 0.75 + 19.99; 
 } //calculates the pretax cell charges 
 float calcReg(); 
 //calculates pretax reg phone charges 
 float getPast() { 
 return pastDue * 1.025; 
 } //calculates and returns the past due charges 
 float calcTotal(); 
 //calculates and returns the total months charges 
 void setValue(); 
 //prompts user to input 
 void checkPastDute();
 //checks whether the amount past due exceeds $100
 }; //end class definition 

 
//class member functions 
float Telephone::calcReg() { 
 return (localReg * 0.22 + longReg * 0.52 + 13.29); 
} 
 
float Telephone::calcTotal() { 
 float cellTax, regTax; 
 float total; 
 cellTax = calcCell() * 1.06; 
 regTax = calcReg() * 1.115; 
 total = 10 * 1.03 + cellTax + regTax + getPast(); 
 return total; 
} 
 
void Telephone::setValue() 
{ 
 cout << "Enter the first and last name of the customer: "; 
 cin >> firstName >> lastName; 
 cout << "Enter the billing month: "; 
 cin >> month; 
 cout << "Minutes of local cellular calls: "; 
 cin >> localCell; 
 cout << "Minutes of long distance cellular calls: "; 
 cin >> longCell; 
 cout << "Minutes of local regular telephone calls: "; 
 cin >> localReg; 
 cout << "Minutes of long distance regular telephone calls: "; 
 cin >> longReg; 
 cout << "Amount past due: "; 
 cin >> pastDue; 
} 

void Telephone::checkPastDute() {
	if (getPast() > 100) {
		cout << "\n Amount past due exceeds $100.00";
	}
}
 
int main() { 
 Telephone x; 
 x.setValue(); 
 cout.setf(ios::fixed); //format output to show 2 decimal places 
 cout.setf(ios::showpoint); 
 cout.precision(2); 
 cout << "\n\nMonthly Telephone Bill for " << x.getName(); 
 //output 
 cout << "\n Billing Month: " << x.getMonth(); 
 cout << "\n Charges (before tax):\n"; 
 cout << "\n Total cellular charges: $" << x.calcCell(); 
 cout << "\n Total regular telephone charges: $" << x.calcReg(); 
 cout << "\n Total amount past due: $" << x.getPast();
 x.checkPastDute(); 
 cout << "\n Total Amount Charge: $" << x.calcTotal(); 
 cout << "\n";

 return 0;
} 
