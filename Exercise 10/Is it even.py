def main_fun():
    # Main function that asks the user for a number
    try:
        user = int(input("Enter a number: "))
        
        # Passing the input to the function
        result = even_or_odd(user)
        print(result)

    except ValueError:
        print("Invalid input. Enter a valid number.")


def even_or_odd(num):
    # Function to check if the number entered by the user is even or odd
    if num % 2 == 0:
        return f"The number {num} is even."
    else:
        return f"The number {num} is odd."


# Calling the main function to run the program
if __name__ == "__main__":
    main_fun()