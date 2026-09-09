city = input("Enter the city name: ")
temp = float(input("Enter today's temperature in C: "))

if temp > 35:
    print("Warning: it is very hot today")

if temp > 25:
    print("It is a warm day today")

if temp > 15:
    print("it is a great day to go outside")
else:
    print("Grab a jacket before you go outside")


if temp > 35:
    print("Weather: Scorching hot")
elif temp > 25:
    print("Weather: Warm and sunny")
elif temp > 15:
    print("Weather: cool and breezy")
else:
    print("weather: cold - stay warm")



import datetime
import calendar

now = datetime.datetime.now()
print("city:", city)
print("Time now:", now)

print(calendar.calendar(now.year))