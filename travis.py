known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi! My name is Travis")
    name = input('What is your name?: ').strip().capitalize()

    if name in known_users:
        output = "Hello {}".format(name)
        print(output)
        remove = input("Would you like to be removed from the system (y/n): ").lower();

        if remove == "y":
            known_users.remove(name)
        
    else:
        print("name NOT recognised")
