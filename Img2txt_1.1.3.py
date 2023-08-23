"""Image to Text 1.1.3 - Convert an image to text to spot intelligible
words for philosophical-universal or psychological interpretation.
Copyright (C) 2022  Fonazza-Stent

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import base64
import os
from PIL import ImageTk, Image

#init
def init():
        global textcheck
        textcheck=0

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
    data=[('Image', '*.bmp *.jpg *.png')]
    imgfilename=askopenfilename(filetypes=data)
    if str(imgfilename)!='':
        imgfile=open(imgfilename,'rb')
        encode(imgfilename)

#encode
def encode(imgfilename):
    imgfile=Image.open(imgfilename)
    w,h=imgfile.size
    ratio=w/h
    height=30
    width=int(height*ratio)
    imgsize=width*height
    im2=imgfile.resize((width,height),Image.Resampling.BICUBIC)
    img2=im2.convert("P", palette=Image.Palette.ADAPTIVE, dither=Image.Dither.FLOYDSTEINBERG, colors=26)
    img3=im2.convert("RGB").quantize(colors=26,method=Image.Quantize.MEDIANCUT,kmeans=2,dither=Image.Dither.FLOYDSTEINBERG)
    img3=img3.convert("P",colors=26,palette=Image.Palette.ADAPTIVE)
    if os.path.isfile("image2.bmp")==True:
        os.remove("image2.bmp")
    img2.save("image2.bmp")
    if os.path.isfile("image3.bmp")==True:
        os.remove("image3.bmp")
    img3.save("image3.bmp")
    global imgtext
    global textcheck
    imgtext=''
    imgtext2=''
    image2=open("image2.bmp",'rb')
    image2.seek(1078)
    filename=str(imgfilename)
    imgfile_size= os.path.getsize("image2.bmp")
    for pixels in range (1,imgsize):
        bytea=image2.read(1)
        bytevalue=int.from_bytes(bytea, "big")
        char=chr(bytevalue+97)
        imgtext2=imgtext2+char
    imgtext2=imgtext2+"                                          "
    reversed_text=""
    for character in imgtext2:
        reversed_text=character+reversed_text
    imgtext2=imgtext2+"\n\nReverse text\n\n"+reversed_text
    #print (imgtext2)
    imgtext3=''
    image3=open("image3.bmp",'rb')
    image3.seek(1078)
    imgfile_size= os.path.getsize("image3.bmp")
    for pixels in range (1,imgsize):
        bytea=image3.read(1)
        bytevalue=int.from_bytes(bytea, "big")
        char=chr(bytevalue+97)
        imgtext3=imgtext3+char
    imgtext3=imgtext3+"                                          "
    reversed_text3=""
    for character in imgtext3:
        reversed_text3=character+reversed_text3
    #imgtext2=imgtext2+"                              "+reversed_text
    imgtext3=imgtext3+"\n\nReverse text\n\n"+reversed_text3
    imgtext="Algorithm 1\n\n"+imgtext2+"\n\n\nAlgorithm 2\n\n"+imgtext3
    textbox.configure(state=NORMAL)
    textbox.delete(1.0,END)
    textbox.insert(INSERT,imgtext[0:20000])
    textbox.configure(state=DISABLED)
    textcheck=1
    image2.close()
    image3.close()
    os.remove("image2.bmp")
    os.remove("image3.bmp")

#Copy Code
def copy_text():
    textbox.tag_add(SEL, "1.0", END)
    textbox.event_generate(("<<Copy>>"))

#Save to file
def Save_to_file():
        global imgtext
        global textcheck
        if textcheck!=1:
                imgtext=' '
        data=[('Text','*.txt')]
        reportfile=asksaveasfilename(filetypes=data, defaultextension=data)
        if str(reportfile)!='':
              reportfilesave=open(reportfile,'w')
              #imgtext=str(imgtext.encode('ascii'))
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
    sub_menu.add_command(compound="left", label="Open", command=open_file, accelerator="Alt+O")
    sub_menu.add_command(compound="left",label="Copy", command=copy_text, accelerator="Alt+C")
    sub_menu.add_command(compound="left",label="Save", command=Save_to_file,accelerator="Alt+S")
    sub_menu.add_command(compound="left",label="Quit", command=QuitApp, accelerator="Alt+Q")
    top.bind_all("<Alt-o>",open_file_hotkey)
    top.bind_all("<Alt-c>",copy_hotkey)
    top.bind_all("<Alt-s>",Save_hotkey)
    top.bind_all("<Alt-q>",Quit_hotkey)
    menubar.bind_all("<Alt-f>",menubar.invoke(1))

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
    init()
    create_app_window()
    create_textbox()
    create_menu()
    create_context_menu()


main()
root.mainloop()
