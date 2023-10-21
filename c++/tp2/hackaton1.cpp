#include <iostream>
#include <string>
using namespace std;

string simbolo(string cadena, char caracter){ //esta funcion nos permite reemplazar los espacios por el simbolo elegido
    int a=cadena.length(); //declaramos la variable 'a' ya que nos daba un error al momento de recorrer la cadena
    for(int i=0; i < a; i++){
        if (cadena[i]==' '){//de esta manera logramos evaluar el caracter en la posicion de 'i' y si esta misma es igual a un espacio 
            cadena[i]=caracter;//reemplaza la posicion de 'i' por el simbolo ingresado por el usuario
        }
    }
    
    return cadena; 
}

int ContadorDePalabras(string cadena, char letra){//esta funcion cuenta la cantidad de palabras que hay en la cadena que comienzan con la letra elegida
    string cadena1=' '+cadena;//esto para crear una nueva cadena que empieze con un espacio, ya que, nosotros decidimos trabajar evaluando los espacios de la cadena y asi distinguir las palabras
    int cantPalabras=0;
   int a=cadena1.length(); //declaramos la variable 'a' ya que nos daba un error al momento de recorrer la cadena
    for(int i=0; i < a; i++){
        if (cadena1[i]==' '){ //se encarga de buscar un espacio en la cadena
            if (cadena1[i+1]==letra){//si encuentra un espacio, evalua el caracter siguiente
            cantPalabras++;
            }
        }
    }

    return cantPalabras;

}

int main() {
    int opcion;
    string cadena;
    char caracter;
    char letra;
    do {//creacion del menu
        cout << "*** Letras y Símbolos ***: " << endl;
        cout << "[1]: SIMBOLO ." << endl;
        cout << "[2]: LETRA " << endl;
        cout << "[0]: Salir." << endl;
        cout <<"Seleccione una opcion: ";
        cin>>opcion;
       switch (opcion) {//utilizamos un switch para seleccionar la opcion del menu elegida
       case 1:
        cout<<"Ingrese una frase: ";
        getline(cin>>ws, cadena);
        cout<<"Ingrese un simbolo: ";
        cin>>caracter;
        cout<<"frase convertida: "<<simbolo(cadena,caracter)<<endl;
        break;
       case 2:
        cout<<"Ingrese una frase: ";
        getline(cin>>ws, cadena);
        cout<<"Ingrese un letra: ";
        cin>>letra;
        cout<<"Resultado: "<<ContadorDePalabras(cadena,letra)<<" Palabra/s comienza/n con la letra: "<<letra<<endl;


       default:
        break;
       }
        
    } while (opcion != 0);



    return 0;
}

//decidimos utilizar un do while para que el menu trabaje hasta que el usuario lo desee. 
//luego utilizamos un swtich para poder seleccionar cada opcion del mismo.
//dentro de cada funcion utilizamos un for para poder recorrer la cadena ingresada
//para lograr el desafio nos basamos en ejercicios realizados en las clases de practica y material teorico de la plataforma