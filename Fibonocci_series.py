
# Python program to get the Fibonacci series between 0 to n
# Fibonacci series is series of numbers such that each number is the sum of the two preceding ones, starting from 0 and 1

def fibonacciNum(n):
    fibonacci_list = [0,1]

    while fibonacci_list[-1] <= n:
        x = fibonacci_list[-1] + fibonacci_list[-2]
        if x > n:
            break
        fibonacci_list.append(x)

    print (fibonacci_list)

fibonacciNum(100)







