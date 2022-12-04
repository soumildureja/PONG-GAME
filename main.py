import turtle
import time
import winsound
import tkinter
from tkinter import messagebox
turtle.bgpic(picname="un1.png")
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width= 800, height= 600)
wn.title("Pong")
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color('white', '#39FF14')
paddle_a.speed(0)
paddle_a.shapesize(7,1)
paddle_a.penup()
paddle_a.goto(-400, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.tilt(180)
paddle_b.shape("square")
paddle_b.color('white', '#39FF14')
paddle_b.speed(0)
paddle_b.shapesize(7.5,1.78)
paddle_b.penup()
paddle_b.goto(400, 0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white", "#4c8bf5")
pen.penup()
pen.goto(0,267)
pen.hideturtle()
pen.write("Player A:0 Player B:0", align= "center" , font= ("Courier", 24, "normal"))

# Smoothing
paddle_a.move_up = False
paddle_a.move_down = False
paddle_b.move_up = False
paddle_b.move_down = False

def paddle_a_up_start():
    paddle_a.move_up = True

def paddle_a_up_end():
    paddle_a.move_up = False
    
def paddle_a_down_start():
    paddle_a.move_down = True

def paddle_a_down_end():
    paddle_a.move_down = False

# write similar code for paddle_b_up and paddle_b_down

def paddle_b_up_start():
    paddle_b.move_up = True

def paddle_b_up_end():
    paddle_b.move_up = False

def paddle_b_down_start():
    paddle_b.move_down = True

def paddle_b_down_end():
    paddle_b.move_down = False

# Keyboard Binding
'''Paddle A'''
wn.listen()
wn.onkeypress(paddle_a_up_start, "w")
wn.onkeyrelease(paddle_a_up_end, "w")

wn.onkeypress(paddle_a_down_start, "s")
wn.onkeyrelease(paddle_a_down_end, "s")

'''Paddle B'''
wn.onkeypress(paddle_b_up_start,"Up")
wn.onkeyrelease(paddle_b_up_end,"Up")
wn.onkeypress(paddle_b_down_start,"Down")
wn.onkeyrelease(paddle_b_down_end,"Down")

# Main Game Loop
while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("grunge-bounce-drum-loop-40464.mp3", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("grunge-bounce-drum-loop-40464.mp3", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a , score_b), align= "center" , font= ("Courier", 24, "normal"))
        # winsound.PlaySound("grunge-bounce-drum-loop-40464.mp3", winsound.SND_ASYNC)
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a , score_b), align= "center" , font= ("Courier", 24, "normal"))
        # winsound.PlaySound("grunge-bounce-drum-loop-40464.mp3", winsound.SND_ASYNC)

    if paddle_a.move_up:
        if paddle_a.ycor() + 70 < 300:
            y = paddle_a.ycor()
            y += 0.5
            paddle_a.sety(y)

    if paddle_a.move_down:
        if paddle_a.ycor() - 70 > -300:
            y = paddle_a.ycor()
            y -= 0.5
            paddle_a.sety(y)
    
    if paddle_b.move_up:
        if paddle_b.ycor() + 70 < 300:
            y = paddle_b.ycor()
            y += 0.5
            paddle_b.sety(y)

    if paddle_b.move_down:
        if paddle_b.ycor() - 70 > -300:
            y = paddle_b.ycor()
            y -= 0.5
            paddle_b.sety(y)
    
    if score_a == 5:
        messagebox.showwarning("GAMEOVER","Player A WON")
        break
    
    if score_b== 5:
        messagebox.showwarning("GAME OVER","Player B WON")
        break
    
    if ball.xcor() > 380 and (ball.ycor() < paddle_b.ycor() + 100 and ball.ycor() > paddle_b.ycor() -100):
        ball.dx *= -1

    if ball.xcor() < -380 and (ball.ycor() < paddle_a.ycor() + 100 and ball.ycor() > paddle_a.ycor() -100):
        ball.dx *= -1

    wn.update()