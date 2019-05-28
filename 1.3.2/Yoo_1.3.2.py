def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip
    
# 17a: Hypotenuse of a triangle
def hyp(leg1, leg2):
    '''Retuns hypotenuse of a right triangle'''
    squared = leg1 ** 2 + leg2 ** 2
    return squared ** 0.5
# 17b: Mean Test
def mean(a,b,c):
    mean = (a+b+c)/3.0
    return mean
# 17c: Perimeter Test
def perimeter(base,height):
    perimeter = (base+height)*2.0
    return perimeter
#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)