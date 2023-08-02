
#include<iostream>
using namespace std;

int main(){
  int n1,n2,suma=0,resta=0,multiplicacion=0,division=0;
  cout<<"Digite un número: ";cin>>n1;
  cout << "Digite un número: ";
  cin >> n2;
  suma=n1+n2;
  resta=n1-n2;
  multiplicacion=n1*n2;
  division=n1/n2;
  cout << "\nEl resultado de la suma es: "<<suma<<endl;
  cout << "\nEl resultado de la resta es :" << resta << endl;
  cout << "\nEl resultado de la multiplicación es: " << multiplicacion << endl;
  cout << "\nEl resultado de la división es: " << division << endl;
}