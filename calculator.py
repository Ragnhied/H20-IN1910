def add(x,y): #Exercise 1,2,3
    return x + y

#Her kommer fem funksjoner med utgangspunkt i metoden "Test driven development", exercise 4:

def factorial(x):
    f = 1
    while x > 0:
        f = x*f
        x -= 1
    return f

def sin(x, N):
    s = 0
    for i in range(N+1):
        s += (((-1)**i)*(x**(2*i+1)))/(factorial((2*i)+1))
    return s

def divide(x,y):
    return x / y

def sqrt(x):
    return ((x)**(1/2))

def cos(x,N):
    c = 0
    for i in range(N+1):
        c+= (((-1)**i)*x**(2*i))/(factorial(2*i))
    return c
