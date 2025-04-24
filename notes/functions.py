def sumTwo(a,b):
    return a + b

#print(sumTwo(2,3))
#print(sumTwo([1,2,3],[4,5,6]))
#print(sumTwo("hello","string"))


def sumInputs():
    """Takes two inputs, casts to int and prints sum"""
    a = int(input("Type an integer: "))
    b = int(input("Type another integer: "))
    
    
    print( a + b)

#sumInputs()

#Lambda function
z = lambda x,y: x*y
print(z(3,4))

#Function returning lambda function
def multiplier(n):
    """Returns lambda function that multiplies its input by given n"""
    return lambda number: n*number

tripler = multiplier(3)
quadrupler = multiplier(4) 


print(tripler(int(input("Enter number to triple: "))))
print(quadrupler(int(input("Enter number to quadruple: "))))
