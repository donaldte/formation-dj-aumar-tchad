import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Crazy Sun Design 🌞")

# Initialize turtle
sun = turtle.Turtle()
sun.speed(0)
sun.hideturtle()

# Draw main sun circle
def draw_circle(x, y, radius, color):
    """Draws a filled circle at (x, y) with given radius and color."""
    sun.penup()
    sun.goto(x, y - radius)
    sun.pendown()
    sun.color(color)
    sun.begin_fill()
    sun.circle(radius)
    sun.end_fill()

# Draw the sun rays
def draw_sun_rays(x, y, radius, num_rays):
    """Draws rays around the sun in a random pattern."""
    sun.penup()
    sun.goto(x, y)
    sun.setheading(0)
    sun.color("yellow")
    for _ in range(num_rays):
        angle = random.randint(0, 360)
        sun.setheading(angle)
        sun.forward(radius + 10)
        sun.pendown()
        sun.forward(random.randint(20, 50))
        sun.penup()
        sun.goto(x, y)

# Draw fun patterns around the sun
def draw_crazy_patterns():
    """Adds crazy patterns around the sun for a unique effect."""
    colors = ["yellow", "orange", "red"]
    sun.penup()
    for _ in range(100):
        sun.goto(random.randint(-250, 250), random.randint(-250, 250))
        sun.color(random.choice(colors))
        sun.dot(random.randint(5, 10))

# Main function to create the sun with rays and patterns
def main():
    # Draw the main sun body
    draw_circle(0, 0, 100, "orange")
    
    # Draw rays
    draw_sun_rays(0, 0, 100, 30)
    
    # Draw additional patterns
    draw_crazy_patterns()

    # Keep the window open
    screen.mainloop()

main()
