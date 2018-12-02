# Program to generate a random number between 0 and 9

# import the random module
import random

first = input("Estramo inferiore -> ")
last = input("Estramo superiore -> ")

print(random.randint(int(first), int(last)))