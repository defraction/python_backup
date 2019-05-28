'''Procedure'''
# 1. N?A
# 2. N/A
# 3. N/A
# 4. N/A
# 5. Int, float, long, and str can represent 6 million.
# 6. The first input does not produce an error because it is the concatenation of 
# 2 strings, therefore remaining as a string type, but the second input produces
# an error because it is attempting to concatenation a string and a integer type,
# which is not possible for the type function to understand.
# 7. Slogan[-7] results in 'h' because if the inputed index number is negative,
# the index is counted from the end of the string to the start , starting at -1,
# and the index number getting lower.
# 8.
slogan = 'My school is the best'
slogan[17:]

# 9.
'DHS ' + slogan[10:]

# 10a. The output of len(activity) is 7 because activity is the variable that the 
# string 'theater' is stored in, so len(activity) displays the length of 'theater'
# which is 7 characters long.
# 10b. The output of activity[0 : len(activity)-1] is 'theate' because this input
# is just slicing from index values of 0 and 6, because the length of 'theater' is 7 and
# 1 subtracted from 7 is 6.
# 11. It returns as true because all of the characters in 'test goo' are in the
# string of 'Greatest good for the greatest number!'.
# 12. 
def how_eligible(essay):
    if '?' in essay:
        a = 1
    else: 
        a = 0
    if '!' in essay:
        b = 1
    else:
        b = 0
    if ',' in essay: 
        c = 1
    else: 
        c = 0
    if '"' in essay:
        d = 1
    else:
        d = 0
    return a + b + c + d
    
'''Assignment Check'''
#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))