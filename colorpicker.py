import sys
from tkinter import *
import tkinter.font
from datetime import datetime
import random

score = 0
mScore = 0
counter = 0
timer = False


def counter_label(lbTime):
    def count():
        if timer == True:
            global counter
            if counter == 0:
                display = "00:00"
            else:
                date = datetime.fromtimestamp(counter)
                string = date.strftime("%M:%S")
                display = string
            lbTime.config(text=display)
            lbTime.after(1000, count)
            counter += 1
    count()


def StartCounter(lbTime):
    global timer
    timer = True
    btnStart['state'] = 'disabled'
    counter_label(lbTime)


def reset():
    global counter, timer, btnStart
    if timer >= 0:
        timer = False
        counter = 0
        timer = 0
        lbTime.config(text='00:00')
    else:
        timer = True
    btnStart['state'] = 'normal'


root = Tk()
root.title("Main Window")
root.geometry("530x300")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.configure(background='#252422')


def info():
    global TitleFont
    root_info = Tk()
    root_info.title("Információ")
    root_info.geometry("500x350")
    root_info.resizable(False, False)
    root_info.eval('tk::PlaceWindow . center')
    root_info.configure(background='#252422')

    info_Title = Label(root_info, text="Szabályzat")

    info1 = Label(root_info, text="1.: 9 szín közül lehet választani.\n\n2.: A 'Start' gomb lenyomásával indíthatod a játékot.\n\n3.: Mindig azt a színt írd le nagy kezdőbetűvel (Kék, Sárga...), \nami a megjelent szöveg színe\n\n4.: Minden jó válaszért +1pont jár.\n\n5.: Rossz válasz esetén vesztettél.")

    infoBtn = Button(root_info, text="Vissza", command=root_info.destroy)

    info_Title.grid(row=0, column=0, padx=20, sticky=EW)
    info1.grid(row=1, pady=15, column=0, padx=20, sticky=EW)
    infoBtn.grid(row=2, column=0)

    info_Title.config(anchor=CENTER, font=(
        'Comic Sans MS', 20, 'bold'), bg="#252422", fg="#ccc5b9")
    info1.config(anchor=CENTER, font=('Comic Sans MS', 12),
                 bg="#252422", fg="#ccc5b9")
    infoBtn.config(anchor=CENTER, font=('Comic Sans MS', 12), bg="#252422",
                   fg="#ccc5b9", activebackground="#eb5e28", activeforeground="#ccc5b9", border=0)


btnStart = Button(root, text='Start', command=lambda: StartCounter(lbTime))
btnReset = Button(root, text='Reset', command=reset)
btnExit = Button(root, text='Exit', command=root.destroy)
btnInfo = Button(root, text="Info", command=info)


def clickEnt(args):
    inEntry.delete(0, 'end')

mystring = StringVar()
inEntry = Entry(root, textvariable=mystring)
inEntry.insert(0, 'Ide írja a szó színét')
inEntry.bind("<Button-1>", clickEnt)

menu = StringVar(root)
menu.set("? szín")
drop = OptionMenu(root, menu, "1 szín", "2 szín", "3 szín",
                  "4 szín", "5 szín", "6 szín", "7 szín", "8 szín", "9 szín")
drop.config(bg="#252422", fg="#ccc5b9",
            activebackground="#eb5e28", activeforeground="#ccc5b9")
drop["menu"].config(bg="#252422", fg="#ccc5b9",
                    activebackground="#eb5e28", activeforeground="#ccc5b9")

myDict = {
    'Zöld': 2818934,  #1cbd22
    'Piros': 2195024,  #db3218
    'Kék': 11153230,  #0b99e6
    'Rózsaszín': 255120181,  #ff78b5
    'Narancs': 2551490,  #ff9500
    'Citrom': 2462550,  #f6ff00
    'Lila': 12718199,  #7f12c7
    'Cián': 23173176,  #17adb0
    'Bíbor': 14423150,  #901796
}

color_lst = [(key, value) for key, value in myDict.items()]

rndName = random.choice(color_lst)
rndRGB = random.choice(color_lst)

def gameActual(event):
    global score, mScore, rndName, rndRGB
    UserText = inEntry.get()
    if UserText == rndRGB[0] :
        lbNotif.config(text = "Helyes! +1pont")
        score += 1
        if score > mScore:
            mScore = score
        lbRoundScore.config(text = score)
        lbMaxScore.config(text= mScore)
    else:
        lbNotif.config(text= "Tévedtél, válasz '%s' volt" %  rndRGB[0])

    rndName = random.choice(color_lst)
    rndRGB = random.choice(color_lst)
    if rndRGB[1] == 2818934:
        lbWord.config(fg='#1cbd22')
    elif rndRGB[1] == 2195024:
        lbWord.config(fg='#db3218')
    elif rndRGB[1] == 11153230:
        lbWord.config(fg='#0b99e6')
    elif rndRGB[1] == 255120181:
        lbWord.config(fg='#ff78b5')
    elif rndRGB[1] == 2551490:
        lbWord.config(fg='#ff9500')
    elif rndRGB[1] == 2462550:
        lbWord.config(fg='#f6ff00')
    elif rndRGB[1] == 12718199:
        lbWord.config(fg='#7f12c7')
    elif rndRGB[1] == 23173176:
        lbWord.config(fg='#17adb0')
    elif rndRGB[1] == 14423150:
        lbWord.config(fg='#901796')
    lbWord.config(text=rndName[0])

    return
   
        

def gameStart():
    lbWord.config(text=rndName[0])
    if rndRGB[1] == 2818934:
        lbWord.config(fg='#1cbd22')
    elif rndRGB[1] == 2195024:
        lbWord.config(fg='#db3218')
    elif rndRGB[1] == 11153230:
        lbWord.config(fg='#0b99e6')
    elif rndRGB[1] == 255120181:
        lbWord.config(fg='#ff78b5')
    elif rndRGB[1] == 2551490:
        lbWord.config(fg='#ff9500')
    elif rndRGB[1] == 2462550:
        lbWord.config(fg='#f6ff00')
    elif rndRGB[1] == 12718199:
        lbWord.config(fg='#7f12c7')
    elif rndRGB[1] == 23173176:
        lbWord.config(fg='#17adb0')
    elif rndRGB[1] == 14423150:
        lbWord.config(fg='#901796')

    
    inEntry.bind('<Return>', gameActual)




btnStart = Button(root, text='Start', command=lambda: [
                  StartCounter(lbTime), gameStart()])
btnReset = Button(root, text='Reset', command=reset)
btnExit = Button(root, text='Exit', command=root.destroy)


lbWord = Label(root, text="")
lbNotif = Label(root, text="Visszajelzés")

lbTime = Label(root, text="Timer")
lbTitle = Label(root, text="Színátváltó")
lb01 = Label(root, text="Max pont:")
lb02 = Label(root, text="Jelenlegi pont:")
lbMaxScore = Label(root, text=mScore)
lbRoundScore = Label(root, text=score)




'''
root.columnconfigure(0, weight = 0)
root.columnconfigure(1, weight = 0)
root.columnconfigure(2, weight = 1)
root.columnconfigure(3, weight = 0)
'''


lbTitle.grid(row=0, column=2, padx=30)
lb01.grid(row=1, column=0, sticky=W, padx=10)
lb02.grid(row=2, column=0, sticky=W, padx=10)
lbMaxScore.grid(row=1, column=1)
lbRoundScore.grid(row=2, column=1)
lbTime.grid(row=1, column=3)

inEntry.grid(row=3, column=2, ipadx=40, ipady=5, sticky=W)
drop.grid(row=3, column=3, sticky=W)

btnStart.grid(row=4, column=2, pady=10, sticky=W)
btnReset.grid(row=4, column=2, pady=10)
btnExit.grid(row=4, column=2, pady=10, sticky=E)
btnInfo.grid(row=4, column=3)
lbNotif.grid(row=5, column=2, columnspan=3)
lbWord.place(relx=0.20,  rely=0.65,  anchor=N)


TitleFont = tkinter.font.Font(
    family='Comic Sans MS',
    weight='bold',
    size=20,
)

SimpleFont = tkinter.font.Font(
    family='Comic Sans MS',
    size=12,
)


lbTitle.config(anchor=CENTER, font=TitleFont, bg="#252422", fg="#ccc5b9")
lbTime.config(font=SimpleFont, bg="#252422", fg="#ccc5b9")
lb01.config(font=SimpleFont, bg="#252422", fg="#ccc5b9")
lb02.config(font=SimpleFont, bg="#252422", fg="#ccc5b9")
lbMaxScore.config(font=SimpleFont, bg="#252422", fg="#eb5e28")
lbRoundScore.config(font=SimpleFont, bg="#252422", fg="#ccc5b9")
lbWord.config(font=('Comic Sans MS', 20, 'bold'), bg="#252422", fg="#ccc5b9")
lbNotif.config(font=SimpleFont, bg="#252422", fg="#ccc5b9")
btnStart.config(font=SimpleFont, bg="#252422", fg="#ccc5b9",
                activebackground="#eb5e28", activeforeground="#ccc5b9", border=0)
btnReset.config(font=SimpleFont, bg="#252422", fg="#ccc5b9",
                activebackground="#eb5e28", activeforeground="#ccc5b9", border=0)
btnExit.config(font=SimpleFont, bg="#252422", fg="#ccc5b9",
               activebackground="#eb5e28", activeforeground="#ccc5b9", border=0)
btnInfo.config(font=SimpleFont, bg="#252422", fg="#ccc5b9",
               activebackground="#eb5e28", activeforeground="#ccc5b9", border=0)


root.mainloop()
