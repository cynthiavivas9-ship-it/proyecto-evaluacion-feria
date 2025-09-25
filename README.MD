# Sistema de Evaluación de Proyectos Estudiantiles

Sistema desarrollado para procesar y analizar datos de evaluación de una feria de ciencias escolar, generando rankings de equipos participantes a través de múltiples rondas.

## Descripción del Proyecto

Este programa procesa datos estructurados de evaluaciones de equipos estudiantiles, calculando puntajes basados en criterios de innovación, presentación y penalizaciones por errores. El sistema genera rankings por ronda y resultados finales acumulados, además de guardar los resultados en un archivo de texto.

### Fórmula de Cálculo de Puntajes

- *+3 puntos* por cada punto en innovación  
- *+1 punto* por cada punto en presentación  
- *-1 punto* si el equipo tuvo errores graves (`errores=True`)

proyecto_evaluacion/
├── README.md                    # Documentación del proyecto
├── src/                        # Código fuente
│          
│   └── Funciones.py            # Funciones principales del sistema
└── notebooks/                  # Notebooks de Jupyter
    └── Rondas.ipynb  # Notebook principal para ejecutar

### Cómo Ejecutar el Programa
Opción 1: Usando Jupyter Notebook (Recomendado)

Opción 2: Desde Python directamente



### Funciones Principales
#### puntos(diccionario)

Entrada: Diccionario con claves 'innovacion', 'presentacion', 'errores'
Salida: Tupla (Total_puntaje, Total_innovacion, Total_presentacion, Total_errores)
Funcionalidad: Calcula el puntaje de un equipo según la fórmula establecida

#### procesar_rondas(evaluaciones, puntos)

Entrada: Lista de diccionarios con datos de todas las rondas
Salida: Tupla (rondas, datos_ordenados)
Funcionalidad: Procesa todas las rondas, genera estadísticas acumuladas y ranking final ordenado por puntaje


#### imprimir_guardar_resultados(rondas, datos_ordenados)

Entrada: Resultados de todas las rondas y ranking acumulado
Salida: Imprime resultados en consola y los guarda en el archivo resultado_final.txt
Funcionalidad: Muestra tabla de cada ronda y tabla de resultados finales

### Estructura de Datos
totales_acumulados (interno en procesar_rondas)
datos_ordenados (resultado final)


============================================================
       
               Resultados de la Feria de Ciencias
============================================================

Ronda 1 - Mejor equipo: ['EquipoA'] (6 puntos)
Equipo    Innovacion   Presentacion   Errores   Puntaje   Ganador
--------------------------------------------------------------
EquipoA         2             1           1        6        1
EquipoB         1             0           0        3        0
...

RESULTADO FINAL
Pos  Equipo    Innovacion   Presentacion   Errores   Puntaje   Rondas Ganadas
---------------------------------------------------------------------------
1    EquipoA        8            10           2        32          2
2    EquipoC        7             6           3        27          1






### Archivos del Proyecto

src/Funciones.py: Contiene todas las funciones principales del sistema

notebooks/evaluacion_feria.ipynb: Notebook ejecutable con el análisis completo

README.md: Documentación del proyecto

resultado_final.txt: Archivo generado con resultados completos


