from tkinter import *
from tkinter.ttk import *


def RunGraphicUserInterface():
    def Tk_Quit(event=None):
        TkWindow.quit()
    
    TkWindow = Tk()
    TkWindow.geometry('+100+100')
    TkWindow.resizable(False, False)
    TkWindow.bind('<Escape>', Tk_Quit)

    LabelFrameAddressBar = LabelFrame(text='Input Address')
    LabelFrameAddressBar.pack(fill=BOTH)

    EntryAddressBar = Entry(LabelFrameAddressBar, width=40)
    EntryAddressBar.pack()

    Button(LabelFrameAddressBar, command=OpenFile, text='Select Dir')

    TkWindow.mainloop()

    
