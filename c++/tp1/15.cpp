#include <iostream>
#include <string>
using namespace std;

int cantidadVocales(string cadena){//cuenta la cantidad de vocales
    int vocales=0;
    for(int i=0; i < cadena.length(); i++){
        char letra = tolower(cadena[i]);//transformo la letra a minuscula
        switch (letra)
        {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            vocales++;
        }

    }
    return vocales;
}

int contar(string cadena, char caracter){//cuenta cantidad de caracteres
    int contadorcarac=0;
    
    for(int i=0;i<cadena.length(); i++){
        
        if (cadena[i]==caracter)
            contadorcarac++;
    return contadorcarac;
    }
}

void caracteresPares(string cadena){//mastrar caracters en posiciones pares
    for(int i=0;i<cadena.length();i++){
        if(i%2==0)
            cout<<cadena[i]<<" ";

    }

}



int main() {
    int opcion;
    do {
        string cadena;
        cout << "Ingresar frase: ";
        getline(cin>>ws, cadena);
        cout << "MENÚ: " << endl;
        cout << "1. Cantidad total de vocales (mayúsculas y minúsculas)." << endl;
        cout << "2: Contar cuántas veces aparece un carácter." << endl;
        cout << "3: Mostrar caracteres en posiciones (índice) pares." << endl;
        cout << "0: Salir." << endl;
        cout << "Opción elegida: ";
        cin >> opcion;
        switch (opcion) {
            case 1:
                cout << "Cantidad de vocales: " << cantidadVocales(cadena) << endl;
                break;
            case 2:
                cout << "Ingresar carácter a contar: ";
                char caracter;
                cin >> caracter;
                cout << "Cantidad encontrada: " << contar(cadena, caracter) << endl;
                break;
            case 3:
                caracteresPares(cadena);
                cout << endl;
                break;
            case 0:
                break;
            default:
                cout << "Opción no válida" << endl;
                break;
        }
    } while (opcion != 0);
}