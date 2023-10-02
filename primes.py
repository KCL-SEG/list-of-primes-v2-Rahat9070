"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def check_prime(num):
    flag = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            flag = False
    
    return flag

def primes(number_of_primes):
    list = []
    # Solution starts here
    if number_of_primes < 1:
        raise ValueError("Sorry, there cannot be less than 1 prime number")
    else:
        counter = 0
        num = 2
        while counter < number_of_primes:
            if check_prime(num):
                list.append(num)
                counter += 1
            num+=1


    return list
