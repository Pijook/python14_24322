def are_prime_numbers(*numbers):
    for number in numbers:
        is_prime_number = True
        if number == 1 or numbers == 0:
            is_prime_number = False
        else:
            for i in range(2, int(number / 2) + 1):
                if number % i == 0:
                    is_prime_number = False
                    break

        if is_prime_number:
            print(number, "is prime number")
        else:
            print(number, "is not a prime number")


are_prime_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
