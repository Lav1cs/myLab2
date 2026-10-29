import turtle


def draw_house_triangle(x, y, size):
    """
    Функция рисует дом из квадрата и треугольной крыши.
    x, y — координаты левого нижнего угла дома.
    size — длина стены и стороны крыши.
    """
    t = turtle.Turtle()
    t.speed(3)

    # 1. Рисуем основание дома (квадрат)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    for _ in range(4):
        t.forward(size)
        t.left(90)


    t.penup()
    t.goto(x, y + size)
    t.pendown()

    # Рисуем треугольник
    t.setheading(0)
    t.left(60)
    t.forward(size)
    t.right(120)
    t.forward(size)

    t.hideturtle()


screen = turtle.Screen()
screen.setup(600, 600)

draw_house_triangle(-100, -100, 200)

screen.mainloop()



favourite_fruits = ['Апельсин', 'Банан', 'Груша', 'Манго', 'Яблоко']

your_fruit = input("Введи любой фрукт")

if (your_fruit in favourite_fruits):
    print(f"{your_fruit} является твоим любимым фруктом")
else:
    print(f"{your_fruit} фуууу")