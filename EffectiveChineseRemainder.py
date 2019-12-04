#this is a simple python script that given a list of k integers
#n1...nk and a list of k modular remainders a1,...,ak will 
#compute the unique a mod n = (n1*...*nk) such that
#a = a1 mod n1,..., a = ak mod nk


from ExtEuclid import extEuclid

def modInv(a,n):
    if n < a:
        return "n is less than a"
    (d,t,s) = extEuclid(a,n)
    if d > 1:
        return "no modular inverse exists"
    if s < 0:
        s = n + s
    return s

print(modInv(3,7))

def effCRT(la,ln):
    n = 1
    for i in ln:
        n = n * i
    a = 0
    for i in range(len(la)):
        m = int(n/ln[i])
        b = m%(ln[i])
        t = modInv(b,ln[i])
        e = t*m
        a = (a + e*la[i])%n
    return a



#k = int(raw_input("how many integers are we using?")
#la is the list of a1,...,ak 
#ln is the list of n1,...,nk
la = [1,2]
ln = [17,23]

print(effCRT(la,ln))
#for i in range(k):
#    la.append(int(raw_input("value of a_"+str(i))))
#    ln.append(int(raw_input("value of n_"+str(i))))


