from turtle import * 

paper = Screen()
paper.bgcolor("Black")
paper.title("Write your name")
paper.setup(width = 1000, height = 500)

#forward,right,back,left
def F():
    turt = Turtle()
    turt.color("white")
    turt.shape("turtle")
    turt.seth(90)
    turt.pu()
    turt.goto(-300,-100)
    turt.pd()
    turt.fd(200)
    turt.rt(90)
    turt.fd(100)
    turt.bk(100)
    turt.rt(90)
    turt.fd(70)
    turt.lt(90)
    turt.fd(70)
    turt.ht()

def R():
    turt = Turtle()
    turt.color("Blue")
    turt.shape("turtle")
    turt.seth(90)
    turt.pu()
    turt.goto(-155,-100)
    turt.pd()
    turt.fd(200)
    for i in range(180):
        turt.fd(1)
        turt.seth(-i)
    turt.seth(315)
    turt.fd(100)
    
R()


paper.exitonclick()