from prime import is_prime

def primes_below(n):
    l=[]
    if n<=0:
        print('Incorrect input')
    else:
        while n>=1:
            n=n-1
            f=is_prime(n)
            if f == True:
                l.append(n)
        print(list(reversed(l))) 
