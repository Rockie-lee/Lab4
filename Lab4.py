import turtle
import random


def draw_square(t, length):
    """Draws a square with the given side length."""
    for _ in range(4):
        t.forward(length)
        t.left(90)


def draw_circle(t, radius):
    """Draws a circle with the given radius."""
    t.circle(radius)


def draw_polygon(t, sides, length):
    """Draws a regular polygon with a given number of sides and side length."""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)


def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw pumpkin body
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Draw the stem
    t.fillcolor("green")
    t.begin_fill()
    t.goto(x, y + radius)  # Start at the top of the pumpkin
    t.setheading(90)  # Point upwards
    t.forward(radius // 2)
    t.right(90)
    t.forward(radius // 5)
    t.right(90)
    t.forward(radius // 2)
    t.right(90)
    t.forward(radius // 5)
    t.end_fill()
    t.setheading(0)  # Reset orientation


def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    draw_polygon(t, 3, size)  # Triangle for the eye
    t.end_fill()


def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()


def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()


def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)

        # Ensure stars are above the pumpkins
        if y < -100:  # Prevent stars from being too low
            y = random.randint(-100, 300)

        draw_star(t, x, y, size)


# Create a turtle object
t = turtle.Turtle()
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
screen = turtle.Screen()
screen.bgcolor("darkblue")
screen.setup(width=600, height=600)
t.clear()

# Draw three jack-o-lanterns at a lower position
draw_pumpkin(t, -150, -150, 100)  # Draw the left pumpkin
draw_eye(t, -190, -60, 30)  # Left eye
draw_eye(t, -110, -60, 30)  # Right eye
draw_mouth(t, -150, -100, 80)  # Mouth

draw_pumpkin(t, 0, -150, 80)  # Middle pumpkin
draw_eye(t, -20, -70, 25)
draw_eye(t, 20, -70, 25)
draw_mouth(t, 0, -110, 60)

draw_pumpkin(t, 150, -150, 100)  # Draw the right pumpkin
draw_eye(t, 110, -60, 30)
draw_eye(t, 190, -60, 30)
draw_mouth(t, 150, -100, 80)

# Draw the night sky with stars
draw_sky(t, 30)  # Draw 30 stars


turtle.exitonclick()


