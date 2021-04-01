def lenght_unos(bitstring):
    c=[]
    d=0
    for i in bitstring:
        if i=='1':
            d+=1
        elif i=='0':
            c.append(d)
            d=0
        c.append(d)
    return(max(c))

def zero_to_uno(bitstring):
    s=''
    v=[]
    i=0
    x=list(bitstring)
    while i<len(x):
        x=list(bitstring)
        if x[i]=='0':
            x[i]='1'
            v.append(''.join(x))
        i+=1
    return(v)

b = input()
x=zero_to_uno(b)
v=[]
for i in x:
    v.append(lenght_unos(i))

print(max(v))
