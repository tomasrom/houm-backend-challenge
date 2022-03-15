# Houm Challenge
Houm Backend Software Engineer Challenge

## Indicaciones
- Se utilizo Python 3.8.10
- En el archivo `requirements.txt` estan las librerias y dependencias utilizadas.
- En el archivo `src/main.py` se encuentran las 3 funciones solicitadas en el enunciado.
- Se incluye un script para correr las preguntas e imprimir las respuestas.

## Aclaraciones
- En un entorno de produccion, seria mejor implementar programacion asincronica para que cada funcion se resuelva en paralelo.
- Seria ideal no utilizar la libreria `requests` por el mismo motivo (es bloqueante, en su hilo). Se podria emplear `aiohttp`.