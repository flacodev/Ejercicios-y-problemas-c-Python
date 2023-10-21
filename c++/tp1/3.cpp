#include <iostream>
using namespace std;
//Leer tres letras desde teclado e indicar cuál de ellas viene primero en el alfabeto.

int main(){
    char letra1, letra2, letra3;
    cout<<"ingrese una letra: ",cin>>letra1;
    cout<<"ingrese una letra: ", cin>>letra2;
    cout<<"ingrese una letra: ",cin>>letra3;
    
    if(letra1<letra2 && letra1<letra3){
        cout<<letra1<< endl;
    }else{
        if(letra2<letra3){
            cout<<letra2<< endl;
        }else{
        cout<<letra3<< endl;
    }
    }
return 0;
  
    
}