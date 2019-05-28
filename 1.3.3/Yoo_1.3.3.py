
'''Procedure'''
# 1-5. N/A

'''Part 1: Conditionals'''
# 6a. Prediction: True
# 6b. Prediction: True
# 7. Compound Conditional: 40<x and x<130 and 100<=y and y<=120
# 8. x, y = (90, 115)
# 40<x and x<130 and 100<=y and y<=120

'''Part 2: if-else Structures and the print() Function!!!!'''
# 9a. 
def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13
    if age < AGE_LIMIT:
        print age, 'is below the age limit.'
    else:
        print age, 'is old enough.'
    print ' Minimum age is ', AGE_LIMIT
# 9b. 
def report_grade(percent):
    '''Less than 80 percent is not a passing grade, 
    80 percent or higher is a passing grade.'''
    if percent<80:
        print ('A grade of', percent, 'does not indicate mastery. Seek extra practice or help.')
    else:
        print 'A grade of', percent, 'percent indicates mastery. Keep up the good work!'
        
'''Part 3: The in operator and an introduction to collections'''
# 11.
def letter_in_word(guess,word):
    '''if the guessed letter is the same as the letter in word, 
    but one is uppercase, it will come out as false.'''
    if guess in word and len(guess) == 1:
        return True
    else:
        return False
# 12.
def hint(color,secret):
    '''Secret must be defined by it self as a variable first'''
    if color in secret:
        print 'The color', color, 'IS in the secret sequence of colors.'
    else:
        print 'The color', color, 'IS NOT in the secret sequence of colors.'

'''Conclusion'''
# 1. They are all instructions that happen if the "if" criteria is met, 
# otherwise, they do not alter or print anything.
# 2. and, or, not, ==, <=, >=, !=, >, <, ==, in, one more that 
# I learned about by searching on the web are bitwise operators such as ">>"
# 3. I think that Ira and Kendra have the right idea, but the arguments that 
# the code is going to run slower and that it takes up more memory are 
# irrelevant because it hardly slows or take more memory. Jayla is right 
# because for efficiency reasons it is smarter to have it just once than twice.

'''Assignment Check'''
#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)