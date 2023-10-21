//Cargar un arreglo con 20 números enteros ingresados por teclado de manera que el arreglo siempre se
//encuentre ordenado en forma ascendente. El arreglo se cargará por completo.
//Hacer tres variantes, suponiendo que el usuario carga los datos de las siguientes formas:
//a) El usuario ingresa los números en orden ascendente.
//b) El usuario ingresa los números en orden descendente.
//c) El usuario ingresa los números sin un orden en particular.

#include <iostream>
using namespace std;
const int MAX=20;

int main() {
    int arreglo[MAX];
    //opcion A
    cout<<"ingrese los valores ordenados de manera ascendente."<< endl;
    for(int i=0; i<MAX; i++){
        cout<<"ingrese el elemento de la posicion "<<i<<endl;
        cin>>arreglo[i];

    }

    //opcion B 

    cout<<"ingrese los valores de manera descendente."<<endl;
    for(int i=MAX-1; i>=0;i--){
        cout<<"ingrese el elemento de la posicion "<<MAX-1<<endl;
        cin>>arreglo[i];

    }

    //opcion C

    int valor; //codigo para hacer un corrimiento en un arreglo!
    for(int i=0; i<MAX;i++){
        cout<<"ingrese el elemento de la posicion "<<i<<endl;
        cin>>valor;
        int indice=0;
        while(indice < i && arreglo[indice] <= valor)
            indice++;

        for (int j=i; j>indice; j--)
            arreglo[j]=arreglo[j-1];
        

        arreglo[indice]=valor;

    }

    return 0;
}