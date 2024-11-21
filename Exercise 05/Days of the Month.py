def is_leap_year(year):
    #It returns True if the given year is a leap year orelse it will be False 
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def years():
    #Dictionary of months and their days
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    #To ask the user for the month number
    try:
        month_number = int(input("Enter the month number (1-12): "))
        
        #To check if the input month is valid or invalid
        if month_number < 1 or month_number > 12:
            print("Invalid month number. Please enter a number between 1 and 12.")
            return
 #To check if it's a leap year when the month is February (month 2)
        if month_number == 2:
            year = int(input("Enter the year to check if it's a leap year: "))
            if is_leap_year(year):
                print("February has 29 days this year.")
            else:
                print("February has 28 days.")
        else:
            #Output the number of days for the month given by the user 
            print(f"Month {month_number} has {month_days[month_number]} days.")
    
    except ValueError:
        print("Invalid. Please enter a valid number.")
years()
