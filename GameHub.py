from tkinter import *
from tkinter import messagebox
import turtle
import random
import time
from itertools import cycle
from random import randrange
from tkinter import Canvas, Tk, messagebox, font
import tkinter as tk
from tkinter import messagebox


t=Tk()
t.geometry("800x800")
t.configure(background="black")


#tic tac toe

def tic_tac_toe():
    global clicked_button,count
    root =Tk()
    root.title("TIC TAC TOE")

    clicked_button=0
    count=0

    def click(b):
        global clicked_button,count
        if b["text"]==" " and clicked_button==0:
            b["text"]="X"
            clicked_button=1
            count=count+1
            won()
        elif b["text"]==" " and clicked_button==1:
            b["text"]="O"
            clicked_button=0
            count=count+1
            won()
        else:
            messagebox.showerror("Error","Box has already been selected")
    #win
    def won():
        global winner
        winner=1
        #for X
        if b1["text"]=="X"and b2["text"]=="X"and b3["text"]=="X":
            b1.config(bg="Lightgreen")
            b2.config(bg="Lightgreen")
            b3.config(bg="Lightgreen")
            winner=0
            messagebox.showinfo("Winner","'X' Win!!!")
            disable_button()
        
        elif b4["text"]=="X"and b5["text"]=="X"and b6["text"]=="X":
            b4.config(bg="Lightgreen")
            b5.config(bg="Lightgreen")
            b6.config(bg="Lightgreen")
            winner=0
            messagebox.showinfo("Winner","'X' Win!!!")
            disable_button()

        elif b7["text"]=="X"and b8["text"]=="X"and b9["text"]=="X":
            b7.config(bg="Lightgreen")
            b8.config(bg="Lightgreen")
            b9.config(bg="Lightgreen")
            winner=0
            messagebox.showinfo("Winner","'X' Win!!!")
            disable_button()

        elif b1["text"]=="X"and b4["text"]=="X"and b7["text"]=="X":
            b1.config(bg="Lightgreen")
            b4.config(bg="Lightgreen")
            b7.config(bg="Lightgreen")
            winner=0
            messagebox.showinfo("Winner","'X' Win!!!")
            disable_button()

        elif b2["text"]=="X"and b5["text"]=="X"and b8["text"]=="X":
            b2.config(bg="Lightgreen")
            b5.config(bg="Lightgreen")
            b8.config(bg="Lightgreen")
            winner=0
            messagebox.showinfo("Winner","'X' Win!!!")
            disable_button()

        elif b3["text"]=="X"and b6["text"]=="X"and b9["text"]=="X":
            b3.config(bg="Lightgreen")
            b6.config(bg="Lightgreen")
            b9.config(bg="Lightgreen")
            winner=0
            messagebox.showinfo("Winner","'X' Win!!!")
            disable_button()

        elif b1["text"]=="X"and b5["text"]=="X"and b9["text"]=="X":
            b1.config(bg="Lightgreen")
            b5.config(bg="Lightgreen")
            b9.config(bg="Lightgreen")
            winner=0
            messagebox.showinfo("Winner","'X' Win!!!")
            disable_button()

        elif b3["text"]=="X"and b5["text"]=="X"and b7["text"]=="X":
            b3.config(bg="Lightgreen")
            b5.config(bg="Lightgreen")
            b7.config(bg="Lightgreen")
            winner=0
            messagebox.showinfo("Winner","'X' Win!!!")
            disable_button()

        #for O
        elif b1["text"]=="O"and b2["text"]=="O"and b3["text"]=="O":
            b1.config(bg="Lightgreen")
            b2.config(bg="Lightgreen")
            b3.config(bg="Lightgreen")
            winner=1
            messagebox.showinfo("Winner","'O' Win!!!")
            disable_button()
        
        elif b4["text"]=="O"and b5["text"]=="O"and b6["text"]=="O":
            b4.config(bg="Lightgreen")
            b5.config(bg="Lightgreen")
            b6.config(bg="Lightgreen")
            winner=1
            messagebox.showinfo("Winner","'O' Win!!!")
            disable_button()

        elif b7["text"]=="O"and b8["text"]=="O"and b9["text"]=="O":
            b7.config(bg="Lightgreen")
            b8.config(bg="Lightgreen")
            b9.config(bg="Lightgreen")
            winner=1
            messagebox.showinfo("Winner","'O' Win!!!")

        elif b1["text"]=="O"and b4["text"]=="O"and b7["text"]=="O":
            b1.config(bg="Lightgreen")
            b4.config(bg="Lightgreen")
            b7.config(bg="Lightgreen")
            winner=1
            messagebox.showinfo("Winner","'O' Win!!!")
            disable_button()    

        elif b2["text"]=="O"and b5["text"]=="O"and b8["text"]=="O":
            b2.config(bg="Lightgreen")
            b5.config(bg="Lightgreen")
            b8.config(bg="Lightgreen")
            winner=1
            messagebox.showinfo("Winner","'O' Win!!!")
            disable_button()

        elif b3["text"]=="O"and b6["text"]=="O"and b9["text"]=="O":
            b3.config(bg="Lightgreen")
            b6.config(bg="Lightgreen")
            b9.config(bg="Lightgreen")
            winner=1
            messagebox.showinfo("Winner","'O' Win!!!")
            disable_button()

        elif b1["text"]=="O"and b5["text"]=="O"and b9["text"]=="O":
            b1.config(bg="Lightgreen")
            b5.config(bg="Lightgreen")
            b9.config(bg="Lightgreen")
            winner=1
            messagebox.showinfo("Winner","'O' Win!!!")

        elif b3["text"]=="O"and b5["text"]=="O"and b7["text"]=="O":
            b3.config(bg="Lightgreen")
            b5.config(bg="Lightgreen")
            b7.config(bg="Lightgreen")
            winner=1
            messagebox.showinfo("Winner","'O' Win!!!")
            disable_button()

    def disable_button():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)
        
    #Buttons
    b1=Button(root,text=" ",height=4,width=10,command=lambda:click(b1))
    b2=Button(root,text=" ",height=4,width=10,command=lambda:click(b2))
    b3=Button(root,text=" ",height=4,width=10,command=lambda:click(b3))

    b4=Button(root,text=" ",height=4,width=10,command=lambda:click(b4))
    b5=Button(root,text=" ",height=4,width=10,command=lambda:click(b5))
    b6=Button(root,text=" ",height=4,width=10,command=lambda:click(b6))

    b7=Button(root,text=" ",height=4,width=10,command=lambda:click(b7))
    b8=Button(root,text=" ",height=4,width=10,command=lambda:click(b8))
    b9=Button(root,text=" ",height=4,width=10,command=lambda:click(b9))

    #GRID
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)



#snake
    
#creating screen
def snake_game():
    screen=turtle.Screen()
    screen.title("SNAKE GAME")
    screen.setup(width=700,height=700)
    screen.tracer(0)
    screen.bgcolor("black")

    #creating border
    turtle.speed(5)
    turtle.pensize(4)
    turtle.penup()
    turtle.goto(-310,250)
    turtle.pendown()
    turtle.color("yellow")
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(600)
    turtle.right(90)
    turtle.forward(500)
    turtle.penup()
    turtle.hideturtle()#to hide the pencil of border

    #score
    score=0
    delay=0.1

    #snake
    snake=turtle.Turtle()
    snake.speed()
    snake.shape("circle")
    snake.color("red")
    snake.penup()
    snake.goto(0,0)
    snake.direction='stop'

    #food
    fruit=turtle.Turtle()
    fruit.speed(0)
    fruit.shape("square")
    fruit.color("white")
    fruit.penup()
    fruit.goto(30,30)

    old_f=[]

    #scoring
    scoring=turtle.Turtle()
    scoring.speed(0)
    scoring.color("white")
    scoring.penup()
    scoring.hideturtle()
    scoring.goto(0,300)
    scoring.write("Score: ",align="center",font=("courier",24,"bold"))

    #movement of snake
    def snake_goto_up():
        if snake.direction!="down":
            snake.direction="up"

    def snake_goto_down():
        if snake.direction!="up":
            snake.direction="down"

    def snake_goto_left():
        if snake.direction!="right":
            snake.direction="left"

    def snake_goto_right():
        if snake.direction!="left":
            snake.direction="right"

    def snake_move():
        if snake.direction=="up":
            y=snake.ycor()
            snake.sety(y+20)
        if snake.direction=="down":
            y=snake.ycor()
            snake.sety(y-20)
        if snake.direction=="left":
            x=snake.xcor()
            snake.setx(x-20)
        if snake.direction=="right":
            x=snake.xcor()
            snake.setx(x+20)

    #keyboard control
    screen.listen()
    screen.onkeypress(snake_goto_up,"Up")
    screen.onkeypress(snake_goto_down,"Down")
    screen.onkeypress(snake_goto_left,"Left")
    screen.onkeypress(snake_goto_right,"Right")

    #main loop
    while True:
        screen.update()

        #snake & fruit collision
        if snake.distance(fruit)<20:
            x=random.randint(-290,270)
            y=random.randint(-240,240)
            fruit.goto(x,y)
            scoring.clear()
            score=score+1
            scoring.write("Score:{}".format(score),align="center",font=("courier",24,"bold"))
            delay=delay-0.001

        #creating new foods
            new_f=turtle.Turtle()
            new_f.speed(0)
            new_f.shape("circle")
            new_f.color("orange")
            new_f.penup()
            old_f.append(new_f)

        #adding ball to snake

        for index in range(len(old_f)-1,0,-1):
            a=old_f[index-1].xcor()
            b=old_f[index-1].ycor()

            old_f[index].goto(a,b)

        if len(old_f)>0:
            a=snake.xcor()
            b=snake.ycor()
            old_f[0].goto(a,b)
        snake_move()

        #snake and border collision
        if snake.xcor()>280 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()<-240:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("pink")
            scoring.goto(0,0)
            scoring.write(" GAME OVER \n Your Score is{}".format(score),align="center",font=("courier",38,"bold"))

        #snake collision
        for food in old_f:
            if food.distance(snake)<20:
                time.sleep(1)
                screen.clear()
                screen.bgcolor("pink")
                scoring.goto(0,0)
                scoring.write(" GAME OVER \n Your Score is{}".format(score),align="center",font=("courier",38,"bold"))

        time.sleep(delay)
    turtle.Terminator()

#egg catcher

def egg_catcher():
    canvas_width = 800
    canvas_height = 400
    global score, egg_speed, egg_interval
    global lives_remaining

    root = Tk()
    root.title("Egg Catcher")
    c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue")
    c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill="sea green", width=0)
    c.create_oval(-80, -80, 120, 120, fill='orange', width=0)
    c.pack()

    color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"])
    egg_width = 45
    egg_height = 55
    egg_score = 10
    egg_speed = 500
    egg_interval = 4000
    difficulty = 0.95
    catcher_color = "blue"
    catcher_width = 100
    catcher_height = 100
    catcher_startx = canvas_width / 2 - catcher_width / 2
    catcher_starty = canvas_height - catcher_height - 20
    catcher_startx2 = catcher_startx + catcher_width
    catcher_starty2 = catcher_starty + catcher_height

    catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=3)
    game_font = font.nametofont("TkFixedFont")
    game_font.config(size=18)


    score = 0
    score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score))

    lives_remaining = 3
    lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining))

    eggs = []

    def create_egg():
        x = randrange(10, 740)
        y = 40
        new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
        eggs.append(new_egg)
        root.after(egg_interval, create_egg)

    def move_eggs():
        for egg in eggs:
            (eggx, eggy, eggx2, eggy2) = c.coords(egg)
            c.move(egg, 0, 10)
            if eggy2 > canvas_height:
                egg_dropped(egg)
        root.after(egg_speed, move_eggs)

    def egg_dropped(egg):
        eggs.remove(egg)
        c.delete(egg)
        lose_a_life()
        if lives_remaining == 0:
            messagebox.showinfo("Game Over!", "Final Score: "+ str(score))
            root.destroy()

    def lose_a_life():
        global lives_remaining
        lives_remaining -= 1
        c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

    def check_catch():
        (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)
        for egg in eggs:
            (eggx, eggy, eggx2, eggy2) = c.coords(egg)
            if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
                eggs.remove(egg)
                c.delete(egg)
                increase_score(egg_score)
        root.after(100, check_catch)

    def increase_score(points):
        global score, egg_speed, egg_interval
        score += points
        egg_speed = int(egg_speed * difficulty)
        egg_interval = int(egg_interval * difficulty)
        c.itemconfigure(score_text, text="Score: "+ str(score))

    def move_left(event):
        (x1, y1, x2, y2) = c.coords(catcher)
        if x1 > 0:
            c.move(catcher, -20, 0)

    def move_right(event):
        (x1, y1, x2, y2) = c.coords(catcher)
        if x2 < canvas_width:
            c.move(catcher, 20, 0)

    c.bind("<Left>", move_left)
    c.bind("<Right>", move_right)
    c.focus_set()
    root.after(1000, create_egg)
    root.after(1000, move_eggs)
    root.after(1000, check_catch)
    root.mainloop()

#rock_paper_scissor
def rock_paper_scissor():
    class RockPaperScissorsGame:
        def __init__(self, master):
            self.master = master
            self.master.title("Rock, Paper, Scissors Game")

            self.choices = ["Rock", "Paper", "Scissors"]

            self.user_choice_label = tk.Label(self.master, text="Your Choice:")
            self.user_choice_label.pack()

            self.user_choice_var = tk.StringVar()
            self.user_choice_var.set(self.choices[0])

            self.user_choice_menu = tk.OptionMenu(self.master, self.user_choice_var, *self.choices)
            self.user_choice_menu.pack()

            self.submit_button = tk.Button(self.master, text="Submit Choice", command=self.play_game)
            self.submit_button.pack()

        def play_game(self):
            user_choice = self.user_choice_var.get()
            computer_choice = random.choice(self.choices)

            result = self.determine_winner(user_choice, computer_choice)

            messagebox.showinfo("Result", f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}")

        def determine_winner(self, user_choice, computer_choice):
            if user_choice == computer_choice:
                return "It's a tie!"
            elif (
                (user_choice == "Rock" and computer_choice == "Scissors") or
                (user_choice == "Paper" and computer_choice == "Rock") or
                (user_choice == "Scissors" and computer_choice == "Paper")
            ):
                return "You win!"
            else:
                return "Computer wins!"

    # Create the main window
    root = tk.Tk()

    # Create an instance of the game
    game = RockPaperScissorsGame(root)

    # Run the Tkinter event loop
    root.mainloop()

#guess number
def guess_no():
    class GuessingGame:
        def __init__(self, master):
            self.master = master
            self.master.title("Guessing Game")

            self.secret_number = random.randint(1, 100)
            self.guess_label = tk.Label(self.master, text="Enter your guess:")
            self.guess_label.pack()

            self.guess_entry = tk.Entry(self.master)
            self.guess_entry.pack()

            self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess)
            self.submit_button.pack()

        def check_guess(self):
            user_guess = self.guess_entry.get()

            try:
                user_guess = int(user_guess)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")
                return

            if user_guess == self.secret_number:
                messagebox.showinfo("Congratulations!", "You guessed the correct number!")
                self.master.destroy()
            elif user_guess < self.secret_number:
                messagebox.showinfo("Incorrect", "Try a higher number")
            else:
                messagebox.showinfo("Incorrect", "Try a lower number")

    # Create the main window
    root = tk.Tk()

    # Create an instance of the game
    game = GuessingGame(root)

    
b1=Button(t,text="Tic Tac Toe",command=tic_tac_toe,bg="white",fg="green",activebackground="green",activeforeground="white",bd="5",font=("Helvetica",20),height=2).pack(pady=20)
b2=Button(t,text="Snake Game",command=snake_game,bg="white",fg="red",activebackground="red",activeforeground="white",bd="5",font=("Helvetica",20),height=2).pack(pady=20)
b3=Button(t,text="Egg Catcher",command=egg_catcher,bg="white",fg="blue",activebackground="blue",activeforeground="white",bd="5",font=("Helvetica",20),height=2).pack(pady=20)    
b4=Button(t,text="Rock Paper Scissor",command=rock_paper_scissor,bg="white",fg="orange",activebackground="orange",activeforeground="white",bd="5",font=("Helvetica",20),height=2).pack(pady=30)
b5=Button(t,text="Guess The Number",command=guess_no,bg="white",fg="yellow",activebackground="yellow",activeforeground="white",bd="5",font=("Helvetica",20),height=2).pack(pady=10)
t.mainloop()


