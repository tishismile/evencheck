def is_prime(n):
    if 1<=n<=3:
        return True
    elif n<=0:
        return False
    else:
        for x in range(2,n):
             if n%x==0:
                 return False
             else:
                return True
    
