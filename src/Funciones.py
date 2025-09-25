#FUNCIONES

def puntos(diccionario):  
    innovacion = diccionario['innovacion']
    presentacion = diccionario['presentacion']
    errores = diccionario['errores']
 
    Total_puntaje= 3 * innovacion +  1 * presentacion -(1 if errores else 0)
    Total_innovacion = innovacion 
    Total_presentacion = presentacion
    Total_errores = 1 if errores else 0   # si hay error suma 1, si no, suma 0
    return Total_puntaje, Total_innovacion, Total_presentacion, Total_errores

#---------------------------PROCESAR RONDAS--------------------------------------


def procesar_rondas(evaluaciones, puntos):
    totales_acumulados = {} # creamos diccionarios
    puntos_ronda_ganada = {} #creamos diccionarios
    rondas = [] # creamos lista para cada  ronda

    nro = 1  # contador manual de ronda
    for ronda in evaluaciones:
        datos_tabla = []
        for equipo, datos in ronda.items():
            puntaje, innovacion, presentacion, errores = puntos(datos)
            if equipo not in totales_acumulados:
                totales_acumulados[equipo] = {"Innovacion":0, "Presentacion":0, "Errores":0, "Pu
            if equipo not in puntos_ronda_ganada:
                puntos_ronda_ganada[equipo] = 0

            totales_acumulados[equipo]["Innovacion"] += innovacion
            totales_acumulados[equipo]["Presentacion"] += presentacion
            totales_acumulados[equipo]["Errores"] += errores
            totales_acumulados[equipo]["Puntaje"] += puntaje

            datos_tabla.append({
                "Equipo": equipo,
                "Innovacion": innovacion,
                "Presentacion": presentacion,
                "Errores": errores,
                "Puntaje": puntaje
            })

        max_puntaje = max(map(lambda p: p["Puntaje"], datos_tabla))
        ganadores = list(map(lambda p: p["Equipo"], filter(lambda p: p["Puntaje"] == max_puntaje
        for g in ganadores:
            puntos_ronda_ganada[g] += 1
        for fila in datos_tabla:
            fila['Ganador'] = 1 if fila['Equipo'] in ganadores else 0

        rondas.append((nro, datos_tabla, ganadores, max_puntaje))
        
        nro += 1  # incrementamos el contador manual de ronda


    datos_totales = []
    for equi in totales_acumulados:
       fila = {
        "Equipo": equi,
        "Innovacion": totales_acumulados[equi]["Innovacion"],
        "Presentacion": totales_acumulados[equi]["Presentacion"],
        "Errores": totales_acumulados[equi]["Errores"],
        "Puntaje": totales_acumulados[equi]["Puntaje"],
        "Rondas Ganadas": puntos_ronda_ganada.get(equi, 0)
    }
       datos_totales.append(fila)
    
    datos_ordenados = sorted(datos_totales, key=lambda x: x["Puntaje"], reverse=True)
    return rondas, datos_ordenados

 #----------------------------------------IMPRIMIR LAS TABLAS-----------------------------------

def imprimir_guardar_resultados(rondas, datos_ordenados):
    with open("resultado_final.txt", "r") as f:
        # --- Imprimir y guardar cada ronda ---
        for ronda_info in rondas:
            nro, datos_tabla, ganadores, max_puntaje = ronda_info
            print(f"\nRonda {nro} - Mejor equipo: {ganadores} ({max_puntaje} puntos)")
            print(f"{'Equipo':<8} {'Innovacion':<11} {'Presentacion':<13} {'Errores':<7} {'Punta
            print("-"*62)
            f.write(f"\nRonda {nro} - Mejor equipo: {ganadores} ({max_puntaje} puntos)\n")
            f.write(f"{'Equipo':<8} {'Innovacion':<11} {'Presentacion':<13} {'Errores':<7} {'Pun
            f.write("-"*62 + "\n")

            for fila in datos_tabla:
                print(f"{fila['Equipo']:<8} {fila['Innovacion']:^11} {fila['Presentacion']:^13} 
                      f"{fila['Errores']:^7} {fila['Puntaje']:^7} {fila['Ganador']:^7}")
                f.write(f"{fila['Equipo']:<8} {fila['Innovacion']:^11} {fila['Presentacion']:^13
                        f"{fila['Errores']:^7} {fila['Puntaje']:^7} {fila['Ganador']:^7}\n")

        # --- RESULTADO FINAL ---
        print("\nRESULTADO FINAL")
        print(f"{'Pos':<4} {'Equipo':<8} {'Innovacion':<11} {'Presentacion':<13} "
              f"{'Errores':<7} {'Puntaje':<7} {'Rondas Ganadas':<14}")
        print("-"*75)
        f.write("\nRESULTADO FINAL\n")
        f.write(f"{'Pos':<4} {'Equipo':<8} {'Innovacion':<11} {'Presentacion':<13} "
                f"{'Errores':<7} {'Puntaje':<7} {'Rondas Ganadas':<14}\n")
        f.write("-"*75 + "\n")

        pos = 1 # incrementamos el contador manual
        for fila in datos_ordenados:
            print(f"{pos:<4} {fila['Equipo']:<8} {fila['Innovacion']:^11} "
                  f"{fila['Presentacion']:^13} {fila['Errores']:^7} "
                  f"{fila['Puntaje']:^7} {fila['Rondas Ganadas']:^14}")
            f.write(f"{pos:<4} {fila['Equipo']:<8} {fila['Innovacion']:^11} "
                    f"{fila['Presentacion']:^13} {fila['Errores']:^7} "
                    f"{fila['Puntaje']:^7} {fila['Rondas Ganadas']:^14}\n")
            pos += 1


#-------------------------------------FIN---------------------------------------------------
