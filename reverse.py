from operator import index


def my_reverse(l):
    index=len(l)
    m=[]
    while index>0:
        index=index-1
        m.append (l[index])
    return m