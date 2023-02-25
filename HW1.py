import turtle

T = turtle.Pen()
S = turtle.Screen()
S.bgcolor("black")
T.pencolor("blue")
n=0
while True:
        for i in range (4):
            T.forward(50)
            T.right(90)
        T.rt(10)
        n+=1
        if n>=36:
            T.forward(50)
            break
    
T.pen(pencolor="white",pensize=10, speed=9)        
T.penup()
T.goto(0,100)
T.pendown()
for i in range (10):
    T.forward(500)

T.penup()
T.goto(0,100)
T.pendown()
for i in range (10):
    T.backward(500)
    
T.penup()
T.goto(0,-100)
T.pendown()
for i in range (2):
       T.forward(500)

T.penup()
T.goto(0,-100)
T.pendown()
for i in range (2):
        T.backward(500)
        
T.pen(pencolor="red",pensize=4, speed = 10)
T.color("pink")
T.penup()
T.goto(0,-400)
T.pendown()
T.begin_fill()
T.lt(140)
T.forward(180)
T.circle(-90,200)
T.setheading(60)
T.circle(-90,200)
T.forward(178)
T.end_fill()
                

T.pen(pencolor="white",pensize=1, speed=9)
T.penup()
T.goto(0,300)
T.pendown()
T.pencolor("green")
a=0
b=0
while True:
        for i in range (4):
            T.forward(80)
            T.right(90)
        T.rt(10)
        a+=1
        if a>=360/45:
            T.forward(50)
            a = 0
            b+=1
            if b>=4:
                break
            




