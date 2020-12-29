import math
def count_primes(num):
    current_number = 4
    number_of_prime = 2
    while current_number <= num:
        is_prime = True
        if current_number%2==0:
            is_prime = False
            current_number += 1
            continue
        else:
            limit = math.ceil(current_number ** 0.5)+1
            for i in range(3, limit, 2):
                if current_number%i==0:
                    is_prime = False
                    #current_number += 1 #first increment
                    continue
                    #This continue statement does not skip the next lines (after the for loop) so you increment current_number twice
        if is_prime == True:
            print(current_number)
            number_of_prime += 1
        current_number += 1 #second increment
    print(number_of_prime)

count_primes(10000000)