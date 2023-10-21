#include <iostream>
using namespace std;
//Escribir un programa que imprima el menú mostrado a continuación y solicite al usuario elegir una opción, la
//cual se debe ejecutar para luego volver a mostrar el menú repetidas veces, hasta que el usuario decida salir:
//‘A’: Invertir número.
//‘B’: Sumatoria de dígitos.
//‘C’: Decir si son múltiplos.
//‘D’: Salir.
//Dependiendo del carácter ingresado por el usuario, realizar la acción indicada en el menú: A: leer un número e
//invertir sus dígitos para luego imprimirlo en orden inverso; B: solicitar un número e imprimir la suma de sus
//dígitos; C: solicitar el ingreso de dos números y decir si el primero es múltiplo del segundo; D: terminar el
//programa.
//Si el usuario ingresa un carácter que no es la opción D, se debe ejecutar lo que corresponda y volver a mostrar
//el menú para permitirle elegir otra opción. Si el carácter ingresado por el usuario no es A, B, C ni D, mostrarle un
//mensaje de error y continuar mostrándole el menú y solicitando una opción hasta que ingrese una que sea válida.
int main() {
    char caracter;
    int numero;
    do
    {
        cout<<"'A' : invertir numero"<<endl;
        cout<<"'B' : invertir numero"<<endl;
        cout<<"'C' : invertir numero"<<endl;
        cout<<"'D' : invertir numero"<<endl;
        
    } while (caracter='D');
switch (caracter)
        {
    case 'A':
    
        numero
    case 'B':
    case 'C':
    case 'D':    
    default:
        break;
        }

     

    return 0;
}