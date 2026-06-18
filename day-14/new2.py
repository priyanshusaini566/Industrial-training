from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox


def sign_pg():
    new2_root=Toplevel()
    new2_root.geometry("1920x1080")
    new2_root.title("Sign up")
    new2_root.config(bg="#E8DCC4")

    main_frame=Frame(new2_root,bg="ivory")
    main_frame.pack(pady=10)

    img = Image.open(r"C:\Users\LENOVO\Downloads\Gemini_Generated_Image_22te3r22te3r22te.png")
    img=img.resize((300,300))
    photoimg= ImageTk.PhotoImage(image=img)
    label=Label(main_frame,image=photoimg)
    label.pack(pady=10)
    label.image = photoimg

    user_frame=Frame(main_frame,bg="ivory")
    user_frame.pack(pady=10)
    user_label=Label(user_frame,text="username",bg="ivory",fg="black",font=("Arial",20,'bold'))
    user_label.pack(side=LEFT)
    entry=Entry(user_frame,fg="black",bg="linen",font=("Arial",20,'bold'))
    entry.pack(padx=10)

    pass_frame=Frame(main_frame,bg="ivory")
    pass_frame.pack(pady=10)
    pass_label=Label(pass_frame,text="password",bg="ivory",fg="black",font=("Arial",20,'bold'))
    pass_label.pack(side=LEFT)
    entry2=Entry(pass_frame,fg="black",bg="linen",font=("Arial",20,'bold'),show="*")
    entry2.pack(padx=10)

    mob_frame=Frame(main_frame,bg="ivory")
    mob_frame.pack(pady=10)
    mob_label=Label(mob_frame,text="mobile    ",bg="ivory",fg="black",font=("Arial",20,'bold'))
    mob_label.pack(side=LEFT)
    entry3=Entry(mob_frame,fg="black",bg="linen",font=("Arial",20,'bold'))
    entry3.pack(padx=10)

    em_frame=Frame(main_frame,bg="ivory")
    em_frame.pack(pady=10)
    em_label=Label(em_frame,text="email      ",bg="ivory",fg="black",font=("Arial",20,'bold'))
    em_label.pack(side=LEFT)
    entry4=Entry(em_frame,fg="black",bg="linen",font=("Arial",20,'bold'))
    entry4.pack(padx=10)

    def register():
        username=entry.get().strip()
        password=entry2.get().strip()
        mobile=entry3.get().strip()
        email=entry4.get().strip()

        if username == "" or password == "":
          messagebox.showerror(
            "Error!",
            "Enter username and password"
        )
          return

        with open("user.txt","a") as file:
            file.write(f"{username},{password},{mobile},{email}\n")

        messagebox.showinfo("successful","Registration successful")

        new2_root.destroy()

        
    

    button=Button(main_frame,text="Register",font=("Arial",20,'bold'),width=10,fg="yellow",bg="black",command=register)
    button.pack()


    
    

    new2_root.mainloop()

