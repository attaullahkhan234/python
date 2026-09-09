# My Travel Ticket Counter

destination = "Barcelona"
passenger_name = "Khan"
ticket_price = 25
number_of_tickets = 3

print("Travel Ticket Details")
print("---------------------")

print("Passenger:", passenger_name)
print("Destination:", destination)
print("Ticket price:", ticket_price, "euros")
print("Number of tickets:", number_of_tickets)

# Calculate total cost
total_cost = ticket_price * number_of_tickets

print("Total cost:", total_cost, "euros")

# Compare values
if number_of_tickets > 1:
    print("You have booked multiple tickets.")
else:
    print("You have booked one ticket.")

# Work with text
print("Destination in uppercase:", destination.upper())
print("Passenger name length:", len(passenger_name))

# Swap two ticket prices
ticket1 = 20
ticket2 = 35

print("\nBefore swapping:")
print("Ticket 1:", ticket1)
print("Ticket 2:", ticket2)

ticket1, ticket2 = ticket2, ticket1

print("\nAfter swapping:")
print("Ticket 1:", ticket1)
print("Ticket 2:", ticket2)