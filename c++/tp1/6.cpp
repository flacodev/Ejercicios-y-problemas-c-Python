#include <iostream>
using namespace std;

int main(){

    float num;
    float armonica=1;
    float suma;
    float sumatotal;
    cout<<"ingrese un numero: ";
    cin>>num;
    while(armonica!=num+1){
        suma=1/armonica;
        armonica+=1;
        sumatotal+=suma;
    }
    cout<<sumatotal<<endl;
    return 0;
}
