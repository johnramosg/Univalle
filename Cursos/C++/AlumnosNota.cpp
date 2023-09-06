#include <iostream>
using namespace std;

int main()
{
  float n1, n2, n3, n4, media = 0;
  cout << "Digite la nota del primer alumno: ";
  cin >> n1;
  cout << "Digite la nota del segundo alumno: ";
  cin >> n2;
  cout << "Digite la nota del tercer alumno: ";
  cin >> n3;
  cout << "Digite la nota del cuarto alumno: ";
  cin >> n4;
  media=(n1+n2+n3+n4)/4;
  cout<<"La media es: "<<media;
  
  return 0;
}