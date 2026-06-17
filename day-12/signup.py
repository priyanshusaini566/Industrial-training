from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import ast  # Safely evaluate strings containing Python literals

def register_details(username, password, mobile, email):
    if username != "" and password != "" and mobile != "" and email != "":
        # Open file in 'w' mode (overwrites or creates fresh data)
        file = open("user_details.txt", "w")
        file.write(
            str({
                'username': username,
                'password': password,
                'mobile': mobile,
                'email': email
            })
        )
        file.close()

        messagebox.showinfo(
            "Registration Successful",
            "All details are saved!"
        )
        signup_root.destroy()
    else:
        messagebox.showwarning(
            "Blank detected",
            "Kindly fill all the details!"
        )

def signup_pg():
    global signup_root
    signup_root = Toplevel()
    signup_root.geometry("1000x800")
    signup_root.title("Sign Up Screen")
    signup_root.config(bg="black")  # Changed to black to match login page style

    # Main structural frame inside the window
    main_frame = Frame(signup_root, bg='lavender')
    main_frame.pack(pady=40, padx=40)

    # Re-adding the image to the Signup page
    try:
        img = Image.open(r"C:\Users\LENOVO\OneDrive\Desktop\industrial training\day-12\images\Gemini_Generated_Image_w9s74mw9s74mw9s7.png")
        img = img.resize((400, 240))
        photoimg = ImageTk.PhotoImage(image=img)
        
        img_label = Label(main_frame, image=photoimg, bg='black')
        img_label.pack(pady=10)
        # CRITICAL: Keep a reference so the image displays properly in Toplevel
        img_label.image = photoimg 
    except Exception as e:
        print(f"Image load failed in signup: {e}")

    heading = Label(
        main_frame,
        text="Sign Up",
        font=("Arial", 26, "bold"),
        bg="lavender",
        fg="black"
    )
    heading.pack(pady=10)

    # Username Field
    user_frame = Frame(main_frame, bg="lavender")
    user_frame.pack(pady=5)
    Label(user_frame, text="Username", font=("Arial", 16, "bold"), bg="lavender", fg="black", width=10, anchor="w").pack(side=LEFT)
    username_entry = Entry(user_frame, font=("Arial", 16))
    username_entry.pack(padx=10)

    # Password Field
    pass_frame = Frame(main_frame, bg="lavender")
    pass_frame.pack(pady=5)
    Label(pass_frame, text="Password", font=("Arial", 16, "bold"), bg="lavender", fg="black", width=10, anchor="w").pack(side=LEFT)
    password_entry = Entry(pass_frame, font=("Arial", 16), show="*")
    password_entry.pack(padx=10)

    # Mobile Field
    mobile_frame = Frame(main_frame, bg="lavender")
    mobile_frame.pack(pady=5)
    Label(mobile_frame, text="Mobile", font=("Arial", 16, "bold"), bg="lavender", fg="black", width=10, anchor="w").pack(side=LEFT)
    mobile_entry = Entry(mobile_frame, font=("Arial", 16))
    mobile_entry.pack(padx=10)

    # Email Field
    email_frame = Frame(main_frame, bg="lavender")
    email_frame.pack(pady=5)
    Label(email_frame, text="Email", font=("Arial", 16, "bold"), bg="lavender", fg="black", width=10, anchor="w").pack(side=LEFT)
    email_entry = Entry(email_frame, font=("Arial", 16))
    email_entry.pack(padx=10)

    # Register Button
    Button(
        main_frame,
        text="Register",
        bg="sky blue",
        fg="white",
        font=("Arial", 18, "bold"),
        bd=5,
        relief='raised',
        width=12,
        command=lambda: register_details(
            username_entry.get().strip(),
            password_entry.get().strip(),
            mobile_entry.get().strip(),
            email_entry.get().strip()
        )
    ).pack(pady=15)