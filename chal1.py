def get_prime_factors(number):
    factors=[]
    divisor=2

    while divisor<=number:
        if number % divisor==0:
            factors.append(divisor)
            number=number//divisor #     
        else:
            divisor+=1

    return factors

number=44
print(get_prime_factors(number))
number1=13
print(get_prime_factors(number1))
    
