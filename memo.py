from timer import timerDecorator
from primes import getPrimeNumbers

def memo(func):
    """ Decorator takes another function as input and returns a new function that caches the output of the input function in a dictionary for each input it receives. The keys are the inputs and the values are the respective results.

    Args:
        func (function): function we are checking the results of and if we have seen it before

    Returns:
        [function return type]: type that matches function return type
    """
    
    # cache is a dictionary that stores the results of the function; the keys are the inputs and the values are the results
    cache = {} 
    
    # time the function using timerDecorator
    @timerDecorator
    def inner(x):
        if x not in cache:
            # if x is not in the cache, we calculate the result of the function and store it in the cache
            print(f"Calculating {x}")
            cache[x] = func(x) 
        # return the result of the function either way
        else: # if x is in the cache
            print(f"Using cache for {x}")
        return cache[x] 
    return inner 

@memo
def primeTest(n):
    return getPrimeNumbers(n)

#test memoization
primeTest(500000)
primeTest(500001)
primeTest(500000)   