import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Hypnotic Spiral 🌀")

# Initialize turtle
spiral = turtle.Turtle()
spiral.speed(0)
spiral.width(2)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def draw_spiral():
    """Creates a rotating, color-shifting spiral that grows outward."""
    for angle in range(360):
        spiral.color(random.choice(colors))  # Change colors randomly
        spiral.forward(angle * 0.1)          # Increase distance with angle
        spiral.left(59)                      # Turn slightly to create a spiral pattern

def draw_recursive_fractal(x, y, size):
    """Creates a recursive fractal pattern around the spiral."""
    if size < 10:
        return
    spiral.penup()
    spiral.goto(x, y)
    spiral.pendown()
    for _ in range(6):
        spiral.forward(size)
        draw_recursive_fractal(spiral.xcor(), spiral.ycor(), size / 2)
        spiral.backward(size)
        spiral.right(60)

def main():
    # Draw the main hypnotic spiral
    draw_spiral()
    
    # Draw recursive fractal around the spiral
    draw_recursive_fractal(0, 0, 200)
    
    # Keep the window open
    screen.mainloop()

main()
