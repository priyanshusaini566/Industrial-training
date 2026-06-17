from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from signup import signup_pg
import os
import ast

# Function to display the successful login dashboard screen
def open_dashboard(username):
    # Hide the main login window completely
    root.withdraw()
    
    # Create the new dashboard window
    dashboard_root = Toplevel()
    dashboard_root.geometry("1920x1080")
    dashboard_root.title("Dashboard")
    dashboard_root.config(bg="black")
    
    # Handle closing the dashboard window (closes the entire app cleanly)
    dashboard_root.protocol("WM_DELETE_WINDOW", root.destroy)
    
    # Main content container frame
    dash_frame = Frame(dashboard_root, bg='lavender')
    dash_frame.pack(pady=100, padx=50)
    
    # Re-displaying your generated image on the new page
    try:
        img_dash = Image.open(r"C:\Users\LENOVO\OneDrive\Desktop\industrial training\day-12\images\Gemini_Generated_Image_w9s74mw9s74mw9s7.png")
        img_dash = img_dash.resize((500, 300))
        photoimg_dash = ImageTk.PhotoImage(image=img_dash)
        
        label_img = Label(dash_frame, image=photoimg_dash, bg='black', pady=10)
        label_img.pack(pady=20)
        # Keep a reference to prevent garbage collection
        label_img.image = photoimg_dash
    except Exception as e:
        print(f"Image load failed in dashboard: {e}")
        
    # Welcome message with user's name
    welcome_label = Label(
        dash_frame,
        text=f"Welcome Back,\n{username}!",
        fg='black',
        bg='lavender',
        font=("Poppins", 28, 'bold'),
        justify=CENTER
    )
    welcome_label.pack(pady=20)
    
    status_label = Label(
        dash_frame,
        text="Login Successful",
        fg='green',
        bg='lavender',
        font=("Arial", 20, 'bold')
    )
    status_label.pack(pady=10)
    
    # Optional Logout button to go back to the login page
    def logout():
        dashboard_root.destroy()
        root.deiconify() # Bring back login window
        user_entry.delete(0, END)
        pass_entry.delete(0, END)

    btn_logout = Button(
        dash_frame,
        text="Logout",
        fg='white',
        bg='crimson',
        font=("Arial", 16, 'bold'),
        bd=5,
        relief='raised',
        command=logout
    )
    btn_logout.pack(pady=20)


# Login authentication verification function
def verify_login():
    username_input = user_entry.get().strip()
    password_input = pass_entry.get().strip()
    
    if username_input == "" or password_input == "":
        messagebox.showwarning("Incomplete Fields", "Please enter both username and password.")
        return

    if not os.path.exists("user_details.txt"):
        messagebox.showerror("Error", "No registered users found. Please sign up first.")
        return

    try:
        with open("user_details.txt", "r") as file:
            data = file.read()
            user_dict = ast.literal_eval(data)
            
            if username_input == user_dict.get('username') and password_input == user_dict.get('password'):
                # POP-UP REMOVED: Directly opening the dashboard window now
                open_dashboard(username_input)
            else:
                messagebox.showerror("Failed", "Invalid Username or Password.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not read registration file: {e}")

root = Tk()
root.geometry("1920x1080")
root.title("Login")
root.config(bg="black")

main_frame = Frame(root, bg='lavender')
main_frame.pack(pady=100)

try:
    img = Image.open(r"C:\Users\LENOVO\OneDrive\Desktop\industrial training\day-12\images\Gemini_Generated_Image_w9s74mw9s74mw9s7.png")
    img = img.resize((500, 300))
    photoimg = ImageTk.PhotoImage(image=img)

    label = Label(main_frame, image=photoimg, bg='black', pady=10)
    label.pack(pady=10)
except Exception as e:
    print(f"Image load failed in login: {e}")

user_frame = Frame(main_frame, bg='lavender')
user_frame.pack()

user_label = Label(
    user_frame,
    text="username",
    fg='black',
    bg='lavender',
    font=("Poppins", 20, 'bold')
)
user_label.pack(side=LEFT)

user_entry = Entry(user_frame, font=("Arial", 20, 'bold'))
user_entry.pack(padx=10)

pass_frame = Frame(main_frame, bg="lavender")
pass_frame.pack(pady=10)

pass_label = Label(
    pass_frame,
    text="password",
    fg='black',
    bg='lavender',
    font=("Arial", 20, 'bold')
)
pass_label.pack(side=LEFT)

pass_entry = Entry(
    pass_frame,
    font=("Arial", 20, 'bold'),
    show="*"
)
pass_entry.pack(padx=10)

def open_signup():
    signup_pg()

btn_frame = Frame(main_frame, bg='lavender')
btn_frame.pack(pady=10)

btn_login = Button(
    btn_frame,
    text="Login",
    fg='white',
    bg='powderblue',
    font=("Arial", 20, 'bold'),
    bd=8,
    relief='raised',
    width=10,
    command=verify_login
)
btn_login.pack(side=LEFT)

btn_signup = Button(
    btn_frame,
    text="Sign up",
    fg='white',
    bg='sky blue',
    font=("Arial", 20, 'bold'),
    bd=8,
    relief='raised',
    width=10,
    command=open_signup
)
btn_signup.pack(padx=10)

root.mainloop()