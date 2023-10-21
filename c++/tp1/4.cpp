#include <iostream>
using namespace std;


//Escribir un programa que, dado un número (entero largo) expresado en segundos, informe el equivalente en
//horas, minutos y segundos

int main(){
    long int num;
    cout<<"ingrese un numero: ",cin>>num;
    int seg = num%60;
    int min=(num/60)%60;
    int hora=(num/60/60);
    cout<<"Horas: "<<hora<<endl;
    cout<<"Minutos: "<<min<<endl;
    cout<<"Segundos: "<<seg<<endl;
    return 0;
}