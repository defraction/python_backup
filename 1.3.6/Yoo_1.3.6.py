import random
'''Procedure'''
# N/A

'''Part 1: Turples, Syntax'''
# 4.
(3,7,9)
# 5. One convention that a teacher requires of sumitted work it is that it must 
# have your name and period number on it. I am not sure what my teacher wants for
# us to follow when it comes to naming python variables, but I assume it is the 
# standard way of naming variables.
# 6a. The output of some_values[1] will be 'b' because that is the value that is 
# stored in index value 1.
# 6b. The output of some_values[0:2] will be 'a', 'b' because those are the values
# stored in the index values between 0 and 2.
# 7a. b[1] == 10 will return as True, because in the tuple, the second value or the
# index value 1 is 10.
# 7b. Since the variable 'a' is now assigned a value of 15, by placing it in the 
# index value 1 of the tuple, it will overwrite the current value of 10 with the
# value that 'a' is storing, which is 15.

'''Part 2: Lists'''
# 8. The input of values[1:] shows every value in the list from the index value
# of 1 and on. This shows that lists elements can be brought up in segments, just
# like tuples.
# 9. By doing values[2] = '3', that changed the index value of 2 to a string that
# says '3'. Because of that, the index value of 2 is not the same as the value of 3,
# so the equation returns false. 
# 10a. By adding [4,5] after values, that added the values of 4 and 5 after the 
# original values. If [4,5] was added in front of the original values, then in
# the list it would display as the first two index values.
# 10b. .append([6,7]) added a list inside of the values list with the values of
# 6 and 7 at the end of the list.
# 11. It does not work because by doing values = values + 5 the line is trying 
# to concatenate a list with an integer which is not possible. Both values must
# be the same data type.
# 12. The operator *= multiplies the variable by the value on the right and stores
# the product in the variable used by overwriting the previous value.
# 14.
def roll_two_dice():
    return random.randint(2,12)

'''Conclusion'''
# 1. They are different data types that can only concatenate with values of their
# respective data types.
# 2. Because with a variety of data types, the language is more flexible and is 
# able to be used for a larger variety of tasks. Integers can not be used for everything
# because not everything is non-decimal numbers and things such as strings are also
# needed for text-based programs and such.
# 3. 1.3.2 - Learned about basic function and what they are.
# 1.3.3 - Learned about if/else statements and boolean variables.
# 1.3.4 - Learned about nested if/else statements and how to make a test case.
# 1.3.5 - Learned about different data types, slicing strings, concatenation of
# strings.
# 1.3.6 - Learned about the differences and similarities of tuples and lists, and
# ways to manipulate them.

'''Assignment Testing'''
#1.3.6 Function Test
print(roll_two_dice())

# 1. After running the new code, I am getting random values between 2 and 12 which
# simulates rolling 2 dice, so because of that, I believe that I have sucessfully
# completed this assignment.