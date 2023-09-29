def fibonacci(n):
    #this function returns the nth number of the fibonacci series starting with 0, 1, 1
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    
def golden_ratio(n):
    #this function gives the golden ratio  by dividing n and n-1 term of fibonacci series but keeps in mind that dividing by zero is not possible
    #so does not take input less than or equal to 2
    if n<=2:
        return None
    return fibonacci(n)/fibonacci(n-1)

#now you can call these functions and the higher the n is more closer the golden ratio is
print(fibonacci(5))
print(golden_ratio(20))
