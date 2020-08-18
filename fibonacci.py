# Python program to display the Fibonacci sequence up to n-th term using recursive functions
#!/usr/bin/python3
def recur_fibo(n) :
    # recursive function to print Fibonacci sequence
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

# Change this value for a different result

nterms = 10        
