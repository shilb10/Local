//This program creates student objects 
//and computes their average grade point averages
/*
 * Jay Patel
 * 7/2/2014
 * CS 255
 */  
#include <iostream> 
#include <iomanip> 
using namespace std; 
 
class Student 
{ 
public: 
 int IDNumber; 
 double gpa; 
 
 Student(const int i, const double g); 
 friend double operator+(const Student &, const Student &); 
}; 
Student::Student(const int id, const double g) 
{ 
 Student::IDNumber = id; 
 Student::gpa = g; 
} 
double operator+(const Student &stud1, const Student &stud2) 
{ 
 double sum; 
 sum = stud1.gpa + stud2.gpa; 
 return(sum); 
} 

int main() 
{ 
	Student s1(100, 3.00);
	Student s2(200, 3.75);
	Student s3(300, 3.83);
	Student s4(400, 4.0);
	Student average(0, 0);
 Student students[] = {s1, s2, s3, s4}; 
 int num = 0;
 
 cout << "How many students in average?: ";
 cin >> num;
 cout << endl;
 if (num > 4 || num <= 0)
 {
 	cout << "Not enough students or invalid number" << endl;
 	return 0;
 }
 for (int i = 0; i < num;  i++)
 {
 	average.gpa = average + students[i];
 } 
 average.gpa /= num;
 for (int i = 0; i < num; i++)
 {
 	cout <<  cout << "Student Information:\n"; 
 cout << "ID: " << students[i].IDNumber << " GPA: " << students[i].gpa << endl;
 }
 cout << setiosflags(ios::fixed | ios::showpoint); 
 cout.precision(2); 
 cout << "\nAverage is " << average.gpa << endl; 
 return 0; 
} 
