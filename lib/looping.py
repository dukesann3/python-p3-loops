#!/usr/bin/env python3
import ipdb

def happy_new_year():

    reversed_range = list(reversed(range(1,11)))

    for i in reversed_range:
        print(f"{i}")
    
    print("Happy New Year!")

def square_integers(int_list):

    squared_list = []
    for int_in_list in int_list:
        squared_list.append(int_in_list**2)

    return squared_list

def fizzbuzz():

    for count in range(1,101):
        if count % 5 == 0 and count % 3 == 0:
            print("FizzBuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print("Buzz")
        else:
            print(f"{count}")


