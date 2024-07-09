from asyncore import loop
import random

def generate_password(length):
    def random_numbers(size, lowerBound, upperBound):
        random_numbers = [random.randint(lowerBound, upperBound) for i in range(size)]
        return random_numbers

    arangment = random_numbers(length, 1, 100)

    def random_letters(amount):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        selected = [random.randint(0, 47) for i in range(amount)]
        return [letters[i] for i in selected]

    letter = random_letters(length)
    def random_symbol(amount):
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']
        selected = [random.randint(0, len(symbols)-1) for i in range(amount)]
        return [symbols[i] for i in selected]

    symbol = random_symbol(5)

    def replace_evens_with_sequence(arangment, letter):
        replacement_iter = iter(arangment)
        return [next(replacement_iter) if ord(num) % 2 == 0 else num for num in letter]

    password = replace_evens_with_sequence(arangment, letter)

    final = ''
    for i in password:
        final += str(i)


    return final

amount = 5
length = 3

for _ in range(amount):
    password = generate_password(length)
    print(password)
