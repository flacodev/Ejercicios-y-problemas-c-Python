#include <iostream>
using namespace std;
//Escribir un programa que lea una fecha en el formato numérico AAAAMMDD y la informe con el formato
//DD/MM/AAAA.
//Precondición: los valores ingresados corresponden a una fecha válida.

int main(){
    long int fecha;
    cout<<"ingrese fecha: ";cin>>fecha;
    int dia=fecha%100;
    fecha/=100;
    int mes=fecha%100;
    int anio=fecha/100;
    cout<<dia<<"/"<<mes<<"/"<<anio << endl;




    return 0;
}