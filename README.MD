# Sistema de Evaluación de Proyectos Estudiantiles

Sistema desarrollado para procesar y analizar datos de evaluación de una feria de ciencias escolar, generando rankings de equipos participantes a través de múltiples rondas.

## Descripción del Proyecto

Este programa procesa datos estructurados de evaluaciones de equipos estudiantiles, calculando puntajes basados en criterios de innovación, presentación y penalizaciones por errores. El sistema genera rankings por ronda y resultados finales acumulados, además de guardar los resultados en un archivo de texto.

### Fórmula de Cálculo de Puntajes

- *+3 puntos* por cada punto en innovación  
- *+1 punto* por cada punto en presentación  
- *-1 punto* si el equipo tuvo errores graves (`errores=True`)
