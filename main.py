from turtle import * 

paper = Screen()
paper.bgcolor("Black")
paper.title("Write your name")
paper.setup(width = 1200, height = 500)

#forward,right,back,left
def F():
    turt = Turtle()
    turt.pensize(5)
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
F()
def R():
    turt = Turtle()
    turt.pensize(5)
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
    turt.seth(300)
    turt.fd(100)
    turt.ht()

R()
    


def U():
    turt = Turtle()
    turt.pensize(5)
    turt.color("Yellow")
    turt.shape("turtle")
    turt.seth(270)
    turt.pu()
    turt.goto(-25,100)
    turt.pd()
    turt.forward(150)      
    turt.circle(50, 180)   
    turt.forward(150)
    turt.ht()
U()





def I():
    turt = Turtle()
    turt.pensize(5)
    turt.color("red")
    turt.shape("turtle")
    turt.seth(90)
    turt.pu()
    turt.goto(200,-100)
    turt.pd()
    turt.goto(200,100)
    turt.lt(90)
    turt.goto(150,100)
    turt.goto(250,100)
    turt.pu()
    turt.goto(250,-100)
    turt.pd()
    turt.goto(150,-100)
    turt.ht()

I()

def T():
    turt = Turtle()
    turt.pensize(5)
    turt.color("green")
    turt.shape("turtle")
    turt.seth(270)
    turt.pu()
    turt.goto(350,100)
    turt.pd()
    turt.rt(90)
    turt.fd(50)
    turt.lt(180)
    turt.goto(400,100)
    turt.pu()
    turt.goto(350,-100)
    turt.lt(90)
    turt.pd()
    turt.fd(200)
    turt.ht()




T()
    

paper.exitonclick()