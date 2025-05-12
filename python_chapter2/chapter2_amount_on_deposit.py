'''
a = p(1 + r)n
 where
 p is the original amount invested (i.e., the principal of $1000),
 r is the annual rate of return (7%),
 n is the number of years (10, 20 or 30) and
 a is the amount on deposit at the end of the nth year.

'''
p = 1000
r = 7 / 100
n = 10

x = (1 + 0.07)**10
a = (p * x)
print("The amount on deposit at the end of 10th year is:", a )