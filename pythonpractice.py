# Program to depict else clause with try-except
# Function to return a/b
def maths_problem(a,b):
    try:
        c = ((a+b) // (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
# Driver to test above function
maths_problem(2.0,3.0)
maths_problem(3.0,3.0)
