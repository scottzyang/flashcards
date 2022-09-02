"""
We have basically five steps:

Setup the cards data that we want to quiz ourselves with
Write code that reads the cards data and parses it into a python dictionary
Write code that iterates over the cards
Get the users's input for each question
Check the users input against the answer
Display "Correct!" or "Incorrect!"

"""
# JSON is a module/file that is read and parsed into a dta format that python understands: a Dictionary
# import the json module from python3
import json

# open the file and parse the JSON
with open('me-capitals.json', 'r') as f: # open json file to read, contents of file passed into open function as variable f
    data = json.load(f) # loads contents of the JSON file and parse it from json into a dictionary called 'data'

# access the data dictionary, and print all values within the cards key
# for i in data["cards"]:
    # print(i)

# define function for flashcard game
def flash_cards():
    score = 0

    # access the data dictionary, into the cards key
    for i in data["cards"]: 
        guess = input(i["q"] + " > ") # access "q" within the index of cards dictionary, assign to guess variable and print. data -> cards -> i -> "q"

        if guess.lower() == i["a"].lower(): # if the lower case version of input matches the lowercase version of the actual answer value
            print("Correct!")
            score += 1
        else:
            print("Incorrect! the answer was", i["a"])

    print(f"Your score was {score} out of 5!")

    # request user input if they would like to play again
    play_again = input("Would you like to play again? (Yes or No) ")

    # calls flashcard function again to initiate game
    if play_again.lower() == "yes":
        flash_cards()
    else:
        return

# initiates the flashcard game
flash_cards()

# potential issue is stack-overflow depending on how often the function is re-called


# JSON - JavaScript Object Notation
# Format for storing and transporting data
# Often used when data is sent from a server to a webpage

# Python dictionaries are pythons form of JSON