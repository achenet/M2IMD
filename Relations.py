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
               
    
orders = orders391()


for i in orders.keys() :
    if orders[i] == 2 or orders[i] == 11:
        print(i)


n = (13,17)




