from tkinter import *
import os


def new():
    popup = Tk()
    popup.wm_title("Nouvelle langue")
    popup.iconbitmap("Assets/logoSCALP.ico")
    label = Label(popup, text="Donnez un nom à votre langue", font='Arial')
    label.pack(side="top", fill="x", pady=10)
    lang = Entry(popup, text='lol')
    lang.pack()

    def mySuperFolder(self):
        wrd = 'Saves/' + lang.get()
        if lang.get() == '' \
                or lang.get().find("!") != (-1) \
                or lang.get().find(".") != (-1) \
                or lang.get().find(";") != (-1) \
                or lang.get().find("*") != (-1) \
                or lang.get().find("/") != (-1) \
                or lang.get().find(">") != (-1) \
                or lang.get().find("<") != (-1) \
                or lang.get().find("|") != (-1) \
                or lang.get().find("?") != (-1) \
                or lang.get().find("/") != (-1) \
                or lang.get().find("\"") != (-1):
            popup.destroy()
            new()
        else:
            os.makedirs(wrd)
            dicoFileName = wrd + '/_dico.txt'
            dicoFile = open(dicoFileName, 'a')
            dicoFile.close()
            dicoGramName = wrd + '/_gram.txt'
            dicoGram = open(dicoGramName, 'a')
            dicoGram.close()
            dicoDescrName = wrd + '/_descr.txt'
            dicoDescr = open(dicoDescrName, 'a')
            dicoDescr.close()
            dicoAlphabetName = wrd + '/_alph.txt'
            dicoAlph = open(dicoAlphabetName, 'a')
            dicoAlph.close()
            popup.destroy()

    B1 = Button(popup, text='Ok', command=lambda: mySuperFolder())
    popup.bind('<Return>', mySuperFolder)
    B1.pack()
    popup.mainloop()