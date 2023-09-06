#include <iostream>
#include<cmath>
using namespace std;
int main()
{
  int a, b, h = 0;
  cout << "Escriba el primer cateto: ";
  cin >> a;
  cout << "Escriba el primer cateto: ";
  cin >> b;
  h=sqrt((a*a)+(b*b));
  cout<<"La hipotenusa es: "<<h<<endl;
}