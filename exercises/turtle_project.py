"""Turtle Project."""

___author___ = "730651920"


from turtle import Turtle, colormode, done
colormode(255)
ground_turtle: Turtle = Turtle()
tree_turtle: Turtle = Turtle()
sky_turtle: Turtle = Turtle()
clouds_turtle: Turtle = Turtle()


def draw_rectangle(a_turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw a rectangle of the given width whose top-left corner is located at x, y."""
    a_turtle.speed(500)
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        if i % 2 != 0:
            a_turtle.forward(length)
            a_turtle.right(90)
            i += 1
        else:
            a_turtle.forward(width)
            a_turtle.right(90)
            i = i + 1


def draw_circle(a_turtle: Turtle, x: float, y: float, size: float) -> None:
    """Function that creates circles."""
    a_turtle.speed(90000)
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.pendown()
    a_turtle.circle(size)


def draw_clouds(clouds_turtle: Turtle, x: float, y: float, size: float) -> None:
    """Function that creates clouds using circles function."""
    clouds_turtle.speed(50000)
    clouds_turtle.fillcolor(255, 255, 255)
    clouds_turtle.pencolor(255, 255, 255)
    clouds_turtle.penup()
    clouds_turtle.goto(x, y)
    clouds_turtle.pendown
    clouds_turtle.begin_fill()
    draw_circle(clouds_turtle, x, y, size)
    clouds_turtle.end_fill()
    clouds_turtle.begin_fill()
    draw_circle(clouds_turtle, x + 25, y - 50, size)
    clouds_turtle.end_fill()
    clouds_turtle.begin_fill()
    draw_circle(clouds_turtle, x - 25, y - 50, size)
    clouds_turtle.end_fill()


def draw_grass(grass_turtle: Turtle, x: float, y: float, size: float) -> None:
    """Function used to draw grass in the scence using traingles."""
    i: int = 0
    grass_turtle.fillcolor(39, 142, 36)
    grass_turtle.pencolor(39, 142, 36)
    grass_turtle.speed(500)
    grass_turtle.penup()
    grass_turtle.goto(x, y) 
    grass_turtle.setheading(0.0)
    grass_turtle.pendown()
    grass_turtle.begin_fill()
    while i < 3:
        grass_turtle.forward(size)
        grass_turtle.left(120)
        i += 1
    grass_turtle.end_fill()    


def sky(sky_turtle: Turtle, x: float, y: float) -> None:
    """Function that creates the sky with clouds."""
    sky_turtle.speed(500)
    sky_turtle.penup()
    sky_turtle.goto(x, y)
    sky_turtle.pendown()
    sky_turtle.fillcolor(0, 204, 204)
    sky_turtle.pencolor(0, 204, 204)
    sky_turtle.begin_fill()
    draw_rectangle(sky_turtle, x, y, 700, 350)
    sky_turtle.end_fill()
    draw_clouds(sky_turtle, -300, 280, 35)
    draw_clouds(sky_turtle, -200, 280, 35)
    draw_clouds(sky_turtle, 0, 280, 35)
    draw_clouds(sky_turtle, 100, 280, 35)


def ground(ground_turtle: Turtle, x: float, y: float) -> None:
    """Draws the ground for the scene."""
    i: int = 0
    ground_turtle.speed(500)
    ground_turtle.penup()
    ground_turtle.goto(x, y)
    ground_turtle.pendown()
    ground_turtle.fillcolor(21, 168, 16)
    ground_turtle.pencolor(21, 168, 16)
    ground_turtle.begin_fill()
    draw_rectangle(ground_turtle, x, y, 700, 300)
    ground_turtle.end_fill()
    while i < 25:
        draw_grass(ground_turtle, x, -10, 30)
        x += 30
        i += 1


def draw_tree(tree_turtle: Turtle, x: float, y: float,) -> None:
    """Function draws trees using grass traingles."""
    tree_turtle.speed(500)
    tree_turtle.penup()
    tree_turtle.goto(x, y)
    tree_turtle.pendown()
    tree_turtle.pencolor(102, 51, 0)
    tree_turtle.fillcolor(102, 51, 0)
    tree_turtle.begin_fill()
    draw_rectangle(tree_turtle, x, y, 20, 50)
    tree_turtle.end_fill()
    draw_grass(tree_turtle, x - 12, y, 50)


def main() -> None:
    """Main function that draws the scence."""
    sky(sky_turtle, -350, 350)
    ground(ground_turtle, -350, 0)
    x_tree1: int = -300
    y_tree1: int = 12
    x_tree2: int = -300
    y_tree2: int = -250
    while x_tree1 != 350 and y_tree1 != -300:
        draw_tree(tree_turtle, x_tree1, y_tree1)
        x_tree1 += 130
        y_tree1 -= 45
    while x_tree2 != 350 and y_tree2 != 0:
        draw_tree(tree_turtle, x_tree2, y_tree2)
        x_tree2 += 110
        y_tree2 += 45


main()


done()