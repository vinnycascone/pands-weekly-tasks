# generate primes
#Author: Vincenzo Cascone


primes= []

for candidate in range (2,100):
    #print (candidate)
    is_prime=True
    # need to check if is divisable by prime
    for divisor in range(2, candidate):
        # if divisable by an int it is not a prime number
        if(candidate%divisor ==0):
            is_prime = False
            # no need to keep checking
            break
    if is_prime:
        primes.append(candidate)

print(primes)