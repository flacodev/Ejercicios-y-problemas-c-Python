#include <iostream>

using namespace std;

//Leer una secuencia de caracteres que finaliza con la letra minúscula 'n', la cual debe ser procesada. Contabilizar
//la cantidad de cada una de las letras vocales minúsculas. También informar la cantidad de caracteres leídos en
//total y el porcentaje de letras vocales minúsculas encontradas en la secuencia.
int main() {
    char caracter;
    int caracteres_totales, cant_vocales, a, e, i, o, u;
    a=0;e=0;i=0;o=0;u=0;
    do
    {
        cout<<"ingrese un caracter(´n´ fin):"<< endl;
        cin>>caracter;
        caracteres_totales+=1;
        switch (caracter)
        {
        case 'a':
            a+=1;
            break;
        case 'e':
            e+=1;
            break;
        case 'i':
            i+=1;
        case 'o':
            o+=1;
            break;
        case 'u':
            u+=1;
            break;
        case 'n':
            break;
        default:
            break;
        }

    } while (caracter!='n');
    cant_vocales=a+e+i+o+u;
    float porcentaje=((cant_vocales*100)/caracteres_totales);
    cout<<"el porcentaje de vocales es: "<<porcentaje<<endl;
    cout<<"la cantidad de caracteres leidos es: "<< caracteres_totales<<endl;

    return 0;
}
