from tkinter import *

window = Tk()
window.title("My personal bio")
window.geometry("400x380")

title = Label(window, text="my personal bio", fg="white", bg="blue",width=48 )
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

name_label = Label(window, text="Name:", fg="black", bg="white")
name_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = Entry(window, fg="blue", bg="lightyellow", width=25)
name_entry.grid(row=1, column=1, padx=10, pady=5)

age_label = Label(window, text="Age:", fg="black", bg="white")
age_label.grid(row=2, column=0, padx=10, pady=5)

age_entry = Entry(window, fg="blue", bg="lightyellow", width=25)
age_entry.grid(row=2, column=1, padx=10, pady=5)


country_label = Label(window, text="Country:", fg="black", bg="white")
country_label.grid(row=3, column=0, padx=10, pady=5)

country_entry = Entry(window, fg="blue", bg="lightyellow", width=25)
country_entry.grid(row=3, column=1, padx=10, pady=5)

hobby_label = Label(window, text="Hobby:", fg="black", bg="white")
hobby_label.grid(row=4, column=0, padx=10, pady=5)

hobby_entry = Entry(window, fg="blue", bg="lightyellow", width=25)
hobby_entry.grid(row=4, column=1, padx=10, pady=5)

favorite_game_label = Label(window, text="Favorite Game:", fg="black", bg="white")
favorite_game_label.grid(row=5, column=0, padx=10, pady=5)

favorite_game_entry = Entry(window, fg="blue", bg="lightyellow", width=25)
favorite_game_entry.grid(row=5, column=1, padx=10, pady=5)

favorite_skills_label = Label(window, text="Favorite Skills:", fg="black", bg="white")
favorite_skills_label.grid(row=6, column=0, padx=10, pady=5)

favorite_skills_entry = Entry(window, fg="blue", bg="lightyellow", width=25)
favorite_skills_entry.grid(row=6, column=1, padx=10, pady=5)


skills_label = Label(window, text="Skills:", fg="black", bg="white")
skills_label.grid(row=7, column=0, padx=10, pady=5)

skills_entry = Entry(window, fg="blue", bg="lightyellow", width=25)
skills_entry.grid(row=7, column=1, padx=10, pady=5)

goals_label = Label(window, text="Goals:", fg="black", bg="white")
goals_label.grid(row=8, column=0, padx=10, pady=5)

goals_entry = Entry(window, fg="blue", bg="lightyellow", width=25)
goals_entry.grid(row=8, column=1, padx=10, pady=5)

about_frame = Frame(window, relief=RAISED, borderwidth=3)
about_frame.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

about_label = Label(about_frame, text="About Me:")
about_label.pack()

about_text = Text(about_frame, height=4, width=40, fg="green", bg="lightyellow")
about_text.pack()

submit = Button(window, text="Show my bio", fg="white", bg="blue", width=20)
submit.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()