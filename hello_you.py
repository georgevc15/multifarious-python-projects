# Ask user for name

name = input("What is your name?: ")

# Ask user for age
age = input("How old are you?: ")

# Ask for the city
city = input("What city do you live in?: ")

# Ask user what the enjoy
love = input("What do you love doing?: ")

# Create output text
string = "Your names is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name,age,city,love)

# Print output to screen
print(output)
