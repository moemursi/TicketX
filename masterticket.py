TICKET_PRICE = 10

tickets_remaining = 100

#output how many remianing tickets



# prompt user by name and ask how many tickets they like

while tickets_remaining >= 1:
    print(f"There are {tickets_remaining} Tickets remaining")

    # gather user name to personalize the user experience

    user = input("Please Enter your name : ")

    no_of_tickets = input(" How many tickets would you like , {} ".format(user))
    no_of_tickets = int(no_of_tickets)

    # calculate total cost( no_of_tickets * price ) assign to variable cost
    cost = no_of_tickets * TICKET_PRICE

    # output the price to the screen

    print(f"The total cost is {cost} ")
    # prompt user if they want to proceed
    should_proceed = input(" do you want to proceed ? Y/N ? ")
    # if they want to proceed ,print out to the screen (sold) to confirm purchase
    if should_proceed.lower() == 'y':
        print("SOLD !!! ")
        tickets_remaining -= no_of_tickets
    # and then decrement the tickets remaining by the numnber o fthe tickets sold
    else:
        print(f"Thank you anyways {user} ")

print("Sorry Buddy !!! All tickets sold out !!! ")



