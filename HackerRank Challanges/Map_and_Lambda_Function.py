
cube =lambda x: x**(3)

def fibonacci(n):
    # return a list of fibonacci numbers
    if  n ==0 :
        fib_numbers=[]
        return fib_numbers
    elif n==1:
        fib_numbers=[0]
        return fib_numbers
    else:
        
        fib_numbers=[0,1]
        for i in range (2,n):
            fib_numbers.append(fib_numbers[i-1]+fib_numbers[i-2])
        return fib_numbers


