from tkinter import *
import math
import random
import tkinter.messagebox

game = Tk()
game.title("Number Game")
game.geometry("350x175")

number = random.randint(1,50)

def ok_funct():
    name = entrybox.get()
    tkinter.messagebox.showinfo("Hello!","Hey "+name+", I am thinking of a number between 1 and 50, try to guess it.")

def guess():
    guessed = int(entrybox2.get())
    if guessed > number:
        tkinter.messagebox.showinfo("Too high","Your guess is too high")
    if guessed < number:
        tkinter.messagebox.showinfo("Too low","Your guess is too low")
    if guessed == number:
        tkinter.messagebox.showinfo("Good job!", "You found the correct number!")

label = Label(game,text="Welcome to the number game!")
label.grid(row=0,column=2,pady=10, padx=3)
name_label = Label(game,text="What's your name?")
name_label.grid(row=1,column=1)
entrybox = Entry(game,width=25)
entrybox.grid(row=1,column=2)

ok_btn = Button(game,text="Ok",command=ok_funct)
ok_btn.grid(row=1,column=3,pady=3,padx=3)

guess_label = Label(game,text="Take a guess:")
guess_label.grid(row=3,column=1)
entrybox2 = Entry(game,width=25)
entrybox2.grid(row=3,column=2)

guess_btn = Button(game,text="Guess",command=guess)
guess_btn.grid(row=3,column=3,pady=3,padx=3)

game.mainloop()
