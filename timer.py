import time;
from primes import getPrimeNumbers

def timerDecorator(func):
    """ Decorator takes a function as input and returns a new function that times the execution of the input function

    Args:
        func (function): function we are timing

    Returns:
        function: new function that times the execution of the input function
    """
    def wrapper (*args, **kwargs): 
        start = time.time() #start time
        result = func(*args, **kwargs) #function we are timing
        end = time.time() #end time
        
        print(f"Time elapsed: {end - start}") #time elapsed in seconds between start and end
        
        return result
    return wrapper

@timerDecorator
def primeTest(n):
    return getPrimeNumbers(n)

primeTest(500000)