import turtle
import random
import numpy as np

# Configuración de la ventana del juego
window = turtle.Screen()
window.bgcolor(1, 1, 1)  # Fondo blanco
window.title("Butterfly Game")  # Título de la ventana
window.setup(800, 800)  # Tamaño de la ventana

# Registrar formas de imagen para los objetos del juego
turtle.register_shape('src/butterfly2.gif')
turtle.register_shape('src/flower2.gif')

# Crear la matriz del juego (una cuadrícula 20x20)
GRID_SIZE = 20
game_matrix = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)  # Inicializa una matriz de ceros
# Convenciones de la matriz:
# 0: espacio vacío
# 1: posición de la mariposa
# 2: posición de una flor

class ScoreBoard(turtle.Turtle):
    """
    Clase que representa el marcador del juego.

    Atributos:
        score (int): Puntaje del jugador.

    Métodos:
        update_score: Muestra el puntaje actualizado en la pantalla.
        increase_score: Incrementa el puntaje en 1 y actualiza el marcador.
    """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0, 350)
        self.update_score()

    def update_score(self):
        """Actualiza la pantalla para mostrar el puntaje actual."""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """Incrementa el puntaje en 1 y muestra el nuevo valor en pantalla."""
        self.score += 1
        self.update_score()
        
        # Verificar condición de victoria
        if self.score >= 20:
            self.show_win_message()
            
    def show_win_message(self):
        """Muestra el mensaje de victoria"""
        self.clear()
        self.goto(0, 0)  # Centra el mensaje
        self.write("¡FELICITACIONES!\n¡Has ganado el juego!", 
                align="center", 
                font=("Arial", 36, "bold"))
        window.update()  # Asegura que el mensaje se muestre
        turtle.time.sleep(2)  # Pausa de 3 segundos
        window.bye()  # Cierra la ventana después de la pausa

class Butterfly(turtle.Turtle):
    """
    Clase que representa a la mariposa controlada por el jugador.

    Atributos:
        grid_x (int): Posición x en la matriz del juego.
        grid_y (int): Posición y en la matriz del juego.

    Métodos:
        update_matrix_position: Actualiza la posición de la mariposa en la matriz del juego.
        move_up, move_down, move_left, move_right: Mueve la mariposa en la matriz.
    """
    def __init__(self):
        super().__init__()
        self.shape('src/butterfly2.gif')
        self.penup()
        self.speed(0)
        self.goto(0, 0)
        self.grid_x = GRID_SIZE // 2
        self.grid_y = GRID_SIZE // 2
        self.update_matrix_position()
        
    def update_matrix_position(self):
        """Actualiza la posición de la mariposa en la matriz, eliminando la anterior y estableciendo la nueva."""
        global game_matrix
        game_matrix = np.where(game_matrix == 1, 0, game_matrix)
        game_matrix[self.grid_y][self.grid_x] = 1

    def move_up(self):
        """Mueve la mariposa una celda hacia arriba, si no sale de la matriz."""
        if self.grid_y > 0:
            self.grid_y -= 1
            new_y = self.ycor() + 40
            if new_y < 380:
                self.goto(self.xcor(), new_y)
                self.update_matrix_position()

    def move_down(self):
        """Mueve la mariposa una celda hacia abajo, si no sale de la matriz."""
        if self.grid_y < GRID_SIZE - 1:
            self.grid_y += 1
            new_y = self.ycor() - 40
            if new_y > -380:
                self.goto(self.xcor(), new_y)
                self.update_matrix_position()

    def move_left(self):
        """Mueve la mariposa una celda hacia la izquierda, si no sale de la matriz."""
        if self.grid_x > 0:
            self.grid_x -= 1
            new_x = self.xcor() - 40
            if new_x > -380:
                self.goto(new_x, self.ycor())
                self.update_matrix_position()

    def move_right(self):
        """Mueve la mariposa una celda hacia la derecha, si no sale de la matriz."""
        if self.grid_x < GRID_SIZE - 1:
            self.grid_x += 1
            new_x = self.xcor() + 40
            if new_x < 380:
                self.goto(new_x, self.ycor())
                self.update_matrix_position()

class Flower(turtle.Turtle):
    """
    Clase que representa una flor en el juego.

    Atributos:
        grid_x (int): Posición x en la matriz del juego.
        grid_y (int): Posición y en la matriz del juego.

    Métodos:
        respawn: Reposiciona la flor en una nueva ubicación aleatoria de la matriz.
    """
    def __init__(self):
        super().__init__()
        self.shape('src/flower2.gif')
        self.penup()
        self.speed(0)
        self.grid_x = 0
        self.grid_y = 0
        self.respawn()

    def respawn(self):
        """Reposiciona la flor en una celda vacía de la matriz de juego."""
        global game_matrix
        game_matrix = np.where(game_matrix == 2, 0, game_matrix)
        
        # Encuentra una posición vacía aleatoria en la matriz
        while True:
            self.grid_x = random.randint(0, GRID_SIZE - 1)
            self.grid_y = random.randint(0, GRID_SIZE - 1)
            if game_matrix[self.grid_y][self.grid_x] == 0:
                break
        
        # Actualiza la matriz y la posición en la pantalla
        game_matrix[self.grid_y][self.grid_x] = 2
        screen_x = (self.grid_x - GRID_SIZE // 2) * 40
        screen_y = (GRID_SIZE // 2 - self.grid_y) * 40
        self.goto(screen_x, screen_y)

def check_collision(butterfly, flower):
    """
    Verifica si la mariposa ha colisionado con una flor.

    Parámetros:
        butterfly (Butterfly): Instancia de la clase Butterfly.
        flower (Flower): Instancia de la clase Flower.

    Retorno:
        bool: True si hay una colisión, False de lo contrario.
    """
    return butterfly.grid_x == flower.grid_x and butterfly.grid_y == flower.grid_y

# Lista de flores en el juego
flowers = []

def initialize_game():
    """Inicializa el juego creando instancias de flores y agregándolas a la lista."""
    global flowers
    for _ in range(5):
        new_flower = Flower()
        flowers.append(new_flower)

def print_matrix():
    print("\nGame Matrix:")
    print(game_matrix)

# Crear los objetos de juego
butterfly = Butterfly()
scoreboard = ScoreBoard()
initialize_game()

# Configurar teclas para mover la mariposa
window.listen()
window.onkey(butterfly.move_up, "Up")
window.onkey(butterfly.move_down, "Down")
window.onkey(butterfly.move_left, "Left")
window.onkey(butterfly.move_right, "Right")

# Bucle principal del juego
game_active = True
while game_active:
    window.update()

    # Verifica colisiones entre la mariposa y las flores
    for flower in flowers:
        if check_collision(butterfly, flower):
            flower.respawn()
            scoreboard.increase_score()
            print_matrix()

    turtle.delay(10)