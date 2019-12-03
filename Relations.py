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

def baseRel(o):
    rel = []
    for i in (0,1,2,4,8,11,16,22,44,88,(16*11),(32*11)):
        for j in (0,1,2,4,8,11,16,22,44,88,(16*11),(32*11)):
            for k in (0,1,2,4,8,11,16,22,44,88,(16*11),(32*11)):
                if ((2**i * 3**j * 5**k)%17, (2**i * 3**j * 5**k)%23) == (1,1):
                    rel.append((i,j,k))
    return rel

rel = baseRel(o)
#print(rel)

def reduceRel(o):
    base = []
    for i in rel:
        if 0 in i:
            base.append(i)
            rel.remove(i)
    for i in rel:
        for j in range(len(rel)):
            if 




