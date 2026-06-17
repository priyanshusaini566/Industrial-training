from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("1920x1080")
root.title("Login")
root.config(bg="black")

# Main Frame
main_frame = Frame(root, bg='lavender')
main_frame.pack(pady=100)

# Image
img = Image.open(
    r"C:\Users\LENOVO\OneDrive\Desktop\industrial training\day-12\images\Gemini_Generated_Image_w9s74mw9s74mw9s7.png"
)
img = img.resize((500, 300))
photoimg = ImageTk.PhotoImage(img)

label = Label(main_frame, image=photoimg, bg='black')
label.pack(pady=10)

# Username
user_frame = Frame(main_frame, bg='lavender')
user_frame.pack(pady=5)

user_label = Label(
    user_frame,
    text="Username",
    fg='black',
    bg='lavender',
    font=("Poppins", 20, 'bold')
)
user_label.pack(side=LEFT)

user_entry = Entry(user_frame, font=("Arial", 20, 'bold'), width=25)
user_entry.pack(padx=10)

# Email
email_frame = Frame(main_frame, bg='lavender')
email_frame.pack(pady=5)

email_label = Label(
    email_frame,
    text="Email",
    fg='black',
    bg='lavender',
    font=("Poppins", 20, 'bold')
)
email_label.pack(side=LEFT)

email_entry = Entry(email_frame, font=("Arial", 20, 'bold'), width=25)
email_entry.pack(padx=10)

# Phone Number
phone_frame = Frame(main_frame, bg='lavender')
phone_frame.pack(pady=5)

phone_label = Label(
    phone_frame,
    text="Phone",
    fg='black',
    bg='lavender',
    font=("Poppins", 20, 'bold')
)
phone_label.pack(side=LEFT)

phone_entry = Entry(phone_frame, font=("Arial", 20, 'bold'), width=25)
phone_entry.pack(padx=10)

# Password
pass_frame = Frame(main_frame, bg="lavender")
pass_frame.pack(pady=5)

pass_label = Label(
    pass_frame,
    text="Password",
    fg='black',
    bg='lavender',
    font=("Arial", 20, 'bold')
)
pass_label.pack(side=LEFT)

pass_entry = Entry(
    pass_frame,
    font=("Arial", 20, 'bold'),
    show="*",
    width=25
)
pass_entry.pack(padx=10)

# Buttons
btn_frame = Frame(main_frame, bg='lavender')
btn_frame.pack(pady=20)

btn_login = Button(
    btn_frame,
    text="Login",
    fg='white',
    bg='powderblue',
    font=("Arial", 20, 'bold'),
    bd=8,
    relief='raised',
    width=10
)
btn_login.pack(side=LEFT)

btn_signup = Button(
    btn_frame,
    text="Sign Up",
    fg='white',
    bg='sky blue',
    font=("Arial", 20, 'bold'),
    bd=8,
    relief='raised',
    width=10
)
btn_signup.pack(side=LEFT, padx=10)

root.mainloop()