# Petal Path Game

Este es un juego simple desarrollado en Python usando la librería `turtle`, donde controlas una mariposa que debe recolectar flores en una cuadrícula de 20x20. Cada vez que la mariposa recolecta una flor, el puntaje aumenta, y la flor aparece en una nueva posición aleatoria.

## Requisitos

- Python 3.x
- Librerías adicionales: `turtle`, `random`, `numpy`

## Estructura del Código

- **Butterfly**: La mariposa que el jugador controla con las teclas de flecha.
- **Flower**: Flores que aparecen en posiciones aleatorias y que la mariposa debe recolectar.
- **ScoreBoard**: Marcador que muestra el puntaje del jugador en la ventana.
- **game_matrix**: Matriz de 20x20 que representa la cuadrícula del juego.

## Cómo Jugar

1. Ejecuta el archivo del juego.
2. Usa las flechas de dirección para mover la mariposa en la cuadrícula.
3. Cada vez que la mariposa recoja una flor, el puntaje aumentará y la flor se reposicionará aleatoriamente.

## Archivos de Imagen

El juego requiere dos imágenes en la carpeta `src/`:
- `butterfly2.gif`: Imagen para la mariposa.
- `flower2.gif`: Imagen para las flores.

Asegúrate de que estas imágenes existan y estén en el formato `.gif` compatible con `turtle`.