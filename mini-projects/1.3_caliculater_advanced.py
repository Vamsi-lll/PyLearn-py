# we have seen 3 types now this is the code which is simple and advanced  

# here is the question  
# while handling the addition function or addition in the above examples we have given 2 numbers  
# what if the user wants to add 3 numbers?  
# we have to add another parameter to the function which is ok for now  
# but what if the user wants to add n number of numbers then here is the break you are in a spot  
# in the types of arguments we have seen the *args option right?  
# we can use this to pass multiple values to the function  

# so here is the example for the function  

def add(*args):  # you can use any variable name here like *a, *nums
    return sum(args)

def sub(*args):  # subtract all values from the first one
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def mul(*args):  # multiply all values together
    if not args:
        return 0
    result = 1
    for num in args:
        result *= num
    return result

def div(*args):  # divide sequentially
    if not args:
        return "No numbers provided"
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error: Division by zero is not allowed"
        result /= num
    return result

# examples for *args functions
print(add(1, 2, 3))          # 6
print(add(1, 2, 3, 4, 5))    # 15
print(sub(10, 2, 3))         # 5
print(mul(2, 3, 4))          # 24
print(div(100, 2, 5))        # 10

