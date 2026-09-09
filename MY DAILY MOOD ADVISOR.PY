name = input("Enter YOUR name: ")
mood = input("How are you feeling today? (good, bad, okay) ")
energy_level = input("What is your energy level today? (low, medium, high) ")

if mood == "good" and energy_level == "high":
    print("You are feeling great! Go outside and enjoy your day.")

elif mood == "good" and energy_level == "medium":
    print("You are doing well. Have a productive day!")

elif mood == "good" and energy_level == "low":
    print("You are feeling good but tired. Take it easy today.")

elif mood == "okay" and energy_level == "high":
    print("You have plenty of energy. Try something fun!")

elif mood == "okay" and energy_level == "medium":
    print("Take a balanced day and do what feels comfortable.")

elif mood == "okay" and energy_level == "low":
    print("You seem a little tired. Get some rest.")

elif mood == "bad" and energy_level == "high":
    print("You have energy, so try doing something you enjoy.")

elif mood == "bad" and energy_level == "medium":
    print("Take some time to relax and do something you like.")

else:
    print("You seem tired and not feeling great. Take some rest.")


import datetime
import calendar

now = datetime.datetime.now()
print("Time now:", now)

print(calendar.calendar(now.year))