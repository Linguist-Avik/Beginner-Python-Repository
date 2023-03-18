#Hangman Game
import random

#importing wordlist from words module
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#importing logo from art module
import hangman_art
print(hangman_art.logo)
#Testing which word word
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\n\nGuess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the gussed already
    if guess in display:
      print(f"You already guessed '{guess}'.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the word.\nYou lose a life!")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #importing stages from art module
    print(hangman_art.stages[lives])