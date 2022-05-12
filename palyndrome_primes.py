from prime import is_prime

l=[]

for x in range (10000, 100000):
    if is_prime(x) == True and list(str(x))==list(reversed(str(x))):
        l.append(x)

print (l) 
    



