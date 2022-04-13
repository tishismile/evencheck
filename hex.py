def to_hex(n):
    l=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    var1=l[n//16]
    var2=l[n%16]
    return (var1+var2)

def hex_color(red,green,blue):
    var1=to_hex(red)
    var2=to_hex(green)
    var3=to_hex(blue)
    return ("#"+var1+var2+var3)

