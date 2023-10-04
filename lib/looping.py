#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i >= 0:
        if(i == 0):
            print("Happy New Year!")
            return i
        print(f"{i}")
        i = i - 1

def square_integers(int_list):
    new_list = [number * number for number in int_list]
    return new_list

def fizzbuzz():
    for e in range(100):
        e = e + 1
        if(e % 3 == 0 and e % 5 == 0):
            print("FizzBuzz")
        elif(e % 3 == 0):
            print("Fizz")
        elif(e % 5 == 0):
            print("Buzz")
        else:
            print(e)
