# Write a program that tells you the following:

# Hours in a year. How many hours are in a year?
# (Assuming a non-leap year)
hours_in_a_year = 365 * 24
print("There are " + str(hours_in_a_year) + " hours in a year.\n")


# Minutes in a decade. How many minutes are in a decade?
minutes_in_a_decade = 10 * 365 * 24 * 60
print("There are " + str(minutes_in_a_decade) + " minutes in a decade.\n")


# Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
my_age_in_seconds = 25 * 365 * 24 * 60 * 60
print("My age in seconds is " + str(my_age_in_seconds) + "\n")


# Andreea Visanoiu​: I'm 48618000 seconds old hahaha. Calculate @Andreea Visanoiu's age.
age = 48618000 / (365 * 24 * 60 * 60)
print("Andreea's age is " + str(age) + " years\n")

# How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?
# Ref: https://en.wikipedia.org/wiki/Year_2038_problem
# Assuming 1 millisecond increment
# with 32 bits, the maximum number of milliseconds is (2 ^ 32) -1
# 1 day has 24 hrs * 60 mins * 60 seconds * 1000 milliseconds
days_to_32_bit_sys_timeout = (2 ** 32 - 1) / (1000 * 60 * 60 * 24)
print("It takes " + str(round(days_to_32_bit_sys_timeout)) + " days for a 32-bit system to timeout if it has a bug with integer overflow")
# How many days does it take for a 64-bit system to timeout, if it has a bug with integer overflow?
days_to_64_bit_sys_timeout = (2 ** 64 - 1) / (1000* 60 * 60 * 24)
print("It takes " + str(round(days_to_64_bit_sys_timeout)) + " days for a 64-bit system to timeout if it has a bug with integer overflow")

# Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need Python modules.
import datetime
my_birthdate = datetime.datetime(1993, 5, 18, 12, 0, 0)
date_today = datetime.datetime.now()
dates_diff = date_today - my_birthdate

print("My age today is " + str(dates_diff.days // 365))