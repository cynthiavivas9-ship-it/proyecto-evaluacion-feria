def puntos(diccionario):  
    innovacion = diccionario['innovacion']
    presentacion = diccionario['presentacion']
    errores = diccionario['errores']
 
    Total_puntaje= 3 * innovacion +  1 * presentacion -(1 if errores else 0)
    Total_innovacion = innovacion 
    Total_presentacion = presentacion
    Total_errores = 1 if errores else 0   # si hay error suma 1, si no, suma 0
    return Total_puntaje, Total_innovacion, Total_presentacion, Total_errores