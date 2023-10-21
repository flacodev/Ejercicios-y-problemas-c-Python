//Suponer que esperamos que los elementos de un arreglo estén ordenados de menor a mayor (de modo que
//cada elemento es menor o igual que el siguiente: a[0] <= a[1] <= a[2] …)
//Sin embargo, para estar seguros queremos probar el arreglo usando una función que informe si encuentra que
//algún elemento no está en orden (retornando su índice en caso de ser así, o retornando -1 si todo el arreglo
//está ordenado). Se supone que el siguiente código realiza esa prueba, pero contiene un error muy usual cuando
//se trabaja con arreglos, ¿en qué consiste?

int en_desorden (double arreglo[], int dimension){
for (int indice = 0; indice < dimension; indice++) {//para solucionarlo deberiamos poner dimension-1
if (a[indice] > a[indice + 1]) {// el error esta que cuando hacemos indice + 1 nos caemos fuera del arrelgo
return indice + 1;
}
return -1;
}}