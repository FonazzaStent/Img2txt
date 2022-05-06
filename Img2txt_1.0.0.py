import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import base64
import os

#Create app window
def create_app_window():
        global top
        global root
        img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAACXBIWXMAAC4jAAAuIwF4pT92AAAAB3RJTUUH5gUCDjsz59y24AAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAANFSURBVEjH7VZLTBNRFD3P6QxSNv5YsBkJLqpWExMjloUx0UhiS6vERhRsEcLHxKgLte0wLbUKfkLUlUaqgXSosX5iTbXGuDDhE4skGjeiMbE7ZAGoC+zQYGdcjCJWbAeEnWc1d9597+Te8+69j0iShIXEIiwwFpxAk2anUqlo9HFHQHg9+G7GDQes5U2cS6vVqiQgaRpEIg+POpsy79lXbml282o5pN9hKd/D6vRDQ0PSTFi5eh2r07M6vcPFjY+PSyqQroGSmYKCgswRhMIR35mWRCIxaw3UoNnNAwiFI4SQrLn6K0EqlXoUjXYGumTItdX2MpOJoihlSavVTnHIsuz1uDNw/JXgUTR6zMkr38ecPEB2WcyKWbhm/ZTb7QcPaZpuOe2bdR10BroAPH/2NPbsKYBOQQBQZ6v80zN49/7cNSC/mzzn4jnX9D/To5ldBDXVdgAl20pLtpUCqLHb5qeSp1BmMhKgQxAgo6baVmYyzTMBRVEWi9nyU1gAoihevHQ5JUmOE8dzc3P/lQBAIpG40NYGGU7HSUJI69lzwXthABMTosft1qrj0GQ4/XRLaygcATCRTNIaTfBe2Go2UhR1635ElqGUWL29co4EF9raQuFIxW4zIUShsZqNPm8zIUQpsRyG8Z3y8hwHIB6Px/r7Yy8GBl6+2mXcyTdx2QkYmrFXWF2OkwAYmv6W+sZzXF5eHgCvx704J4dhGABjY5/ar/v9gZu/+vHjJ9MJ0rup0iwldUgkxL37q1id3nawprunZ3DwLavTHz5ydLqPZs6jamzsk7229s37DwButF+jabq3rw+AYXPx/IzMdr9fOR0ATdOTk5M3OjoBGAyGf23XAD7E437h5taS4kKWZXIYAKHbd7pjAw32qlVFRZkmmkoNuoJBVqfv7umRJCmZTAaELlan37HTNDIymmWibVi7GsDH4eHMEcT6BwDkr8jv7eurazzkaT2vKyr0X72yfPmyuQ/9elulcv9EUdyyvXT085eppQZ7VWNDw5+nz6CByWQE0CEIr9/M/GwRRdF3pmX085f8pUsMmzYaNheXGAxFaXnPoEFWeLzeH6+Kr1/V+M/6FjE0U11hdTodKpsd+f/4zYbvB6JTsody90AAAAAASUVORK5CYII='
        root= tk.Tk()
        top= root
        top.geometry("600x450+468+138")
        top.resizable(1,1)
        top.title("Image to Text")
        favicon=tk.PhotoImage(data=img) 
        root.wm_iconphoto(True, favicon)

#Textbox
def create_textbox():
        global textbox
        textbox = Text(top)
        textbox.place(relx=0.033, rely=0.022, relheight=0.918, relwidth=0.933)
        scroll_1=Scrollbar (top)
        scroll_1.pack(side=RIGHT, fill=Y)
        textbox.configure(yscrollcommand=scroll_1.set)
        scroll_1.configure(command=textbox.yview)
        textbox.configure(state=DISABLED)

#Open File
def open_file():
    global imgfile
    global imgfilename
    data=[('BMP', '*.bmp')]
    imgfilename=askopenfilename(filetypes=data)
    if str(imgfilename)!='':
        imgfile=open(imgfilename,'rb')
        encode()

#encode
def encode():
    global imgtext
    imgtext=''
    imgfile.seek(225)
    filename=str(imgfilename)
    imgfile_size= os.path.getsize(filename)
    for pixels in range (1,imgfile_size-225):
        bytea=imgfile.read(1)
        bytevalue=int.from_bytes(bytea, "big")
        char=chr(int(bytevalue)+97)
        imgtext=imgtext+char
    textbox.configure(state=NORMAL)
    textbox.delete(1.0,END)
    textbox.insert(INSERT,imgtext[0:20000])
    textbox.configure(state=DISABLED)

#Copy Code
def copy_text():
    textbox.tag_add(SEL, "1.0", END)
    textbox.event_generate(("<<Copy>>"))

#Save to file
def Save_to_file():
        data=[('Text','*.txt')]
        reportfile=asksaveasfilename(filetypes=data, defaultextension=data)
        if str(reportfile)!='':
              reportfilesave=open(reportfile,'w')
              reportfilesave.write(imgtext)
              reportfilesave.close()

#Quit
def QuitApp():
    okcancel= messagebox.askokcancel("Quit?","Do you want to quit the app?",default="ok")
    if okcancel== True:
        top.destroy()

#menu
def create_menu():
    menubar=tk.Menu(top, tearoff=0)
    top.configure(menu=menubar)
    sub_menu=tk.Menu(top, tearoff=0)
    menubar.add_cascade(menu=sub_menu,compound="left", label="File")
    sub_menu.add_command(compound="left", label="Open", command=open_file)
    sub_menu.add_command(compound="left",label="Copy", command=copy_text)
    sub_menu.add_command(compound="left",label="Save", command=Save_to_file)
    sub_menu.add_command(compound="left",label="Quit", command=QuitApp)
    top.bind_all("<Control-o>",open_file_hotkey)
    top.bind_all("<Control-c>",copy_hotkey)
    top.bind_all("<Control-s>",Save_hotkey)
    top.bind_all("<Control-q>",Quit_hotkey)

def open_file_hotkey(event):
    open_file()

def copy_hotkey(event):
    copy_text()

def Save_hotkey(event):
    Save_to_file()

def Quit_hotkey (event):
    QuitApp()

#contextmenu
def context_menu(event):
        try:
                menucopy.tk_popup(event.x_root, event.y_root)
        finally:
                menucopy.grab_release()
def create_context_menu():
        global menucopy
        root.bind("<Button-3>", context_menu)
        menucopy = Menu(root, tearoff = 0)
        menucopy.add_command(label="Copy", command=copy_text)

#main procedure
def main():
    create_app_window()
    create_textbox()
    create_menu()
    create_context_menu()


main()
root.mainloop()
