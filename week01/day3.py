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

# Angry boss. Write an angry boss program that rudely asks what you want.
# Whatever you answer, the angry boss should yell it back to you and then fire you.
# For example, if you type in I want a raise, it should yell back like this:
# WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!
request = input("WHAT ON EARTH DO YOU WANT ")
print(" WHADDAYA MEAN " + "\"" + request.upper() + "\"?!? YOU'RE FIRED!!");

# Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
# Table of Contents 
# Chapter 1: Getting Started        page 1
# Chapter 2: Numbers                page 9
# Chapter 3: Letters                page 13

title = "Table of Contents"
chapter_1 = "Chapter 1: Getting Started"
chapter_1_page = "page 1"
chapter_2 = "Chapter 2: Numbers"
chapter_2_page = "page 9"
chapter_3 = "Chapter 3: Letters"
chapter_3_page = "page 13"

print(title)
print()
print(chapter_1.ljust(30, ' ') + chapter_1_page)
print(chapter_2.ljust(30, ' ') + chapter_2_page)
print(chapter_2.ljust(30, ' ') + chapter_3_page)

# Generate random number in Python
import random
print (random.randint(1, 100))