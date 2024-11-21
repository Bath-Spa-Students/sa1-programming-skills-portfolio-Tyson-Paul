# Void Function returns nothings . It executes the statement and prints 
# Value returning function returns takes input perform operations and return 
# function name must be descriptive like square function , random function 
# We use def keyword to create any function  # Function header 
# Be careful regarding indentation 

# Void function 
def print_message():
    print("Hello World")
# Calling function 
print_message()

# Local variable 
def print_message():
    message ="Hello World"  # Local variable 
    print(message)
# Calling function 
print_message()
# If i call this message it shows an error 

def print_message():
    message ="Hello World"  # Local variable 
    print(message)
print(message)     # message is not defined bcz local varaible life is inside of program 
print_message()


#Diffenrent functions have same local variables name - No syntax error 

def print_message():
  message ="hy"
  print(message)
  
def print_message_2():
  message ="hello"
  print(message)

print_message()
print_message_2()

# Paasing argument to variable   

def print_message_2(message):  # parameter 
  print(message)

msg ="Good Morning"
print_message_2(msg)  # Argument 

#Example  parameter x store value and get double 
def main():
    value =5
    show_double(value)
    
def show_double(x):
      print(x*2)

main()

# Passing Multiple arguments 
  #https://www.w3schools.com/python/python_functions.asp