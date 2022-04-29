from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import filedialog
from Cleaner import Cleaner, LevelupCleaner
from makeZip import makeZip
import os

def RunGraphicUserInterface():
    def Tk_Quit(event=None):
        TkWindow.quit()
    
    TkWindow = Tk()
    TkWindow.title("Maplestory Screenshot Cleaner")
    TkWindow.geometry("+%d+%d" % (TkWindow.winfo_screenwidth()/2, TkWindow.winfo_screenheight()/2))
    TkWindow.resizable(False, False)
    TkWindow.bind('<Escape>', Tk_Quit)

    # AddressBar
    LabelFrameAddressBar = LabelFrame(text='Input Address')
    LabelFrameAddressBar.pack(fill=BOTH)

    EntryAddressBar = Entry(LabelFrameAddressBar, width=80)
    EntryAddressBar.pack()

    def OpenDirectory():
        DirectoryName = filedialog.askdirectory(title='Select the path of the screenshot')
        if not DirectoryName:
            EntryAddressBar.delete(0, END)
        EntryAddressBar.insert(0, DirectoryName)

    ButtonSelectDir = Button(LabelFrameAddressBar, command=OpenDirectory, text='Select Dir')
    ButtonSelectDir.pack(side=LEFT)

    def RunCleaner():
        if not os.path.isdir(EntryAddressBar.get()):
            messagebox.showinfo('info', '잘못된 경로')
            return
        if not CheckbuttonLevelupCheck.get():
            Cleaner(EntryAddressBar.get())
        else:
            LevelupCleaner(EntryAddressBar.get())

        if CheckbuttonLZipCheck.get():
            makeZip(EntryAddressBar.get())

    ButtonRunCleaner = Button(LabelFrameAddressBar, command=RunCleaner, text='Run Cleaner')
    ButtonRunCleaner.pack(side=LEFT)


    # OptionBar
    LabelFrameOptionBar = LabelFrame(text='Option')
    LabelFrameOptionBar.pack(fill=BOTH)

    CheckbuttonLevelupCheck = IntVar()
    CheckbuttonLevelupOption = Checkbutton(LabelFrameOptionBar, text='Levelup Check', variable=CheckbuttonLevelupCheck)
    CheckbuttonLevelupOption.pack(fill=BOTH)

    CheckbuttonLZipCheck = IntVar()
    CheckbuttonZipOption = Checkbutton(LabelFrameOptionBar, text='Add Zip File', variable=CheckbuttonLZipCheck)
    CheckbuttonZipOption.pack(fill=BOTH)

    TkWindow.mainloop()

    
