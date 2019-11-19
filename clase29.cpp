#include <iostream>
#include <fstream>
#include <cmath>
using namespace std; 

int main(){
	int Nx = 30;
	int Ntc= 210;
	int D = 1;
	double s = 1.0;
	double dx = 2/Nx;
	double dt = 1/Ntc;
	double phio[Nx][Ntc];
	double phin[Nx][Ntc];
	double phi_0 = 0.0;
	double phi_1 = 0.0;
	double phi_2 = 0.0;
	double t_0 = 0.0;
	double x0 = -1.0;
	double xf = 1.0;
	int i, j;
	ofstream outfile;
	
	outfile.open("datosA.dat");
	for(i=0;i<Nx;i++){
		for(j=0;j<Ntc;j++){
		  phio[i][j]=0.0;
		  if((i>0) && (i<1)){
			if(j==0){
			  phio[i][j] = 0;
			} 
      }
      else{
          phio[i][j] = 1;
      }
    }
  }
	outfile.close();
	
	outfile.open("datosC.dat");
	for(i=1;i<Nx-1;i++){
		for(j=1;j<Ntc;j++){
		  phin[i+1][j] = phio[i][j]+ (dt*D)/(pow(dx,2))*(phio[i][j+1]-2*phio[i][j] + 1*phio[i][j-1])+(dt*s);
    }
  }
	outfile.close();
									  
  outfile.open("datosD.dat");
  for(i=1;i<Nx-1;i++){
    for(j=1;j<Ntc-10;j++){
      phio[i][j] = phin[i][j];
    }
  }
  outfile.open("datosB.dat");
  for(j=0;j<Nx+1;j++){
    for(i=0;i<Ntc;i++){
      outfile << phio[i][j] << endl;
    }
  }
  outfile.close();
  return 0;
}
