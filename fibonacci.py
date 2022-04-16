def big_fibonacci(n):
    var1=1
    var2=1
    var3=var1+var2
    while len(str(var3))<n:
        var1=var2
        var2=var3
        var3=var1+var2
    return var3
