#short script that uses the pollard pho algo to factor numbers

#we'll need Euclid's algo to find gcd

def euclid(a,b):
    r1 = a
    r2 = b

    while ( r2 != 0 ):
        r = r1%r2
        r1 = r2
        r2 = r
    return r1


def pollard(n,c):
    f = lambda x: (x*x+c)%n
    x1 = f(1)
    x2 = f(f(1))
    g = euclid(x1-x2,n)

    if c > 100:
        return "prime probable"
    
    while ( g == 1 ):
        x1 = f(x1)
        x2 = f(f(x2))
        g = euclid(x1-x2,n)
    
    if g == n or x1 == x2:
        return pollard(n,c+1)
    
    return g



n = 2**29 - 1
p = (pollard(n,1))
print(p)
q = pollard(p,1)
print(q)
print(pollard(q,1))
n = int(n/q)
p = pollard(n,1)
print(p)
while (pollard(p,1) != "prime probable"):
    p = pollard(p,1)
    print(p)
print(pollard(p,1))
