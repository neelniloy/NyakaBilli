from tkinter import *
import tkinter.messagebox
import random
import pygame
from PIL import ImageTk, Image

root = Tk()
root.configure(background='white')
root.title("Nyaka Billi")




bclick = True
flag = 0
score = 0
first_time = True
min_attempt = 1
max_attempt = 9

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
pic = ['1.jpg','3.jpg','5.jpg','6.jpg']

pos = random.choice(num)

img = ImageTk.PhotoImage(Image.open(random.choice(pic)))
img = img._PhotoImage__photo.subsample(5)




def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def enableButton():
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)




def play_music():

    pygame.mixer.init()
    pygame.mixer.music.load("meow.wav")
    pygame.mixer.music.play()



def btnClick(buttons):

    global bclick, flag, photo, pos, score, bp, min_attempt, first_time, max_attempt

    if pos == "1":
        b = button1
    elif pos == "2":
        b = button2
    elif pos == "3":
        b = button3
    elif pos == "4":
        b = button4
    elif pos == "5":
        b = button5
    elif pos == "6":
        b = button6
    elif pos == "7":
        b = button7
    elif pos == "8":
        b = button8
    elif pos == "9":
        b = button9

    if buttons == button1:
        bp = 1
    elif buttons == button2:
        bp = 2
    elif buttons == button3:
        bp = 3
    elif buttons == button4:
        bp = 4
    elif buttons == button5:
        bp = 5
    elif buttons == button6:
        bp = 6
    elif buttons == button7:
        bp = 7
    elif buttons == button8:
        bp = 8
    elif buttons == button9:
        bp = 9

    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "⨉"
        flag += 1
        attempt = "Current Attempt : " + str(flag)
        label1["text"] = attempt

        if buttons == b:
            play_again.configure(state=NORMAL)
            play_music()
            buttons.configure(image=img, height="141", width="132")
            score += 1
            temp = score
            score //= flag
            score += temp
            label["text"] = "Your Score : " + str(score)
            hints["text"] = "Nice! You got it!" + "\nIt took you {} attempts".format(flag)

            disableButton()
            buttons.configure(state=NORMAL)

            if first_time:
                play_again.configure(state=NORMAL)
                min_attempt = flag
                max_attempt = flag
                label2["text"] = "Best Attempt : " + str(min_attempt)
                label3["text"] = "Worst Attempt : " + str(max_attempt)
                first_time = False
            else:
                if min_attempt > flag:
                    min_attempt = flag
                    label2["text"] = "Best Attempt : " + str(min_attempt)
                if max_attempt < flag:
                    max_attempt = flag
                    label3["text"] = "Worst Attempt : " + str(max_attempt)

        elif buttons != b:
            if int(pos) < bp:
                hints["text"] = "Billi is in lower box"
            elif int(pos) > bp:
                hints["text"] = "Billi is in higher box"

    elif buttons == b:
        tkinter.messagebox.showinfo("Nyaka Billi", "Billi has been found!")

    else:
        tkinter.messagebox.showinfo("Nyaka Billi", "Button already Clicked!")



def PlayAgain():
    global flag, bclick, pos, img

    enableButton()

    flag = 0
    bclick = True

    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    if pos == "1":
        b = button1
    elif pos == "2":
        b = button2
    elif pos == "3":
        b = button3
    elif pos == "4":
        b = button4
    elif pos == "5":
        b = button5
    elif pos == "6":
        b = button6
    elif pos == "7":
        b = button7
    elif pos == "8":
        b = button8
    elif pos == "9":
        b = button9

    b.configure(image='', text=' ', font='Times 20 bold', bg='deep sky blue', fg='white', height=4, width=8)

    label["text"] = "Your Score : " + str(score)
    attempt = "Current Attempt : " + str(flag)
    label1["text"] = attempt
    hints["text"] = " "

    pos = random.choice(num)

    img = ImageTk.PhotoImage(Image.open(random.choice(pic)))
    img = img._PhotoImage__photo.subsample(5)



label = Label(root, text="Your Score : 0", font='Times 12 ',bg='white', fg='black', height=1, width=14)
label.grid(row=1, column=0)
label1 = Label(root, text="Current Attempt : 0", font='Times 12 ',bg='white', fg='black', height=1, width=14)
label1.grid(row=2, column=0)
label2 = Label(root, text="Best Attempt : 0", font='Times 12 ',bg='white', fg='black', height=1, width=12)
label2.grid(row=1, column=1)
label3 = Label(root, text="Worst Attempt : 0", font='Times 12 ', bg='white', fg='black', height=1, width=12)
label3.grid(row=2, column=1)

hints = Label(root, text=" ", font='Times 12 ', bg='white', fg='black', height=2, width=14)
hints.grid(row=2, column=2)



button1 = Button(root, text=' ', font='Times 20 bold', bg='deep sky blue', fg='white', height=4, width=8,
                 command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(root, text=' ', font='Times 20 bold', bg='deep sky blue', fg='white', height=4, width=8,
                 command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(root, text=' ', font='Times 20 bold', bg='deep sky blue', fg='white', height=4, width=8,
                 command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(root, text=' ', font='Times 20 bold', bg='deep sky blue', fg='white', height=4, width=8,
                 command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(root, text=' ', font='Times 20 bold', bg='deep sky blue', fg='white', height=4, width=8,
                 command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(root, text=' ', font='Times 20 bold', bg='deep sky blue', fg='white', height=4, width=8,
                 command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(root, text=' ', font='Times 20 bold', bg='deep sky blue', fg='white', height=4, width=8,
                 command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(root, text=' ', font='Times 20 bold', bg='deep sky blue', fg='white', height=4, width=8,
                 command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(root, text=' ', font='Times 20 bold', bg='deep sky blue', fg='white', height=4, width=8,
                 command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

play_again = Button(root, text='Play Again', font='Times 10 bold', bg='gray', fg='white', height=1, width=10,command=lambda: PlayAgain())
play_again.grid(row=1, column=2)

play_again.configure(state=DISABLED)



root.mainloop()

