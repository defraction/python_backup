from __future__ import print_function
'''Procedure'''
# N/A

'''Part 1: Nested if Structures and Testing'''
# 1.
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
# 1a. The return value was from line 17 of the code.
# 1b1. 'orange' will cause line 15 to be executed.
# 1b2. 'apple' or 'banana' will cause line 17 to be executed.
# 1b3. 'potato' will cause line 20 to be executed.
# 1b4. If a food that is not part of any list is inserted, that will cause line
# 22 to be executed.
# 1c. Bananas will never be reported as starchy because it is part of the fruits 
# category which is prioritzed first, because it is an "if" not an "else" 
# statement, unlike starchy which is an "else" statement.
# 2. 
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    if food_id('apple') != 'NOT Citrus, Fruit':
        works = 'apple bug in food_id()' 
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = 'potato bug in food_id()' 
    if food_id('oof') != 'NOT Starchy, NOT Fruit':
        works = 'not listed food id bug in food_id()' 
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
# 3.
def f(n):
    if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                print ('The number is a multiple of 6')
                return 'multiple of 6'
            else:
                print ('The number is even')
                return 'even'
        else:
            print ('The number is odd')
            return 'odd'
    else:
        print ('The input is not an integer')
        return 'not integer'
# 4. You can use a non-integer, any odd number, any even number that is not a multiple of 6, and a multiple of 6.
# 5.
def f_test():
    works = True
    if f(1.1) != 'not integer':
        works = 'not integer bug in f()'
    if f(13) != 'odd':
        works = 'odd bug in f()'
    if f(10) != 'even':
        works = 'even bug in f()'
    if f(12) != 'multiple of 6':
        works = 'multiple of 6 bug in f()'
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

'''Part 2: The raw_input() function, type casting, and print() from Python 3'''
# 6. When + is used as a concatenation between two strings, it results in the 
# second string being placed right after the first. When + is used as a numeric 
# addition, it results in the two numbers getting added resulting in a string or float.
# 7. 
# 7a. If line 9 in the model isn't executed, then line 11 is executed, so if guess is not not equal to secret then line 11 will execute as the only option left.
# 7b.
import random

def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess < secret:
        print('Too low - my number was ', secret, '.', sep='')
    if guess > secret:
        print('Too high - my number was ', secret, '.', sep='')
    if guess == secret:
        print('Right, my number is', guess, end='!\n')
# 8.
def quiz_decimal(low,high):
    answer = float(raw_input('Type a number between ' + str(low) + ' and ' + str(high) + ': '))
    if answer > low and answer < high:
        print('Good!', low, '<', answer, '<', high)
    if answer > float(high):
        print('No,', answer, 'is greater than', high)
    if answer < float(low):
        print('No,', answer, 'is less than', low)
        
'''Conclusion'''
# 1. Glass box testing tests your if structure and every outcome in that function to see if there is an error in any part of the function.
# 2. An structure will always execute one block of code if the function has an if and else statement. If the structure only has if and elif statements it will execute either 1 or 0 blocks of code depending on the input.
# 3. Test suites run the tested code several times with different inputs that cover a variety of inputs. Programmers probably write test suites first to effectively test the code after they have written it.
# 4. 
def integer(n):
    if int(n) != n:
        print ('The input is not an integer')

def even(n):
    if int(n) % 2 == 0:
        print ('The number is even')
        
def odd(n):
    if int(n) % 2 != 0:
        print ('The number is odd')
        
def multiple_6(n):
    if int(n) % 2 == 0 and int(n) % 3 == 0:
        print ('The number is a multiple of 6')
        
'''Challenge'''
# 1.
def f_challenge(n):
    if n % 2 == 0 and n % 3 == 0:
        print ('The input is an integer')
        print ('The number is even') 
        print ('The number is a multiple of 6')
    elif int(n) != n:
        print ('The input is not an integer')
    elif n % 2 == 0:
        print ('The input is an integer')
        print ('The number is even')
    elif n % 2 != 0:
        print ('The input is an integer')
        print ('The number is odd')
        
'''Assignment Check'''
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)

