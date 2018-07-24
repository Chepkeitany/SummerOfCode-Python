# Full name greeting.
# Write a program that asks for a person’s first name, then middle, and then last.
# Finally, it should greet the person using their full name.

first_name = input("What's your first name? ")
middle_name = input("What's your middle name? ")
last_name = input("What's your last name? ")

full_name = first_name + " " + middle_name + " " + last_name
print("Hello " + full_name)

# Bigger, better favorite number. Write a program that asks for a person’s favorite number.
# Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)

guess = input("What's your favourite number? ")

better_guess = int(guess) + 1

print("I think " + str(better_guess) + " is a bigger and better favorite number");