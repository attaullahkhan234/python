from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()

window.title("My Profile With Photo")
window.geometry("500x550")

# Main title
profile_title = Label(
    window,
    text="My Profile With Photo",
    fg="white",
    bg="blue",
    width=48
)
profile_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Name
name_label = Label(window, text="Name:", fg="black", bg="white")
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = Entry(window, fg="blue", bg="lightyellow", width=25)
name_entry.grid(row=1, column=1, padx=10, pady=5)

# Hobby
hobby_label = Label(window, text="Hobby:", fg="black", bg="white")
hobby_label.grid(row=2, column=0, padx=10, pady=5)

hobby_entry = Entry(window, fg="blue", bg="lightyellow", width=25)
hobby_entry.grid(row=2, column=1, padx=10, pady=5)

# Photo album title
album_title = Label(
    window,
    text="My Photo Album",
    fg="black",
    bg="yellow",
    width=40
)
album_title.grid(row=3, column=0, columnspan=2, pady=10)

# Image
img_file = Image.open("football.png")
img_file = img_file.resize((300, 180))

photo = ImageTk.PhotoImage(img_file)

pic_label = Label(window, image=photo)
pic_label.grid(row=4, column=0, columnspan=2, pady=10)


# Message button
def show_message():
    messagebox.showinfo(
        "Message",
        "Thank you for visiting my profile!"
    )


msg_button = Button(
    window,
    text="Click to react",
    bg="red",
    fg="white",
    command=show_message
)
msg_button.grid(row=5, column=0, columnspan=2, pady=5)


# Details window
def show_details():

    top = Toplevel(window)

    top.title("Profile Details")
    top.geometry("400x200")

    info = Label(
        top,
        text="This is a simple photo of my hobby.",
        wraplength=350
    )
    info.pack(pady=10)

    info2 = Label(
        top,
        text="This is a professional photo of football.",
        wraplength=350
    )
    info2.pack(pady=10)

    info3 = Label(
        top,
        text="This match was played between 2 teams in 2025.",
        wraplength=350
    )
    info3.pack(pady=10)


details_btn = Button(
    window,
    text="Click to see details",
    bg="green",
    fg="white",
    command=show_details
)

details_btn.grid(row=6, column=0, columnspan=2, pady=5)


window.mainloop()