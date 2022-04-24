from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from Cleaner import Cleaner, LevelupCleaner

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
        if CheckbuttonLevelupCheck.get() == 0:
            Cleaner(EntryAddressBar.get())
        else:
            LevelupCleaner(EntryAddressBar.get())

    ButtonRunCleaner = Button(LabelFrameAddressBar, command=RunCleaner, text='Run Cleaner')
    ButtonRunCleaner.pack(side=LEFT)


    # OptionBar
    LabelFrameOptionBar = LabelFrame(text='Option')
    LabelFrameOptionBar.pack(fill=BOTH)

    CheckbuttonLevelupCheck = IntVar()
    CheckbuttonLevelupOption = Checkbutton(LabelFrameOptionBar, text='Levelup Check', variable=CheckbuttonLevelupCheck)
    CheckbuttonLevelupOption.pack(fill=BOTH)

    TkWindow.mainloop()

    
