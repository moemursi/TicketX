TICKET_PRICE = 10

tickets_remaining = 100

#output how many remianing tickets

print(f"There are {tickets_remaining} Tickets remaining")

#gather user name to personalize the user experience

user  = input("Please Enter your name : ")

# prompt user by name and ask how many tickets they like

no_of_tickets = input(" How many tickets would you like , {} ".format(user))
no_of_tickets = int(no_of_tickets)

#calculate total cost( no_of_tickets * price ) assign to variable cost
cost = no_of_tickets * TICKET_PRICE

#output the price to the screen

print(f"The total cost is {cost} ")