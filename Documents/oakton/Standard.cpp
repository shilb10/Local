/**
 * Jay Patel
 * CS 255
 * 6/28/2014
 **/

#include <iostream> 
#include <math.h>
using namespace std; 
 
class Standard { 
public: 
 //data members 
 double data[100]; 
 double count, mean, sigma, sum, variance; 
 
 //default constructor to initialize variables 
 Standard() { 
 count = 0; 
 mean = 0; 
 sigma = 0; 
 sum = 0; 
 variance = 0; 
 } 
 void getData(double dataArray[100])//accessor function 
 { 
 for(int i = 0; i < count; i++) 
 { 
 data[i] = dataArray[i]; 
 } 
 } 
 void setCount(int c)//accessor for the count 
 { count = c; } 
 double getCount()//mutator for the count value 
 { return count; } 
 
 double MeanValue() 
 { 
 for(int i = 0; i < count; i++) 
 { 
 sum += data[i]; 
 } 
 mean = sum / count; 
 return mean; 
 } 

 double Variance() {
 	double sum = 0;
 	for(int i = 0; i < count; i++) {
 		sum += pow(data[i] - mean, 2)/count;
 	}
 	variance = sum;
 	return variance;
 }

 double StandardDeviation(){
 	return sqrt(Variance());
 }
 }; 

int main() 
{ 
 //declare a data array 
 double MyData[] = {10, 20, 30, 40, 50, 65, 70, 75}; 
 int size = 0; 
 
 //declare a class object 
 Standard s; 
 
 //inform the class of the data array length 
 s.setCount(sizeof(MyData) / sizeof(double)); 
 s.getCount(); 
 s.getData(MyData); 
 
 cout << "welcome to the standard deviation program\n" << endl;

 cout << "Given Data Set: {10, 20, 30, 40, 50, 65, 70, 75}" << endl;

 cout << endl;

 //compute the mean value 
 cout << "mean value is: " << s.MeanValue() << endl; 
 cout << "variance value is: " << s.Variance() << endl;
 cout << "standard deviation value is: " << s.StandardDeviation() << endl;

cout << endl;
 cout << "thank you for visiting the standard deviation program" << endl;
 
 return 0; 
}//end main 
