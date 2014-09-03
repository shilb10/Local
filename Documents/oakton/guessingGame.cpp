/**
 * Jay Patel
 * CS 255
 * 7/5/2104
 **/
#include <iostream> 
#include <stdlib.h> //Header file for call to functions RAND, SRAND 
#include <time.h> //Header file for call to TIME function 
using namespace std; 
 
void guessingGame(void); 
 
int main(void) 
{ 
 srand(time(NULL)); 
 guessingGame(); 
 return 0; 
} 
 
void guessingGame(void) 
{ 
 int x, guess, response; 
 
 do { 
 
 //assign an integer value to variable x that is in the range of 1 to 20 
 x = 1 + rand() % 20; 

cout << endl << "Welcome: the guessing game. \n I have a number from 1 " 
 << "and 20." << endl << "Can you guess it?" << endl 
 << "Please type your first guess." << endl << "? "; 
 cin >> guess; 
 
 // Complete the while loop condition to allow the user to continue and 
 // input another guess if necessary 
 
 while (guess != x) { 
 
 if (guess < x ) 
 
// Complete cout statements that tell the user if they are too high or 
// too low 
 cout << "Too low" << endl; 
 else 
 cout << "Too high" << endl;; 
 
 cin >> guess; 
 } 
 cout << endl << "Great job - you guessed the correct number!" << endl 
 << "Would you like to try again?" << endl << "Please type " 
 << "(1 = yes, 2 = no)? "; 
 cin >> response; 
 
 } //complete the while condition to allow the user to play again 
 while (response == 1); 
 } 
 
