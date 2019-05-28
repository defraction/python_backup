import random
#%run Hangman/He_Yoo_Hangman.py
def hangman_display(guessed, secret):
    '''Takes every character in the guessed string, which is all of your
    characters that you guess will be in the secret, and appends it to the end
    of the guess_char list that is empty at the start, then for every letter in 
    the secret it checks it against the guess_char list and if they are the same
    then it prints out the letter, but if it is not then it will print out a '-'
    or if it is a space then it will print out a space, every letter is printed
    side by side since there is a trailing comma'''
    disp_word = ''
    for secret_letter in secret:
        if secret_letter in guessed:
            disp_word += secret_letter
        elif secret_letter == ' ':
            disp_word += ' '
        else:
            disp_word += '-'
    return disp_word

import random
def hangman():
    '''Takes in the raw input of a single character and then will run every
    char for guessed input such that if the character matches any in the secret
    it will print the word, but if not then it will print out a - to indicate
    that the character in the word has not yet been found, once all of the
    letters in secret has been completed then it will tell you that you have won
    the game, but if you run out of guesses then it will end the game and tell
    you that you have lost'''
    x = 'redo'
    print('Only use single lowercase letters to guess the word.')
    print('If you type more than one letter, regardless of if it is correct, you will lose.')
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    secret_word_list = ('string', 'float', 'list', 'integer', 'print', 'return')
    secret = random.choice(secret_word_list)
    print secret
    guessed_letters = []
    guesses = 0
    guessed = secret
    display = ''
    for char in secret:
            if char != ' ':
                display += '-'
            else:
                display += ' '
    print(display)
    guessed = raw_input("Start off with your first guess: ")
    if len(secret) <= 5:
        guesses = 2
    if len(secret) > 5:
        guesses = 0
    if len(secret) > 7:
        guesses = -2
    if len(guessed) > 1:
        print('You can not do that.')
        guesses = 10
    if guesses !=10:
        display = ''
        for char in guessed:
            guessed_letters.append(char)
            if char.lower() not in alphabet:
                print('No special characters.')
                guesses -= 1
        for char in secret:
            if char.upper() in guessed_letters or char.lower() in guessed_letters:
                display += char
            elif char != ' ':
                display += '-'
            else:
                display += ' '
    if guesses < 10:
        print(display)
    lose = 0
    while guesses < 8:
        display = ''
        if guesses != 1:
            print('You have ' + str(8 - guesses) + ' guesses left.')
        else:
            print('You have ' + str(8 - guesses) + ' guesses left.')
        guessed = raw_input("Guess again: ")
        if len(guessed) > 1:
            print('You can not do that.')
            break
        for char in guessed:
            guessed_letters.append(char)
            if char not in alphabet:
                print('No special characters.')
                guesses -= 1
            if char.upper() not in secret.upper():
                guesses += 1
        for char in secret:
            if char.upper() in guessed_letters or char.lower() in guessed_letters:
                display += char
            elif char != ' ':
                display += '-'
            else:
                display += ' '
        print(display)
        if display.upper() == secret.upper():
            print('You win the game!')
            lose = 1
            break
    if lose == 0:
        print('You lost!') 
        print('The actual word was: ' + secret)
    def retry():
        '''This function runs based on whether the user wants to play again or
        not and if the user does wants to play again, then the game will be 
        launched again, otherwise it will be exit the game. Also, if the user 
        types in something else that is not valid when they are asked about 
        retrying, they will be asked to type either yes or no'''
        retry = raw_input("Would you like to play again? Enter YES or NO: ")
        if retry.upper() == 'Y' or retry.upper() == 'YES':
            hangman()
            x = 'nope'
            return(x)
        elif retry.upper() == 'N' or retry.upper() == 'NO':
            x = 'nope'
            print('Thank you for playing!')
            return(x)
        else:
            print('Please enter YES or NO.')
            x = 'do it'
            return(x)
    while x == 'redo':
        x = retry()
        
hangman()