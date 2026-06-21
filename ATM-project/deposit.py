from tkinter import *
from tkinter import messagebox

def activate():
    sub_root=Toplevel()
    sub_root.geometry("1920x1080")
    sub_root.title("Deposit section")
    sub_root.config(bg="#121212")
    label=Label(sub_root,text="Welcome to the deposit section !!",font=("Garamond",60,'bold'),bg="#121212",fg="white")
    label.pack(pady=60)

    main_frame=Frame(sub_root,bg="ivory")
    main_frame.pack(pady=20)
    label1=Label(main_frame,text="Enter the amount to deposit :",font=("Garamond",40,'bold'),bg="ivory",fg="black")
    label1.pack(pady=40)

    entry=Entry(main_frame,fg="black",bg="white",font=("Garamond",30,'bold'),width=15)
    entry.pack(pady=20)

    btn_frame=Frame(sub_root,bg="#121212")
    btn_frame.pack(pady=20)

    def btn1_fxn():
        entry.delete(0,END)
        entry.insert(0,"500 RS.")
    def btn2_fxn():
        entry.delete(0,END)
        entry.insert(0,"1000 RS.")
    def btn3_fxn():
        entry.delete(0,END)
        entry.insert(0,"2000 RS.")
    def btn4_fxn():
        entry.delete(0,END)
        entry.insert(0,"5000 RS.")

    btn1=Button(btn_frame,text="500 Rs.",bg="ivory",fg="black",width=10,font=("Garamond",30,'bold'),command=btn1_fxn)
    btn1.pack(side=LEFT)
    btn2=Button(btn_frame,text="1000 Rs.",bg="ivory",fg="black",width=10,font=("Garamond",30,'bold'),command=btn2_fxn)
    btn2.pack(side=LEFT,padx=20)

    btn2_frame=Frame(sub_root,bg="#121212")
    btn2_frame.pack(pady=10)

    btn3=Button(btn2_frame,text="2000 Rs.",bg="ivory",fg="black",width=10,font=("Garamond",30,'bold'),command=btn3_fxn)
    btn3.pack(side=LEFT)
    btn4=Button(btn2_frame,text="5000 Rs.",bg="ivory",fg="black",width=10,font=("Garamond",30,'bold'),command=btn4_fxn)
    btn4.pack(side=LEFT,padx=20)


    btn3_frame=Frame(sub_root,bg="#121212")
    btn3_frame.pack(pady=10)

    def deposit():
        amount=entry.get()
        if amount=="":
            messagebox.showerror("Error!!","Enter valid number!!")
        else:
            with open("depositdatabase.txt","a") as file:
              file.write(amount + "\n")
            messagebox.showinfo("Hurray!!","Amount deposited successfully")
            sub_root.destroy()
        

    btn5=Button(btn3_frame,text="Deposit",bg="ivory",fg="black",font=("Garamond",30,'bold'),command=deposit)
    btn5.pack(side=LEFT,padx=20)

    sub_root.deiconify()