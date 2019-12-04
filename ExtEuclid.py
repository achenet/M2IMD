#this is a small script that given two numbers a and b
#returns s,t,d such that a*s+b*t = d, and d = gcd(a,b)

def extEuclid(a,b):
    if a < b:
        a,b = b,a
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while (r2 != 0):
        q = int(r1/r2)
        r3 = r1%r2
        (r1,s1,t1,r2,s2,t2) = (r2,s2,t2,r3,s1-q*s2,t1-q*t2)
    print(r1,s1,t1)
    return r1,s1,t1


#a = int(raw_input("a = "))
#b = int(raw_input("b = "))
#print(extEuclid(a,b))

