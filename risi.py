import tkinter as tk
from tkinter import * 

def save_info():
    sourceip_info = f"Source IP : {sourceip.get()}"
    sourceport_info= f"Source Port : {sourceport.get()}"
    destinationip_info = f"Destination IP : {destinationip.get()}"
    destinationport_info = f"Destination Port : {destinationport.get()}"
    comment_info = f"Comment : {comment.get()}"
    print (sourceip_info,sourceport_info,destinationip_info,destinationport_info,comment_info)

    file = open("soc.txt", 'a')
    file.write("\n")
    file.write(sourceip_info)
    file.write("\n")
    file.write(sourceport_info)
    file.write("\n")
    file.write(destinationip_info)
    file.write("\n")
    file.write(destinationport_info)
    file.write("\n")
    file.write(comment_info)
    file.write("\n")
    file.write("_____________________")
    file.write("\n")
    file.close()

    sourceip_entry.delete(0,END)
    sourceport_entry.delete(0,END)
    destinationip_entry.delete(0,END)
    destinationport_entry.delete(0,END)
    comment_entry.delete(0,END)

root = tk.Tk()
root.title('Form')
canv = tk.Canvas(width= 500, height= 500)
canv.pack()

sourceip = Label(text="Source IP : ")
sourceip.place(x=10,y=50)
sourceip = StringVar()
sourceip_entry = Entry(textvariable = sourceip)
sourceip_entry.place(x=10,y=70,width="300")

sourceport = Label(text = "Source Port : ")
sourceport.place(x=10,y=100)
sourceport = StringVar()
sourceport_entry = Entry(textvariable = sourceport)
sourceport_entry.place(x=10,y=120,width="300")

destinationip = Label(text = "Destination IP : ")
destinationip.place (x=10,y=150)
destinationip = StringVar()
destinationip_entry = Entry(textvariable = destinationip)
destinationip_entry.place(x=10,y=170,width="300")

destinationport = Label(text = "Destination Port : ")
destinationport.place(x=10,y=200)
destinationport = StringVar()
destinationport_entry = Entry(textvariable = destinationport)
destinationport_entry.place(x=10,y=220,width="300")

comment = Label(text="Comment : ")
comment.place(x=10,y=250)
comment = StringVar()
comment_entry = Entry(textvariable = comment)
comment_entry.place(x=10,y=270,width="300")

submit = Button(text="Submit",command=save_info)
submit.place(x=250,y = 300)

root.mainloop()
