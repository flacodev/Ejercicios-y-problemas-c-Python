#include <iostream>
#include <string>
using namespace std;

//Realizar un algoritmo que almacene información de, como máximo, 500 libros en un arreglo estático. Un libro
//se define como un struct con los siguientes campos: titulo, autor, ISBN, editorial, cantidadHojas. El algoritmo
//finaliza luego de cargar el libro "El hobbit", el cual debe procesarse o cuando ya no quede espacio en el arreglo
//(lo que suceda primero). Finalmente, imprimir el arreglo resultante mostrando todos los datos de cada libro.


const int df=500;
struct libros{
    string nombreLibro;
    string autor;
    int codigo;
    string editorial;
    int cantidadHojas;
};

int cargarArreglo(libros array[], int dl){
    string nombre, nombreAutor, nombreEditorial;
    do{
        //titulo
        cout<<"Ingrese el titulo: "<<endl;
        getline(cin>>ws, nombre);
        array[dl].nombreLibro = nombre;
        //autor
        cout<<"Ingrese el autor: "<<endl;
        getline(cin>>ws, nombreAutor);
        array[dl].autor = nombreAutor;
        //isbn
        cout<<"ingrese el ISBN: "<<endl;
        cin>>array[dl].codigo;
        //editorial
        cout<<"Ingrese la editorial: "<<endl;
        getline(cin>>ws, nombreEditorial);
        array[dl].editorial = nombreEditorial;
        //cantidad de hojas
        cout<<"ingrese la cantidad de hojas: "<<endl;
        cin>>array[dl].cantidadHojas;
        //incrementar dl para moverse en el array
        dl++;

    }while(nombre != "el hobbit" && dl<= df);

return dl;
}
void imprimirArray(libros array[], int dl){
    for (int i=0; i<=dl ; i++){
        cout<<"titulo: "<<array[i].nombreLibro<<endl;
        cout<<"autor: "<<array[i].autor<<endl;
        cout<<"ISBN"<<array[i].codigo<<endl;
        cout<<"Editorial"<<array[i].editorial<<endl;
        cout<<"cantidad de hojas"<<array[i].cantidadHojas<<endl;
    }
}

int main() {

    libros array[df];
    int dl=0;
    dl=cargarArreglo(array, dl);
    cout<<"imprimir array"<<endl;
    imprimirArray(array,dl);

    return 0;
}