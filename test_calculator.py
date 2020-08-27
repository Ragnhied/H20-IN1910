#Filen inneholder alle testfilene laget i Project 0
from calculator import add, factorial, sin, divide, sqrt, cos
from math import factorial as factorial_math
from math import sin as sin_math
from math import cos as cos_math
import pytest

def test_add_exercise_1():
    assert add(1,2) == 3

def test_add_floatpointnumbers_exercise_2(): 
    expected = 0.1 + 0.2
    computed = add(0.1, 0.2)
    tol = 1e-9
    result = abs(expected-computed) < tol
    assert result, "The test failed"

def test_add_string_exercise_3():
    assert add("Hello ", " World") == "Hello World"

#Her kommer fem testfunksjoner med utgangspunkt i metoden "Test driven development", exercise 4:

def test_factorial_exercise_4():
    assert factorial(5) == 120
    success = abs(factorial(5) == factorial_math(5))
    assert success, "The test failed!"

def test_sin_exercise_4():
    expected = sin_math(1)
    computed = sin(1,1000)
    tol = 1e-9
    value = abs(expected-computed) < tol
    assert value, "test_sin() failed!"

def test_divide_exercise_4():
    assert divide(90,2) == 45

def test_sqrt_exercise_4():
    assert sqrt(25) == 5

def test_cos_exercise_4():
    tol = 1e-9
    assert (cos(1,1000) == cos_math(1))<tol

def test_add_TypeError_exercise_5(): #Tester at funksjonen gir feilmeldingen TypeError ved å sette sammen string og float
    with pytest.raises(TypeError):
        add("Hello",19)

def test_divide_ZeroDivisionError_exercise_5(): #Tester at funksjonen gir riktig feilmelding når man deler et tall på null
    with pytest.raises(ZeroDivisionError):
        divide(9,0) 

@pytest.mark.parametrize("x, x2", [[(1, 2),3], [(1, 1),2], [(2, 4),6]])
def test_add_exercise_6(x,x2):
    assert add(x[0],x[1]) == x2

@pytest.mark.parametrize("x, x2", [[(0.1, 0.2),0.3], [(0.1, 0.1),0.2], [(0.3, 0.4),0.7]])
def test_add_floatpointnumbers_exercise_6(x,x2): 
    tol = 1e-9
    assert abs((add(x[0],x[1])-x2)) <tol

@pytest.mark.parametrize("x, x2", [[("Hello ","World"),"Hello World"], [("Whats ","Up"),"Whats Up"], [("Lets"," Go"),"Lets Go"]])
def test_add_string_exercise_6(x, x2): 
    assert add(x[0],x[1]) == x2

@pytest.mark.parametrize("x, x2", [[5,5], [10,10], [21,21]])
def test_factorial_exercise_6(x,x2):
    assert factorial(x) == factorial_math(x2)

@pytest.mark.parametrize("x, x2", [[(1, 1000),1], [(2, 1000),2], [(4, 1000),4]])
def test_sin_exercise_6(x,x2):
    tol = 1e-9
    assert abs((sin(x[0],x[1])-sin_math(x2))) <tol

@pytest.mark.parametrize("x, x2", [[(90, 2),45], [(45, 5),9], [(10, 4),2.5]])    
def test_divide_exercise_6(x,x2):
    assert divide(x[0],x[1]) == x2

@pytest.mark.parametrize("x, x2", [[25,5], [9,3], [16,4]]) 
def test_sqrt_exercise_6(x,x2):
    assert sqrt(x) == x2

@pytest.mark.parametrize("x, x2", [[(1, 1000),1], [(2, 1000),2], [(4, 1000),4]])
def test_cos_exercise_6(x,x2):
    tol = 1e-9
    assert abs((cos(x[0],x[1])-cos_math(x2))) <tol

@pytest.mark.parametrize("x, x2", [["Hello ",19], [20,"Something"], [2,"Pac"]])
def test_add_TypeError_exercise_6(x,x2): 
    with pytest.raises(TypeError):
        add(x,x2)

@pytest.mark.parametrize("x, x2", [[90, 0], [45, 0], [10, 0]]) 
def test_divide_ZeroDivisionError_exercise_6(x,x2):
    with pytest.raises(ZeroDivisionError):
        divide(x,x2)
        