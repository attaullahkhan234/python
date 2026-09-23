from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title("My Photo Album")
window.geometry("400x380")


title = Label(window, text="My Photo Album", fg="white", bg="purple", width=40)
title.pack(pady=10)
img_file = Image.open("pizza.png")
img_file = img_file.resize((300,180))
photo = ImageTk.PhotoImage(img_file)
pic_label = Label(window, image=photo)
pic_label.pack(pady=10)



def show_message():
    messagebox.showinfo("Message", "Welcome to my photo album!")
msg_button = Button(window, text="click to react", bg="blue", fg="white", command=show_message)
msg_button.pack(pady=5)


def show_details():
    top = Toplevel(window)
    top.title("Photo Details")
    top.geometry("200x120")
    info = Label(top, text="taken on: 1 june 2025")
    info.pack(pady=10)
    place = Label(top, text="location: my garden")
    place.pack(pady=10)
    top.mainloop()
details_btn = Button(window, text="click to see details", bg="green", fg="white", command=show_details)
details_btn.pack(pady=5)

window.mainloop()