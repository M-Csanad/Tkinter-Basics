from tkinter import *
import tkinter.font
from datetime import datetime



counter = 0
timer = False

def counter_label(lbTime):
    def count():
        if timer == True:
            global counter
            if counter == 0:
                display="00:00"
            else:
                date = datetime.fromtimestamp(counter)
                string = date.strftime("%M:%S")
                display=string
            lbTime.config(text=display)
            lbTime.after(1000, count)
            counter += 1
    count()

def StartCounter(lbTime):
    global timer
    timer = True
    counter_label(lbTime)
    
    

def info():
    global TitleFont
    root_info=Tk()
    root_info.title("Információ")
    root_info.geometry("520x300")
    root_info.resizable(False, False)
    root_info.eval('tk::PlaceWindow . center')
    root_info.configure(background='#252422')

    '''TitleFont = tkinter.font.Font(
    family = 'Comic Sans MS', 
    weight = 'bold', 
    size = 20,
    )'''
    
    info_Title=Label(root_info, text="Színátváltó")
    info_Title.config(anchor=CENTER, font = TitleFont, bg="#252422", fg="#ccc5b9")
    info_Title.grid(row=0, column=2)

    '''info1=Label(root_info, text="1.: 9 szín közül lehet választani.")
    info2=Label(root_info, text="2.: A Start gomb lenyomásával indíthatod a játékot.")
    info3=Label(root_info, text="3.: Mindig azt a színt írd le ")'''

    






def reset():
    global counter, timer, btnStart
    if timer >= 0:
        timer=False
        counter=0
        timer=0
        lbTime.config(text='00:00')
    else:
        timer=True
    btnStart['state'] = 'normal'




root = Tk()
root.title("Main Window")
root.geometry("500x300")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.configure(background='#252422')


lbTime = Label(root, text="Timer")
lbTitle = Label(root, text="Színátváltó")
lb01 = Label(root, text="Max pont:")
lb02 = Label(root, text="Jelenlegi pont:")
lbMaxScore = Label(root, text="x")
lbRoundScore = Label(root, text="x")

btnStart = Button(root, text='Start', command=lambda:StartCounter(lbTime))
btnReset = Button(root, text='Reset', command=reset)
btnExit = Button(root, text='Exit', command=root.destroy)
btnInfo = Button(root, text="Info", command=info)



def clickEnt(*args):
    inEntry.delete(0, 'end')

inEntry = Entry(root)
inEntry.insert(0, 'Ide írja a szó színét')
inEntry.bind("<Button-1>", clickEnt)

myDict = {
        'zöld' : '#1cbd22',
        'piros' : '#db3218',
        'kék' : '#0b99e6',
        'rózsaszín' : '#ff78b5',
        'narancs' : '#ff9500',
        'citrom' : '#f6ff00', 
        'lila' : '#7f12c7',
        'cián' : '#17adb0',
        'bíbor' : '#901796'
    }
color_lst = list(myDict.items())


def game():
    UserText = inEntry.get()
    
    

btnStart = Button(root, text='Start', command=lambda:StartCounter(lbTime))
btnReset = Button(root, text='Reset', command=reset)
btnExit = Button(root, text='Exit', command=root.destroy)

menu = StringVar(root)
menu.set("? szín")
drop = OptionMenu(root, menu, "1 szín", "2 szín", "3 szín", "4 szín", "5 szín", "6 szín", "7 szín", "8 szín", "9 szín")
drop.config(bg="#252422", fg="#ccc5b9", activebackground="#eb5e28", activeforeground="#ccc5b9")
drop["menu"].config(bg="#252422", fg="#ccc5b9", activebackground="#eb5e28", activeforeground="#ccc5b9")



lbWord = Label(root, text="Színes Szöveg")
lbNotif = Label(root, text="Visszajelzés")

'''
root.columnconfigure(0, weight = 0)
root.columnconfigure(1, weight = 0)
root.columnconfigure(2, weight = 1)
root.columnconfigure(3, weight = 0)
'''



lbTitle.grid(row=0, column=2)
lb01.grid(row=1, column=0, sticky=W, padx=10)
lb02.grid(row=2, column=0, sticky=W, padx=10)
lbMaxScore.grid(row=1, column=1)
lbRoundScore.grid(row=2, column=1)
lbTime.grid(row=1, column=4, padx=10)

inEntry.grid(row=3, column=2, ipadx=20, ipady=5, sticky=E)
drop.grid(row=3, column=3, sticky=W)

btnStart.grid(row=4, column=2, pady=10, sticky=W)
btnReset.grid(row=4, column=2, pady=10)
btnExit.grid(row=4, column=2, pady=10, sticky=E)
lbWord.grid(row=5, column=2, sticky=EW)
lbNotif.grid(row=5, column=3, sticky=E)
btnInfo.grid(row=4, column=3)


TitleFont = tkinter.font.Font(
    family ='Comic Sans MS', 
    weight = 'bold', 
    size = 20,
)

SimpleFont = tkinter.font.Font(
    family ='Comic Sans MS', 
    size = 12,
)


lbTitle.config(anchor=CENTER, font = TitleFont, bg="#252422", fg="#ccc5b9")
lbTime.config(font = SimpleFont, bg="#252422", fg="#ccc5b9")
lb01.config(font = SimpleFont, bg="#252422", fg="#ccc5b9")
lb02.config(font = SimpleFont, bg="#252422", fg="#ccc5b9")
lbMaxScore.config(font = SimpleFont, bg="#252422", fg="#eb5e28")
lbRoundScore.config(font = SimpleFont, bg="#252422", fg="#ccc5b9")
lbWord.config(font = SimpleFont, bg="#252422", fg="#ccc5b9")
lbNotif.config(font = SimpleFont, bg="#252422", fg="#ccc5b9")
btnStart.config(font = SimpleFont, bg="#252422", fg="#ccc5b9", activebackground="#eb5e28", activeforeground="#ccc5b9", border=0)
btnReset.config(font = SimpleFont, bg="#252422", fg="#ccc5b9", activebackground="#eb5e28", activeforeground="#ccc5b9", border=0)
btnExit.config(font = SimpleFont, bg="#252422", fg="#ccc5b9", activebackground="#eb5e28", activeforeground="#ccc5b9", border=0)
btnInfo.config(font = SimpleFont, bg="#252422", fg="#ccc5b9", activebackground="#eb5e28", activeforeground="#ccc5b9", border=0)











root.mainloop()