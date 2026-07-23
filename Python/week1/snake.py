import tkinter as tk
import random

# Game settings
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20
SPEED = 100  # milliseconds

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.reset_game()

        self.root.bind("<Up>", self.change_direction)
        self.root.bind("<Down>", self.change_direction)
        self.root.bind("<Left>", self.change_direction)
        self.root.bind("<Right>", self.change_direction)

        self.update()

    def reset_game(self):
        self.canvas.delete("all")

        self.direction = "Right"
        self.score = 0

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.spawn_food()

        self.score_text = self.canvas.create_text(
            50, 20, text=f"Score: {self.score}",
            fill="white", font=("Arial", 14)
        )

    def spawn_food(self):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        new_dir = event.keysym

        opposite = {
            "Up": "Down",
            "Down": "Up",
            "Left": "Right",
            "Right": "Left"
        }

        if opposite[new_dir] != self.direction:
            self.direction = new_dir

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= CELL_SIZE
        elif self.direction == "Down":
            head_y += CELL_SIZE
        elif self.direction == "Left":
            head_x -= CELL_SIZE
        elif self.direction == "Right":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        # Collision with wall
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT
        ):
            return False

        # Collision with itself
        if new_head in self.snake:
            return False

        self.snake.insert(0, new_head)

        # Eat food
        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
            self.canvas.itemconfig(
                self.score_text,
                text=f"Score: {self.score}"
            )
        else:
            self.snake.pop()

        return True

    def draw(self):
        self.canvas.delete("snake")
        self.canvas.delete("food")

        # Draw snake
        for x, y in self.snake:
            self.canvas.create_rectangle(
                x, y,
                x + CELL_SIZE, y + CELL_SIZE,
                fill="lime",
                tags="snake"
            )

        # Draw food
        fx, fy = self.food
        self.canvas.create_oval(
            fx, fy,
            fx + CELL_SIZE, fy + CELL_SIZE,
            fill="red",
            tags="food"
        )

    def game_over(self):
        self.canvas.create_text(
            WIDTH // 2,
            HEIGHT // 2,
            text=f"GAME OVER\nScore: {self.score}\nPress R to Restart",
            fill="white",
            font=("Arial", 20),
            justify="center"
        )

        self.root.bind("r", self.restart)
        self.root.bind("R", self.restart)

    def restart(self, event=None):
        self.root.unbind("r")
        self.root.unbind("R")
        self.reset_game()
        self.update()

    def update(self):
        if self.move_snake():
            self.draw()
            self.root.after(SPEED, self.update)
        else:
            self.game_over()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()