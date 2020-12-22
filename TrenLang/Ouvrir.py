from tkinter import *
import os


def selectlang(arg):
    global currentLang
    currentLang = arg


def ouvrir():
    ouvrirWindow = Tk()
    if 1 < len(os.listdir('Saves')):
        Choice = Button(ouvrirWindow, text=os.listdir('Saves')[1],
                        command=lambda: selectlang(os.listdir('Saves')[1]))
        Choice.pack()
    if 2 < len(os.listdir('Saves')):
        Choice = Button(ouvrirWindow, text=os.listdir('Saves')[2],
                        command=lambda: selectlang(os.listdir('Saves')[2]))
        Choice.pack()
    if 3 < len(os.listdir('Saves')):
        Choice = Button(ouvrirWindow, text=os.listdir('Saves')[3],
                        command=lambda: selectlang(os.listdir('Saves')[3]))
        Choice.pack()
    if 4 < len(os.listdir('Saves')):
        Choice = Button(ouvrirWindow, text=os.listdir('Saves')[4],
                        command=lambda: selectlang(os.listdir('Saves')[4]))
        Choice.pack()
    if 5 < len(os.listdir('Saves')):
        Choice = Button(ouvrirWindow, text=os.listdir('Saves')[5],
                        command=lambda: selectlang(os.listdir('Saves')[5]))
        Choice.pack()
    if True:

        if 6 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[6],
                            command=lambda: selectlang(os.listdir('Saves')[6]))
            Choice.pack()
        if 7 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[7],
                            command=lambda: selectlang(os.listdir('Saves')[7]))
            Choice.pack()
        if 8 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[8],
                            command=lambda: selectlang(os.listdir('Saves')[8]))
            Choice.pack()
        if 9 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[9],
                            command=lambda: selectlang(os.listdir('Saves')[9]))
            Choice.pack()
        if 10 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[10],
                            command=lambda: selectlang(os.listdir('Saves')[10]))
            Choice.pack()
        if 11 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[11],
                            command=lambda: selectlang(os.listdir('Saves')[11]))
            Choice.pack()
        if 12 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[12],
                            command=lambda: selectlang(os.listdir('Saves')[12]))
            Choice.pack()
        if 13 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[13],
                            command=lambda: selectlang(os.listdir('Saves')[13]))
            Choice.pack()
        if 14 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[14],
                            command=lambda: selectlang(os.listdir('Saves')[14]))
            Choice.pack()
        if 15 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[15],
                            command=lambda: selectlang(os.listdir('Saves')[15]))
            Choice.pack()
        if 16 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[16],
                            command=lambda: selectlang(os.listdir('Saves')[16]))
            Choice.pack()
        if 17 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[17],
                            command=lambda: selectlang(os.listdir('Saves')[17]))
            Choice.pack()
        if 18 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[18],
                            command=lambda: selectlang(os.listdir('Saves')[18]))
            Choice.pack()
        if 19 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[19],
                            command=lambda: selectlang(os.listdir('Saves')[19]))
            Choice.pack()
        if 20 < len(os.listdir('Saves')):
            Choice = Button(ouvrirWindow, text=os.listdir('Saves')[20],
                            command=lambda: selectlang(os.listdir('Saves')[20]))
            Choice.pack()

    ouvrirWindow.mainloop()
