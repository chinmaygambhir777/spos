# ------------------------------------------------------------
# 🕹️ Gaming App using Python Turtle
#
# 📦 Required Libraries:
#     pip install PythonTurtle (Note: Usually built-in with Python)
#
# 🚀 How to Run:
# 1. Save this code as gamingApp.py
# 2. Run it using: python gamingApp.py
# 3. Use Left/Right arrow keys to move the paddle and catch the ball.
# ------------------------------------------------------------

import turtle, random

# Set up the paddle turtle
t = turtle.Turtle()
t.speed(0)
t.shape("square")
t.color("blue")
t.penup()
t.goto(0, -150)

# Set up the ball turtle
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(random.randint(-150, 150), 150)

# Initialize score
score = 0

def move_left():
    """Move the paddle left, checking for the wall."""
    x = t.xcor() - 20
    if x > -200:
        t.setx(x)

def move_right():
    """Move the paddle right, checking for the wall."""
    x = t.xcor() + 20
    if x < 200:
        t.setx(x)

def move_ball():
    """Main game loop: moves ball, checks for catch or miss."""
    global score
    
    # Move ball down
    y = ball.ycor() - 5
    ball.sety(y)

    # Check for a catch
    if ball.ycor() < -150 and abs(ball.xcor() - t.xcor()) < 20:
        score += 1
        print("Score:", score)
        # Reset ball to top
        ball.goto(random.randint(-150, 150), 150)

    # Check for a miss (game over)
    elif ball.ycor() < -200:
        print("Game Over! Final Score:", score)
        turtle.bye()  # Close the game window
        return        # Stop the game loop

    # Keep the loop running
    turtle.ontimer(move_ball, 50)

# Set up keyboard listeners
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")

# Start the game
move_ball()
turtle.mainloop()
