main_frame=Frame(root,bg="#1E1E1E")
main_frame.pack(pady=10)

img=Image.open(r"C:\Users\LENOVO\Downloads\Gemini_Generated_Image_k2u9ctk2u9ctk2u9.png")
img=img.resize((400,300))
photoimg=ImageTk.PhotoImage(image=img)

main_label=Label(main_frame,image=photoimg)
main_label.pack(pady=10)