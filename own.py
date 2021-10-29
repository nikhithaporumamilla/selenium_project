#write fourth nearest prime number to given number
def prime_numbers(num):
    large_prime = []
    small_prime = []
    current_number = num
    while len(large_prime) < 4:
        current_number+=1
        is_prime = True
        for val in range(2, current_number):
            if current_number%val == 0:
                is_prime = False
                break
        if is_prime:
            large_prime.append(current_number)
    print(large_prime)

    current_number = num
    while len(small_prime) < 4:
        current_number = current_number - 1
        is_prime = True
        for val in range(2, current_number):
            if current_number % val == 0:
                is_prime = False
                break
        if is_prime:
            small_prime.append(current_number)
    print(small_prime)
    count = 0
    fourth_prime = 0
    while count < 4:
        if num - small_prime[0] < large_prime[0] - num:
            fourth_prime=small_prime.pop(0)
        else:
            fourth_prime = large_prime.pop(0)
        count+=1
    print(fourth_prime)



number = int(input("Please enter the number: "))
prime_numbers(number)