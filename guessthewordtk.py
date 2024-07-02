from tkinter import *
root=Tk()
root.minsize(650,650)
root.configure(background="lightblue")

l1=Label(root,text="WIERDLE")
l1.place(relx=0.45,rely=0.05, anchor=CENTER)

input_field=Entry(root)
input_field.place(relx=0.6, rely=0.05, anchor=CENTER)

ca=Label(root)
root.mainloop()
