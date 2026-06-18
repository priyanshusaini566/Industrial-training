from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from new2 import sign_pg

root=Tk()
root.geometry("1920x1080")
root.title("the login page")
root.config(bg="#E8DCC4")

main_frame=Frame(root,bg="ivory")
main_frame.pack(pady=10)

img=Image.open(r"C:\Users\LENOVO\Downloads\Gemini_Generated_Image_22te3r22te3r22te.png")
img=img.resize((300,300))
photoimg=ImageTk.PhotoImage(image=img)

label=Label(main_frame,image=photoimg)
label.pack(pady=10)

user_frame=Frame(main_frame,bg="ivory")
user_frame.pack()
user_label=Label(user_frame,text="username",bg="ivory",fg="black",bd=5,font=("Arial",20))
user_label.pack(side=LEFT)
entry=Entry(user_frame,bg="linen",fg="black",font=("Arial",20),bd=3)
entry.pack(padx=10)

pass_frame=Frame(main_frame,bg="ivory")
pass_frame.pack(pady=10)
user_label2=Label(pass_frame,text="password",bg="ivory",fg="black",bd=5,font=("Arial",20))
user_label2.pack(side=LEFT)
entry2=Entry(pass_frame,bg="linen",fg="black",font=("Arial",20),bd=3)
entry2.pack(padx=10)

def btn_verify():
    username=entry.get().strip()
    password=entry2.get().strip()

    print(username,password)

def open_sign():
    sign_pg()


btn_frame=Frame(main_frame,bg="ivory")
btn_frame.pack(pady=10)

login_btn=Button(btn_frame,text="Login",width=10,relief="raised",bg="black",fg="yellow",font=("Arial",20,'bold'),command=btn_verify)
login_btn.pack(side=LEFT,padx=5)

sign_btn=Button(btn_frame,width=10,text="Sign up",bg="black",fg="yellow",relief="raised",font=("Arial",20,'bold'),command=open_sign)
sign_btn.pack(side=LEFT,padx=5)



root.mainloop()