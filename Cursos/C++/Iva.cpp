//Escribe un programa que lea de la entrada estandar el precio de un producto y muestre en la salida estandar el precio del producto al aplicarle el iva
#include<iostream>

using namespace std;

int main(){
  int precio;
  float poriva;
  float iva;
  cout<<"Digite el precio del producto: ";
  cin>>precio;
  cout<<"Digite el porcentaje del iva: ";
  cin>>poriva;
  iva=precio+(precio*(poriva/100));
  cout<<"\nEl precio del producto al aplicarle el IVA es: "<<iva<<" Pesos"<<endl;

  return 0;
}