#this is a simple python script that given a list of k integers
#n1...nk and a list of k modular remainders a1,...,ak will 
#compute the unique a mod n = (n1*...*nk) such that
#a = a1 mod n1,..., a = ak mod nk

#but for that we need a reliable method of computing modular inverse, which we don't really... ok we can just use the ExtEuclid.py

from ExtEuclid import extEuclid

def modularInverse(a,n):
    if n < a:
        return "n is less than a"
    (d,s,t) = extEuclid(a,n)
    if d > 1:
        return "no modular inverse exists"
    if s < 0:
        s = n + s
    return s


def effCRT(la,ln):
    



k = int(raw_input("how many integers are we using?")
la = []
ln = []
for i in range(k):
    la.append(int(raw_input("value of a_"+str(i))))
    ln.append(int(raw_input("value of n_"+str(i))))


