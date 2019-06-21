from main import *
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
def r():
    m = messagebox.askquestion("EXIT","Are u sure")
    if m=='yes':
        root.quit()
def k():
    if i.get() == 0:
        messagebox.showwarning("Warning", "Read about the app first")
    elif i.get() == 1:
        messagebox.showinfo("success", "U can proceed")


root = Tk()
root.geometry("700x500+450+120")
my=Font(family="Times New Roman",size=25,underline=2)
l = Label(root, text="Please read about the Application first ",bg="black",fg="white",font=my)
l.pack(fill= X)
ny=Font(family="Californian FB",size=15,weight="bold")
ty=Font(family="Californian FB",size=12,slant="italic")
bu= Button(root,text="ABOUT",bg="white",fg="black",font=ny)
bu.pack()
la= Label(root, text="Name",fg="red",font=my)
lb= Label(root, text="Age",fg="red",font=my)
en= Entry(root,fg="black",font=ty)
et= Entry(root,fg="black",font=ty)
la.pack()
en.pack()
lb.pack()
et.pack()
i=IntVar()

c= Checkbutton(root,text="I know about the Application.",fg="blue",variable=i,font=ny)
c.pack()
v=Label(root,text="Select one of them:",bg="black",fg="white",font=my)
v.pack(fill=X)
e= Button(root,text="Run using Default values.",fg="green",font=ny,command=main(1))
e.pack()
d= Button(root,text="Run using your own values.",fg="purple",font=ny,command=main())
d.pack()


f=Button(root,text="EXIT",fg="black",font=ny,command=r)
f.pack()
root.mainloop()