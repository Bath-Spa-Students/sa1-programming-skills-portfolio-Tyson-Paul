name=input("Please Enter your Name:")
hometown=input("Please Enter your Hometown:")

#To ensure the input given by the user is a number
while True:
    try:
        age=int(input("Please Enter your Age:"))
        break
    except ValueError:
        print("Invalid. Please Enter a numerical value for Age.")


Bio ={"Name": name,"Hometown":hometown,"Age": age}
print(Bio["Name"])
print(Bio["Hometown"])
print(Bio["Age"])