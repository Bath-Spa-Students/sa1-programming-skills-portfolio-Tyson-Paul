#Start a loop that prompts the user to enter for pizza toppings
while True:
    toppings = input("Enter a pizza topping (or 'quit' to stop): ")

    #If the user enters 'quit', break the loop
    if toppings.lower() == 'quit':
        print("Stopping the pizza topping selection.")
        break

    #Otherwise, add the topping to the pizza
    print(f"Adding {toppings} to your pizza.")