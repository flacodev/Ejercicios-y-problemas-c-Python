//La universidad posee información histórica sobre los estudiantes (no más de 1000) de una materia
//determinada. De cada uno almacena: nombre y apellido, legajo, cantidad de inasistencias a clase, calificación
//obtenida. Almacenar esta información en un arreglo de structs. Se pide:
//d) Imprimir nombre y apellido de los alumnos que tuvieron más de 5 inasistencias.
//e) Imprimir número de legajo de los alumnos cuya calificación promedio sea mayor o igual a la calificación
//promedio total (requiere calcular un promedio de las calificaciones de todos los alumnos en el listado).
//f) Imprimir el número de legajo de aquellos alumnos que tienen promedio mayor o igual a nueve.
//g) Dado el legajo de un alumno, eliminarlo del listado.
//Nota: analizar si es posible reutilizar código en más de uno de los incisos.

#include <iostream>
#include <string>
using namespace std;
const int MAX=1000;
struct estudiantes
{
    string nombre;
    string apellido;
    int legajo;
    int cant_inasis;
    float notas;
};

int cargar_alumnos(estudiantes array[], int dl){
    string nombre_estudiante, apellido_estudiante;
    int cant_cargar, contador;
    float notas_estudiante, promedio_estudiante;
    cout<<"cuantos estudiantes desea cargar?: ";cin>>cant_cargar;
    do
    {
        cout<<"Ingrese el nombre: ";
        getline(cin>>ws, nombre_estudiante);
        array[dl].nombre = nombre_estudiante;
        cout<<"Ingrese el apellido: ";
        getline(cin>>ws, apellido_estudiante);
        array[dl].apellido = apellido_estudiante;
        cout<<"ingrese el legajo: ";
        cin>>array[dl].legajo;
        cout<<"ingrese la cantidad de inasistencias: ";
        cin>>array[dl].cant_inasis;
        cout<<"ingrese las notas(-1 para terminar): ";
        cin>>notas_estudiante;
        while (notas_estudiante!= -1){
            notas_estudiante+=notas_estudiante;
            contador++;
            cout<<"ingrese las notas(-1 para terminar): ";
            cin>>notas_estudiante; 
        }
        promedio_estudiante= notas_estudiante/contador;
        array[dl].notas=promedio_estudiante;
        dl++;
        cout<<"alumno cargado!"<<endl;
        cant_cargar--;
    } while ( cant_cargar!=0 && dl<MAX);//terminar
    
    
    return dl;
}

void inasistencias (estudiantes array[], int dl){
    for (int i=0; i<dl; i++){
        if(array[i].cant_inasis > 5){
            cout<<array[i].nombre;
            cout<<" "<<array[i].apellido<<endl;
        }
        else{
            cout<<"No hay estudiantes con mas de 5 inasistencias!"<<endl;
            break;
        };
    }

}
int promedio_total(estudiantes array[], float dl){
    float promedio=0;
    float promedio_total=0;
    for (int i=0; i<dl; i++){
        promedio += array[i].notas;
    };
    promedio_total=promedio / dl;
    return promedio_total;

}

int buen_promedio(estudiantes array[], int dl){
    float promedio_analizar;
    promedio_analizar = promedio_total(array, dl);
    for(int i=0; i<dl ; i++){
        if (array[i].notas>promedio_analizar){
            cout<<array[i].legajo<<endl;
        }
        else{
            cout<<"ningun estudiante supera el promedio total"<<endl;
        }
    }
}

void eliminar_alumno(estudiantes array[], int dl){
    string nombreEliminar, apellidoEliminar;
    cout<<"Ingrese el nombre a eliminar: "; 
    getline(cin>>ws, nombreEliminar);
    cout<<"Ingrese el apellido a eliminar: "; 
    getline(cin>>ws, apellidoEliminar);
    
    for(int i=0; i<=dl; i++){
        int indice=0;
            while (indice < i && array[i].nombre == nombreEliminar && array[i].apellido == apellidoEliminar)
                indice++;
            
            for (int j=i; j>indice; j--)
                array[j]=array[j-1];
    dl--;
    } 
}


int main() {
    estudiantes array[MAX];
    int dl=0;
    int opcion;
    do
    {
        cout << "*** SISTEMA DE ESTUDIANTES: " << endl;
        cout << "[1]: Cargar estudiantes: "<<endl;
        cout << "[2]: alumnos con mas de 5 inasistencias: "<<endl;
        cout << "[3]: alumnos con promedio mayor al promedio total: "<<endl;
        cout << "[4]: eliminar alumno: "<<endl;
        cin>>opcion;
     switch (opcion)
        {
        case 1:
            dl=cargar_alumnos(array, dl);
            break;
        
        case 2: 
            inasistencias(array, dl);

        case 3:
            buen_promedio(array, dl);

        case 4:
            eliminar_alumno(array, dl);
        default:
            break;
        }
    } while (opcion !=0);
    

    return 0;
}