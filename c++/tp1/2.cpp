#include <iostream>
using namespace std;
/*Contar la cantidad de números negativos leídos desde teclado. La serie termina con el valor cero (0), el cual no
debe procesarse. ¿Qué cambiaría si debiera procesarse también el último número ingresado (0)?*/

int main(){
    int num, cant=0; 
    cout<<"ingrese un numero entero: " << endl;
    cin>>num;
    while(num!=0){
        if(num<0){
            cant++;
        }
        cout<<"ingrese un numero entero: " << endl;
        cin>>num;
    }
    cout<<cant<<endl;
    return 0;

}