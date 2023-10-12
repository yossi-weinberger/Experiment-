pic_price = 5
roller_price = 20
slide_price = 10
ballpool_price = 5

age = int(input("Please insert your age: "))

if age >= 18:
    height = int(input("Please insert your height: "))
    if height >= 120:
        print("You can go to the roller coaster")
        pic = input("Do you want your picture taken?: ").casefold()
        if pic[0] == "y":
            print(f"You need to pay {pic_price}$ for the picture and"
                  f" {roller_price}$ for the roller coaster")
        if pic[0] == "n":
            print(f"You need to pay {roller_price}$")
    else:
        print("You can go to the slide")
        print(f"You need to pay {slide_price}$")
else:
    print("You can go to the ball pool")
    print(f"You need to pay {ballpool_price}$")
