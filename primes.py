def sqrt(n):
    """ Returns the square root of n """
    return int(n**0.5)

def isPrime(n):
    """ Returns True if n is prime """
    if n < 2:
        # 0 and 1 are not prime; interferes with logic
        return False
    for i in range(2, sqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    """ Returns a list of prime numbers up to n
        Args: n (int): Upper limit
        Returns: primeNumbers (list): List of prime numbers up to n"""
    
    # comprehension
    primeNumbers = [i for i in range(2, n+1) if isPrime(i)]
    
    #print(primeNumbers)

    return primeNumbers