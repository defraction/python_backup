from __future__ import print_function
'''Procedure'''
# N/A

'''Part 1: for loops, range(), and help()'''
# 4.
def days():
    '''First, it iterates through the string 'MTWRFSS' and prints the letter + 
    day for every letter in the string. Next, it iterates through numbers 5 to 7
    and inserts the integer as a string in the string 'It is the (insert number)
    th of September'
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')

# 5.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

def picks():
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/picks')

# 6a.
def roll_hundred_pair():
    list = []
    for rolls in range(1,101):
        list += [random.choice([1,2,3,4,5,6]) + random.choice([1,2,3,4,5,6])]
        
    plt.hist(list)
    plt.savefig('1.3.7/roll_hundred_pair')

# 6b. 
def dice(n):
    sum = 0 
    for rolls in range(n):
        sum += random.randint(1,6)
    return('Roll was ' + str(sum))
    
'''Part 2: While loops'''
# 7.
def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
'''Line 2 is necessary because there needs to be a initial guess to trigger the 
while loop, also it needs to be an incorrect guess because if it is correct,
then it will just immediately print 'Thank you!'.'''

# 8.
import random

def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''The arguments in this function are 'Amy', 'Bill', 'Cathy', and 'Dale'.
    They are all string data types. This function chooses a random winner out of
    those four people and then counts the number of guess that it takes the user
    to guess the correct person. The values returned are guess again, if the user
    guesses incorrectly, or the number of tries it took the user to guess the 
    correct winner.
    '''
    winner = random.choice(players) 

    ####
    # This prints the beginning line of the code with all the players names 
    # followed by commas.
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # This runs through the amount of players.
        print(p+', ', end='')
    print(players[len(players)-1]) # This prints the players names with commas.

    ####
    # guesses is initialized at 1 guess, and while the guess is not the same as
    # the winner, every guess adds one to  the guesses variable, and when the 
    # winner is correctly guessed at the end, it prints the amount of guesses it
    # took.
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses
    
# 9.
def goguess():
    correct = random.randint(1, 20)
    print('I have a number between 1 and 20 inclusive.')
    tries = 1
    guess = 0
    while guess != correct:
        guess = int(raw_input('Guess: '))
        if guess == correct:
            print('Right! My number is ' + str(correct) + '! You guessed in ' + str(tries) + ' tries!')
        elif guess > correct:
            print(str(guess) + ' is too high.')
            guess = int(raw_input('Guess: '))
            tries += 1
        else:
            print(str(guess) + ' is too low.')
            tries += 1

# 10. You will need anywhere from 1 to 6000 guesses, because the answer will vary
# every time.

# 11a.
def matches(ticket, winners):
    common = 0
    for number in ticket:
        for win in winners:
            if number == win:
                common += 1
    return common
    
# 11b. 
def report(guess, secret):
    number_right_place = 0
    number_wrong_place = 0
    Secret_mystery = []
    Guess_mystery = []
    
    for answer in range(len(guess)):
        if guess[answer] == secret[answer]:
            number_right_place += 1
        else:
            Secret_mystery.append(secret[answer])
            Guess_mystery.append(guess[answer])
    for guess in Guess_mystery:
        for secret in Secret_mystery:
            if guess == secret:
                number_wrong_place += 1
                break
    return [number_right_place, number_wrong_place]
    
'''Conclusion'''
# 1. It can be tedious and disorganized, so it possibly may be harder to track 
# down errors.
# 2. Iteration and analysis of a large set of data are relatated because iteration
# can be used to analyze large sets of data.
# 3. A for loop goes through all of the data set, but a while loop only works 
# when a certain condition is being met and stops once the condition is not true
# anymore.
# 4. My partner and I worked well together, helping each other and asking questions
# when we had to. My strengths are that I follow the directions to do what needs
# to be met, and not under or overdo things, and something that I may need to work 
# on is to work faster and more effectively.

'''Assignment Check'''

#1.3.7 Function Test
roll_hundred_pair()
print(dice(5))
goguess()
print(matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17]))
guess = ['red','red','red','green','yellow']
secret = ['red','red','yellow','yellow','black']
print(report(guess, secret))

# I believe that I have got all the correct outputs when testing my assignment, 
# therefore, I believe that I have correctly finished this assignemnt.