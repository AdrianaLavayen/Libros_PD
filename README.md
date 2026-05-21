## **Gestor de Libros** - Patrones de Diseño
Sistema de Gestión de Libros es un registro personal de libros que nos permite llevar 
un registro o control de las lecturas realizadas.

## Patrones Creacionales
- **Builder**
      Permite construir un libro paso a paso sin pasar todos los parametros a la vez. Cada
      método set_() asigna un atributo y retorna self para poder encadenar métodos. Al final
      build() delega la creación.
- **Factory Method**
      Decide que tipo de libro se crea dependiendo si proporcionamos saga o no. Nunca se crea
      un LibroIndependiente o LibroSaga directamente. (Si tiene saga crea LibroSaga, de lo
      contrario será LibroIndependiente).
## Patrones Estructurales
- **Decorator**
      Agrega la puntuación y reseña, sin modificar la clase original. Solo posemos aplicarlo
      con los libros ya terminados.
## Patrones de comportamiento 
- **Observer** 
      Cuando un libro es marcado como terminado, el registro notifica automaticamente a todos
      los observaores suscritos.

## Como correrlo
1. Tener python 3 instalado
2. Correr el archivo: python GestorLibros.py
