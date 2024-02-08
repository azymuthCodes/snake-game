import tkinter
import turtle
import time
import random
import math


delay=0.1


#Window Creation    
window=turtle.Screen()
window.bgcolor("green")
window.bgpic("snake-backdrop.png")
window.title("Snake Game")
window.tracer(0) 
#Change the Window Icon
img=tkinter.Image("photo",file="snake.png")
turtle._Screen._root.iconphoto(True,img)



#Snake Creation
global snake
snake=turtle.Turtle()
snake.shape("square")
snake.color("red")
snake.speed(1)
snake.penup()
snake.direction="stop"



#Food Creation
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.shapesize(0.7,0.7)
food.penup()
foodposx=random.randint(-200,200)
foodposy=random.randint(-200,200)
food.goto(foodposx,foodposy)

#Border Creation
border=turtle.Turtle()
border.speed(0)
border.color("cyan")
border.pensize(5)
border.penup()
border.setpos(-313,235)
border.pendown()
for i in range(2):
    border.forward(626)
    border.right(90)
    border.forward(526)
    border.right(90)
border.hideturtle()


score=0
highscore=0
segments=[]

#Score Creation
penScore=turtle.Turtle()
penScore.speed(0)
penScore.shape("square")
penScore.color("black")
penScore.penup()
penScore.hideturtle()
penScore.goto(-220,260)
penScore.write("Score:{}".format(score),align="left",font=("Arial",24,"normal"))


#High Score Creation
penHScore=turtle.Turtle()
penHScore.speed(0)
penHScore.shape("square")
penHScore.color("black")
penHScore.penup()
penHScore.hideturtle()
penHScore.goto(220,260)
penHScore.write("High Score:{}".format(highscore),align="right",font=("Arial",24,"normal"))



def movements():
    if snake.direction=="right":
        snake.setx(snake.xcor()+20)
    elif snake.direction=="left":
        snake.setx(snake.xcor()-20)
    elif snake.direction=="up":
        snake.sety(snake.ycor()+20)
    elif snake.direction=="down":
        snake.sety(snake.ycor()-20)

def go_up():
    if snake.direction!="down":
        snake.direction="up"
def go_down():
    if snake.direction!="up":
        snake.direction="down"
def go_right():
    if snake.direction!="left":
        snake.direction="right"
def go_left():
    if snake.direction!="right":
        snake.direction="left"


window.listen()
window.onkey(go_up,"Up")
window.onkey(go_down,"Down")
window.onkey(go_left,"Left")
window.onkey(go_right,"Right")

#Main Loop
while True:
    window.update()

    #Detect Border Collision
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>200 or snake.ycor()<-260:
        snake.direction="stop"
        time.sleep(2)
        snake.goto(0,0)
        
        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()
        foodposx=random.randint(-200,200)
        foodposy=random.randint(-200,200)
        food.goto(foodposx,foodposy)


        score=0

        penScore.clear()
        penScore.write("Score:{}".format(score),align="left",font=("Arial",24,"normal"))
        
        penHScore.clear()
        penHScore.write("High Score:{}".format(highscore),align="right",font=("Arial",24,"normal"))


    #Detect Food Collision    
    foodcollidingdist=math.sqrt(pow(snake.xcor()-foodposx,2)+pow(snake.ycor()-foodposy,2))
    if foodcollidingdist<15:
        foodposx=random.randint(-200,200)
        foodposy=random.randint(-200,200)
        food.goto(foodposx,foodposy)

        #Add segment 
        segment=turtle.Turtle()
        segment.shape("square")
        segment.color("white")
        segment.speed(0)
        segment.penup()
        segments.append(segment)

        delay-=0.001

        score+=10

        if score>highscore:
            highscore=score
            penHScore.clear()
            penHScore.write("High Score:{}".format(highscore),align="right",font=("Arial",24,"normal"))

        
        penScore.clear()
        penScore.write("Score:{}".format(score),align="left",font=("Arial",24,"normal"))

    
    #To setpos for the upcoming segments
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments)>0:
        segments[0].goto(snake.xcor(),snake.ycor())

    movements()

    #Detect Body Collision
    for segment in segments:
        bodycollidingdist=math.sqrt(math.pow(snake.xcor()-segment.xcor(),2)+math.pow(snake.ycor()-segment.ycor(),2))
        if bodycollidingdist<15:
            snake.direction="stop"
            time.sleep(2)
            snake.goto(0,0)
            
            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()
            foodposx=random.randint(-200,200)
            foodposy=random.randint(-200,200)
            food.goto(foodposx,foodposy)

            score=0

            penScore.clear()
            penScore.write("Score:{}".format(score),align="left",font=("Arial",24,"normal"))
    


    time.sleep(delay)


window.mainloop()
       