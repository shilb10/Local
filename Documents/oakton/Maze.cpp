/**
 * Jay Patel
 * CS 255
 * 07/19/2014
 **/

#include <iostream> 
#include <string> 
using namespace std; 
 
struct cell 
{ 
 int cellNumber; 
 bool up , down; 
 bool left, right; 
 bool checked; 
}; 
 
int main() 
{ 
 int end = 15; 
 cell maze[4][4]; 
 
 cell myCell1 = {1, false, false, false, true, false}; 
 maze[0][0] = myCell1; 
 
 cell myCell2 = {2, false, true, true, false, false}; 
 maze[0][1] = myCell2; 
 
 cell myCell3 = {3, false, false, false, true, false}; 
 maze[0][2] = myCell3; 
 
 cell myCell4 = {4, false, true, true, false, false}; 
 maze[0][3] = myCell4; 
 
 cell myCell5 = {5,false, false, false, true, false}; 
 maze[1][0] = myCell5; 
 
 cell myCell6 = {6, true, true, true, true, false}; 
 maze[1][1] = myCell6; 
 
 cell myCell7 = {7, false, false, true, true, false}; 
 maze[1][2] = myCell7; 
 
 cell myCell8 = {8, true, true, true, false, false}; 
 maze[1][3] = myCell8; 
 
 cell myCell9 = {9,false, true, false, true, false}; 
 maze[2][0] = myCell9; 
 
 cell myCell10 = {10, true, false, true, false, false}; 
 maze[2][1] = myCell10; 
 
 cell myCell11 = {11, false, true, false, true, false}; 
 maze[2][2] = myCell11; 
 
 cell myCell12 = {12, true, true, true, false, false}; 
 maze[2][3] = myCell12; 
 
 cell myCell13 = {13, true, false, false, true, false}; 
 maze[3][0] = myCell13; 
 
 cell myCell14 = {14, false, false, true, false, false}; 
 maze[3][1] = myCell14; 
 
 cell myCell15 = {15, true, false, false, false, false}; 
 maze[3][2] = myCell15; 
 
 cell myCell16 = {16, true, false, false, false, false}; 
 maze[3][3] = myCell16; 
 
 int i = 0; 
 int x = 0; 
 int y = 1; 
 int solutionPath[20] = {0}; 
 int xpath[20]; 
 int ypath[20]; 
 
 int programPath[20] = {0}; 
 int s = 0; 
 
 while(maze[y][x].cellNumber != end) 
{
 if(maze[y][x].right && !maze[y][x+1].checked) 
 { 
 solutionPath[i] = maze[y][x].cellNumber; 
 xpath[i] = x; 
 ypath[i] = y; 
 maze[y][x].checked=true; 
 programPath[s] = maze[y][x].cellNumber; 
 cout << "Moved to " << programPath[s] << endl;
 s++; 
 x++; 
 i++; 
 } 
 else if(maze[y][x].down && !maze[y+1][x].checked) 
 { 
 solutionPath[i] = maze[y][x].cellNumber; 
 xpath[i] = x; 
 ypath[i] = y; 
 maze[y][x].checked = true; 
 programPath[s] = maze[y][x].cellNumber;
 cout << "Moved to " << programPath[s] << endl; s++; 
 y++; 
 i++; 
 } 
 
 else if(maze[y][x].left && !maze[y][x-1].checked) 
 { 
 solutionPath[i] = maze[y][x].cellNumber; 
 xpath[i] = x; 
 ypath[i] = y; 
 maze[y][x].checked = true; 
 programPath[s] = maze[y][x].cellNumber; 
 cout << "Moved to " << programPath[s] << endl; s++; 
 x--; 
 i++; 
 } 
 
 else if(maze[y][x].up && !maze[y-1][x].checked) 
 { 
 solutionPath[i] = maze[y][x].cellNumber; 
 xpath[i] = x; 
 ypath[i] = y; 
 maze[y][x].checked = true; 
 programPath[s] = maze[y][x].cellNumber; 
 cout << "Moved to " << programPath[s] << endl;
 s++; 
 y--; 
 i++; 
 } 
 else 
 { 
 maze[y][x].checked = true; 
 solutionPath[i] = 0; 
 programPath[s] = maze[y][x].cellNumber; 
 cout << "Moved to " << programPath[s] << endl;
 s++; 
 x = xpath[i-1]; 
 y = ypath[i-1]; 
 i--; 
 } 
 } 
 programPath[s] = maze[y][x].cellNumber;
 cout << "Moved to " << programPath[s] << endl; 
 solutionPath[i] = maze[y][x].cellNumber; 
 cout << "\n solution path is: \n"; 
 i = 0; 
 while(solutionPath[i] != 0) 
 { 
 cout << " " << solutionPath[i]; 
 i++; 
 } 
 
 cout << "\n actual program path: \n"; 
 i = 0; 
 
 while(programPath[i] != 0) 
 { 
 cout << " " << programPath[i]; 
 i++; 
 } 
 cout << "\n"; 
 
 return 0; 
}
