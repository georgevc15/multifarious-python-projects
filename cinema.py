films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,1],
    "Ghost Busters":[12,5]
    }

while True:

    choise = input("What film would to like to wath?: ").strip().title()

    if choise in films:
        age = int(input("How old are you?: ").strip())

        #check user age
        if age >= films[choise][0]:

            #check enough seats
            num_seats  = films[choise][1]    

            if num_seats > 0:
                print("Enjoy the film!")
                films[choise][1] = films[choise][1] - 1
            else:
                print("Sorry, we are sold out!")
        else:
            print("Tou are too young to see that film")
    else:
        print("We don't have that film...")
