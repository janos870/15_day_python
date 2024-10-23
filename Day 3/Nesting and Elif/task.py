print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is you age?"))
    if age <= 14:
        bill = 5
        print("Children ticket are $5 ")
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7 ")
    else:
        bill = 12
        print("Adult ticket are $12 ")

    wants_photo = input("Do you wat to have a photo take? Type y for Yes or n for No.")

    if  wants_photo == "y":
        bill += 3

    print(f"Your fine bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
