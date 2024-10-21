# Proyecto de Transformaciones LL(1) en Python

Este proyecto en Python implementa transformaciones para convertir gramáticas en formato LL(1), incluyendo eliminación de recursividad por la izquierda, eliminación de factores comunes, y factorización por la izquierda. También incluye una representación de un Árbol de Sintaxis Abstracta (AST).

## Estructura del Proyecto

```plaintext
ll1_transformations/
├── grammar.py
├── ast.py
├── main.py

# Uso del Proyecto de Transformaciones LL(1)

Este documento explica cómo utilizar el proyecto de transformaciones para gramáticas LL(1).

## Requisitos Previos

Asegúrate de tener instalado Python 3. Puedes verificar la instalación ejecutando:

```bash
python3 --version
```

## Ejecución

Para ejecutar el proyecto, sigue estos pasos:

**Abre una terminal**y ejecuta el siguiente comando en la terminal:

   ```bash
   python3 main.py
   ```

## Personalización

Puedes adaptar el proyecto a tus necesidades modificando el diccionario `productions` en el archivo `main.py`. Este diccionario representa las producciones de la gramática que deseas transformar.

### Modificando Producciones

1. **Abre el archivo `main.py`** en un editor de texto.

2. **Busca la variable `productions`**. Debería verse así:

   ```python
   productions = {
       'S': ['A', 'A B'],
       'A': ['aA', 'b'],
       'B': ['bB', 'c']
   }
