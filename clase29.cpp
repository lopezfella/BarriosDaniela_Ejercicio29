#include <iostream>
#include <fstream>
#include <cmath>
using namespace std; 

int main(){
  int Nx = 30;
  int D = 1;
  double s = 1.0;
  double dt = 0.1;
  double uo[nx][nt];
  double un[nx][nt];
  double phi_0 = 0;
  double phi_1 = 0;
  double phi_2 = 0;
  double t_0 = 0;
  double x0 = -1.0;
  double xf = 1.0;
  int i, j;
  ofstream outfile;
