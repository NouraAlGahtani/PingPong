import turtle as turtle
import os


player_a_score = 0
player_b_score = 0

win = turtle.Screen() # to create a window
win.title("THE PINGPONG GAME") #Name of the game duh
win.bgcolor('purple') # color of main Page aka homescreen
win.setup(width=800, height=600) # size of the game
win.tracer(0) # Speeeeeeeeeeeeeeeed


# Create left paddle for the game

paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square') # i kinda want to change the shape but i cant sadly :/
paddle_left.color('pink')
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)




# now same thing but right side hehe
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square') # i kinda want to change the shape but i cant sadly :/
paddle_right.color('white')
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350,0)


# now we will create the ball
ball = turtle.Turtle()
ball.speed(1) # 1 slowest and 0 fastest
ball.shape('circle')
ball.color('black')
ball.penup()
ball.goto(0,0)
ball_dx = 1.5 # setting up pixs
ball_dy = 1.5


#  pen for Scores(updated)
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0", align="center" , font=('monaco', 25,"normal"))



# controllers for left paddle

def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 15
    paddle_left.sety(y)
    
    

# moving the left paddle Down
def paddle_left_down():
 y = paddle_left.ycor()
 y  = y - 15
 paddle_left.sety(y)



# moving the right paddle up
def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 15
    paddle_right.sety(y)
    
# moving the paddle down

def paddle_right_down():
 y = paddle_right.ycor()
 y = y - 15
 paddle_right.sety(y)



# Keyboard binding
win.listen()
win.onkeypress(paddle_left_up,"u")
win.onkeypress(paddle_left_down,"e")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down, "down")











#######################Main Game func aka loop##################

while True:
    win.update() # so our ping pong game starts 
    #########how to move the ball##########
    
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)
    
    
    
    
    # setting up the border
    
    if ball.ycor() > 290: #right top border
       ball.sety(290)
       ball_dy = ball_dy * -1
    
    if ball.ycor() > -290: # left top border
       ball.sety(-290)
       ball_dy = ball_dy * -1
       
    if ball.xcor() > 390:  #right width bord
        ball.goto(0,0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}" .format(player_a_score, player_b_score), align="center", font=('Manaco',24,"normal"))
        os.system("afplay wallhit.wav&")
        # colis w paddle handling
        
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")
        
    if(ball.xcor() < -340) and (ball.xcor() > -350 ) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40):
       ball.setx(-340)
       ball_dx = ball_dx * -1
       os.system("afplay paddle.wav&")







