# Tarea Técnica - Ruuf 

Este repositorio contiene la solución al ejercicio técnico solicitado por el equipo de Ruuf, donde se debía calcular cuántos paneles solares caben en un techo rectangular, considerando rotaciones.

---

## Descripción del problema

Dado un panel solar de dimensiones `a × b` y un techo de dimensiones `x × y`, la tarea consiste en determinar cuántos paneles pueden colocarse dentro del techo, permitiendo rotar los paneles para maximizar la cantidad total.

Ejemplos proporcionados por Ruuf:

- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## Solución

La solución implementa una función llamada `calculate_panels` que prueba diferentes formas de colocar los paneles:

- Prueba todas las posiciones posibles con paneles sin rotar.
- Calcula si en el espacio restante se pueden colocar paneles rotados.
- Repite el proceso invirtiendo las dimensiones (como si se rotaran todos los paneles).
- Devuelve el máximo entre ambas estrategias.

Se incluyeron comentarios y pruebas para validar la lógica.

---

##  Estructura del proyecto
