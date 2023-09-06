#include<iostream>
using namespace std;

int main(){
  float n1,n2,n3,final=0;

  cout<<"Digite la nota de practicas: ";cin>>n1;
  cout << "Digite la nota Teorica: ";
  cin >> n2;
  cout << "Digite la nota de participación: ";
  cin >> n3;

  final=((n1*0.3)+(n2*0.6)+(n3*0.1));
  cout<<"La nota final es: "<<final<<endl;
}