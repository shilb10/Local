#include <iostream> 
#include <string> 
using namespace std; 
 
class Linear { 
 
 private: 
 float cost, rate, time, salvage; 
 string type; 
 
 public: 
 
 Linear() { 
 cost = 0; 
 rate = 0; 
 time = 0; 
 salvage = 0; 
 type = ""; 
 } //constructor 
 
 void setValues(); 
 //allows the user to input values for the asset 
 
 string getType() { return type; } 
 //returns the asset name / type 
 double getRate() { return rate; } 
 //returns the depreciation rate 
 float getDepreciation() { return cost * rate; } 
 //returns the annual depreciation expense 
 float getBookValue() 
 { return (cost - salvage) - getDepreciation(); } 
 //returns the book value of the asset 
 bool Monitor() { return (getBookValue() > salvage); } 
 //compares the book value to the salvage value 
 //returns 1 if book value > salvage, 0 if book value < salvage 
 float getDepreciable(){ return cost-salvage;}
}; 
 
void Linear::setValues() { 
 cout << "Asset Type: "; 
 cin >> type; 
 cout << "Asset Cost: "; 
 cin >> cost; 
 cout << "Asset Life (years): "; 
 cin >> time; 
 cout << "Salvage Value: "; 
 cin >> salvage; 
 
 rate = (cost - salvage) / (cost * time); 
} 
 
int main() 
{ 
 Linear asset; 
 
 asset.setValues(); 
 
 cout << endl << endl << asset.getType() << " Report:\n"; 
 cout << "Depreciable Amount: " << asset.getDepreciable() << endl;
 cout << "Depreciation Rate: " << asset.getRate() * 100 
 << "%" << endl; 
 cout << "Annual Depreciation Expense: $" << asset.getDepreciation() << ".00"
 << endl; 
 cout << "Book Value: $" << asset.getBookValue() << ".00" << endl; 
 if(asset.Monitor() == 0) 
 cout << "Warning: Book value of " << asset.getType() 
 << " has fallen below the salvage value." << endl; 
 return 0; 
} 
