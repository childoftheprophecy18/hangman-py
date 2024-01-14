# HANGMAN 

# TODO 5-1: update the word list to ud=se the word_list from hangman_words.py
# word_list = ["luffy", "zoro", "sanji", "chopper", "brook", "jinbei", "usopp", "robin", "nami"]
import hangman_words #from hangman_words import word_list

# TODO 1-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(hangman_words.word_list) # chosen_word = random.choice(word_list)

print(f"The chosen word is: {chosen_word}")  # Print the chosen word

#TODO 4-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

# TODO 5-3 :- import the logo from hangman.py
from hangman import logo
print(logo)
 
# TODO 2-1 :- Create an empty list called display 
# for each letter in the choosen_word, add a "-" to 'display'.
#so if the choosen word is was "luffy", display should be []"-","-","-","-","-"] with 5 "-" representing each lwtter to guess

display = []
word_length = len(chosen_word)
for _ in range(len(chosen_word)):
    display += "_"

# TODO 3 :-using a while loop to let the user guess again . The loop should only stop once when the user has correctly guessed all the letters in chosen_word and 'display' has no more "_" blanks,, then we can tell they won.

end_of_game = False

while not end_of_game:

    
# TODO 1-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    
    guess = input("Guess a letter: ").lower()

    # TODO 5-4:- if the user already entered a letter thry already entered/guessed,print the letter and let them know
    if guess in display:
        print(f"you already guessed: {guess}") 

    # TODO 2-2 :- Loop through each position in the choosen word;
    # if the letter at that position matches 'guess' the reveal that letter in display at that position.
    # e.g : if the user guessed "u" and choosen word was "luffy", then display should be ["-","u","-","-","-"]. 

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(f"Current Position : {position} \nCurrent letter : {letter} \nguessed letter : {guess} ")
        if letter == guess:
            display[position] = letter
        # else:
        #     print("Wrong")


    # TODO 1-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    # for letter in (chosen_word):
    #     if letter == guess:
    #         print("Right")
    #     else:
    #         print("Wrong")

    #TODO 4-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        
        # TODO 5-5:- if the letter is not in chosen word ,print out the letter and let them know its. not in the word. 
        print(f"you guessed {guess}, tthats not in the word. you loose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you loose")

    # join all the elemens in the list and turn it into string
    print(f"{''.join(display)}")   


    #TODO 2-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    # print(display)

    if "_" not in  display:
        end_of_game = True
        print("you win")

    # TODO 5-2: import the stages from hangman.py,, reduce err
    from hangman import stages    
        
    # TODO 4-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])