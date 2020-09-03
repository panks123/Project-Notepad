from tkinter import *
from tkinter import ttk
from tkinter import font
from functools import partial
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os


fontStyle="corbel"
fontSize=12

def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    textArea.delete(1.0,END)

def setDark():
    global themebgColor
    global themefgColor
    global themeInsertbgColor
    themebgColor = "Black"
    themeInsertbgColor = "White"
    themefgColor = "White"
    textArea.configure(bg=f"{themebgColor}", insertbackground=f"{themeInsertbgColor}", fg=f"{themefgColor}")


def setBright():
    global themebgColor
    global themefgColor
    global themeInsertbgColor
    themebgColor = "White"
    themeInsertbgColor = "Black"
    themefgColor = "Black"
    textArea.configure(bg=f"{themebgColor}", insertbackground=f"{themeInsertbgColor}", fg=f"{themefgColor}")


def getFont(fontBox,new_root):
    # global fontStyle
    # fontStyle=fontBox.get().lower()
    # new_root.destroy()
    # print(fontStyle)
    # global fontSize
    # fontSize=50
    print("Not Working")
    new_root.destroy()

def setFont():
    new_root=Tk()
    new_root.title("Fonts")
    new_root.wm_iconbitmap("notepad.ico")
    ttk.Label(new_root, text="Select Font Type: ",
              font=("Times New Roman", 15)).grid(column=0,
                                                 row=2, padx=10, pady=25)
    fonts = list(font.families())
    fonts.sort()
    font_type = StringVar()
    fontBox = ttk.Combobox(new_root, width=27, textvariable=font_type, font=("Times New Roman", 12))
    fontBox['values'] = tuple(fonts)
    fontBox.grid(row=2, column=1, pady=25)
    fontBox.current(1)
    btn=Button(new_root,text="Ok", font=("Times New Roman", 15), command=partial(getFont,fontBox,new_root), bg="cyan")
    btn.grid(row=3,column=1,pady=20)
    new_root.mainloop()



def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        textArea.delete(1.0,END)
        f=open(file,"r")
        textArea.insert(1.0,f.read())
        f.close()


def saveFile():
    global file
    if file== None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                               filetypes=[("All Files", "*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            # save as a new file
            f=open(file,"w")
            f.write(textArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file+"-Notepad"))
            # print("file saved")
    else:
        # save the file
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    textArea.event_generate(("<<Cut>>"))  # tkinter internally handles this command


def copy():
    textArea.event_generate(("<<Copy>>"))


def paste():
    textArea.event_generate(("<<Paste>>"))

def selectall():
    textArea.event_generate(("<<SelectAll>>"))


def about():
    import tkinter.messagebox as tmsg
    tmsg.showinfo("Notepad","This is a notepad created by Pankaj Kumar\n\n"+" "+u"\u00a9"+"Pankaj Kumar 2020")


if __name__ == '__main__':
    root = Tk()
    root.geometry("740x640")
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("notepad.ico")
    textArea=Text(root,font=f"{fontStyle} {fontSize}")
    textArea.pack(expand=True,fill=BOTH)
    themebgColor="White"
    themeInsertbgColor="Black"
    themefgColor="Black"
    textArea.configure(bg=f"{themebgColor}", insertbackground=f"{themeInsertbgColor}",fg=f"{themefgColor}")
    file=None

    MenuBar=Menu(root)
    fileMenu=Menu(MenuBar,tearoff=False)

    # file Menu
    fileMenu.add_command(label="New",command=newFile)
    fileMenu.add_command(label="Open",command=openFile)
    fileMenu.add_command(label="Save",command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=fileMenu)

    # edit Menu

    editMenu=Menu(MenuBar,tearoff=False)
    editMenu.add_command(label="Cut",command=cut)
    editMenu.add_command(label="Copy",command=copy)
    editMenu.add_command(label="Paste",command=paste)
    editMenu.add_command(label="Select All",command=selectall)
    MenuBar.add_cascade(label="Edit",menu=editMenu)

    # view menu
    viewMenu = Menu(MenuBar, tearoff=False)
    fontMenu = Menu(viewMenu,tearoff=False)
    fonts = list(font.families())
    fonts.sort()

    viewMenu.add_command(label="Fonts",command=setFont)
    themeMenu = Menu(viewMenu, tearoff=False)
    themeMenu.add_command(label="Dark theme", command=setDark)
    themeMenu.add_command(label="Bright theme", command=setBright)
    viewMenu.add_cascade(label="Theme", menu=themeMenu)
    MenuBar.add_cascade(label="View", menu=viewMenu)
    root.config(menu=MenuBar)

    # help menu

    helpMenu=Menu(MenuBar,tearoff=False)
    helpMenu.add_command(label="About",command=about)
    MenuBar.add_cascade(label="Help",menu=helpMenu)
    root.config(menu=MenuBar)

    scrollbar=Scrollbar(textArea)
    textArea.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=textArea.yview)
    scrollbar.pack(side=RIGHT,fill=Y)

    root.mainloop()
