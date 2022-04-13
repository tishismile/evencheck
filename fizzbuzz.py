n=0

while n<1000: 
    n=n+1   
    if n%3==0 and n%5>0:
        print('Fizz')
    elif n%5==0 and n%3>0:
        print('Buzz')
    elif n%15==0:
        print('FizzBuzz')
    else:
        print(n)

