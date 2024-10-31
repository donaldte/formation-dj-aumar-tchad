import turtle
import random

# Configuration de l'écran
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Crazy Moon Design 🌕")

# Initialisation de la tortue
moon = turtle.Turtle()
moon.speed(0)
moon.hideturtle()
moon.color("gray")
moon.pensize(2)

def draw_circle(x, y, radius, color):
    """Dessine un cercle avec des positions et couleurs aléatoires pour les cratères."""
    moon.penup()
    moon.goto(x, y - radius)
    moon.pendown()
    moon.color(color)
    moon.begin_fill()
    moon.circle(radius)
    moon.end_fill()

def draw_moon(x, y, radius):
    """Dessine le contour de la lune avec des cratères aléatoires."""
    draw_circle(x, y, radius, "lightgray")
    
    # Créer des cratères de manière aléatoire
    for _ in range(10):
        crater_radius = random.randint(10, 30)
        crater_x = x + random.randint(-radius + 20, radius - 20)
        crater_y = y + random.randint(-radius + 20, radius - 20)
        draw_circle(crater_x, crater_y, crater_radius, "darkgray")

def draw_crazy_patterns():
    """Ajoute des motifs aléatoires pour donner un effet graphique fou à la lune."""
    colors = ["white", "lightgray", "darkgray", "silver"]
    moon.penup()
    for _ in range(100):
        moon.goto(random.randint(-200, 200), random.randint(-200, 200))
        moon.color(random.choice(colors))
        moon.dot(random.randint(2, 8))

def main():
    # Dessiner la lune et les motifs
    draw_moon(0, 0, 100)
    draw_crazy_patterns()
    screen.mainloop()

main()
