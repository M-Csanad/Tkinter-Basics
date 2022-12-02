from tkinter import *
import time

root = Tk()
root.title("Main Window")
root.geometry("500x400")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.configure(background='#0c2327')

lb00 = Label(root, text="Színátváltó")
lb01 = Label(root, text="Max pont:")
lb02 = Label(root, text="Jelenlegi pont:")
lbMaxScore = Label(root, text="x")
lbRoundScore = Label(root, text="x")
lbTime = Label(root, text="01:15")


entResult = Entry(root, text="Eredmény")
lbWord = Label(root, text="Színes Szöveg")
lbNotif = Label(root, text="Visszajelzés")

lb01.grid(row=0, column=0, sticky=W)
lb02.grid(row=1, column=0, sticky=W)















root.mainloop()