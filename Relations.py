#this is a simple Python script to find the order of all elements in a given Z/nZ given
#the prime factorization of n

#n is written as a tuple of its prime factors
def orders391():
    orders = {}
    for i in range(1,17):
        for j in range(1,23):
            for k in (1,2,4,8,11,16,22,44,88,(16*11),(32*11)):
                if ((i**k)%17,(j**k)%23)==(1,1):
                    orders[(i,j)] = k
                    break
    return orders
               
    
o = orders391()
for i in o:
    if o[i] == 4:
        print(i)

def baseRel(o):
    rel = []
    for i in (0,1,2,4,8,11,16,22,44,88,(16*11),(32*11)):
        for j in (0,1,2,4,8,11,16,22,44,88,(16*11),(32*11)):
            for k in (0,1,2,4,8,11,16,22,44,88,(16*11),(32*11)):
                if ((2**i * 3**j * 5**k)%17, (2**i * 3**j * 5**k)%23) == (1,1):
                    rel.append((i,j,k))
    return rel

def multZ17():
    l = [2,8,9,15]
    for i in l:
        for j in l:
            if (i*j)%17 in l:
                print(i, " * ",j, " = ", (i*j)%17)
    return 0
print(multZ17())




#rel = baseRel(o)
#print(rel)

def reduceRel(rel):
    base = []
    for i in rel:
        if i[0] == 0 or i[1] == 0 or i[2] == 0:
            base.append(i)
            rel.remove(i)
            print(i)
    #we'll need to treat the case where one or more exponents is zero
    for i in rel:
        for j in rel:
            if i[0]%j[0]==0 and i[1]%j[1]==0 : 
                rel.remove(i)
    return rel

#print(reduceRel(rel))


