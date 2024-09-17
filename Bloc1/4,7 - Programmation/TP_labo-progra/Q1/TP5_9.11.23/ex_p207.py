"""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))
=> 4*3*2*1 = 24
"""

"""
def factorial(n):
    return n * factorial(n - 1)

print(factorial(4))
=> RecursionError: maximum recursion depth exceeded
"""

"""
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))
=> 25+28+3
"""
