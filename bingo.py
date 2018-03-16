import random
import csv

def list_creator(file):
    '''Builds the list of possible game squares for Bingo game.'''
    square_data = []
    for line in file:
        square_data.append(line)        #adds individual items to the list of possible call items for customized Bingo cards.
    return square_data

def bingo_caller(caller):
    '''BINGO calling engine. Takes list of square options, chooses one from those remaining.'''
    call = random.choice(caller)
    return(call)

def bingo_discard(caller, call):
    '''Removes called item from list to prevent duplicates.'''
    caller.remove(call)
    if len(caller) == 0:
        caller = "Nothing left to call"
    return caller

def main():
    csv_file = csv.reader(open(input('Enter file name, including extension:'), 'r'))
    engine = list_creator(csv_file)
    new_call = "y"
    while new_call == "y":
        choice = bingo_caller(engine)
        print(choice)
        engine = bingo_discard(engine, choice)
        new_call = input("Call another square? (y/n)")
        if new_call != "y" or engine == "Nothing left to call":
            print("Game Over!")
            break
if __name__ == "__main__":
    main()

