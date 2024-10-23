# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


def is_prime(num):
    if num < 2:
        return f"{num} is not prime"
    for n in range(2, num):
        if num % n == 0:
            return f"{num} is not prime"
    return f"{num} is prime"

input_number = int(input("Enter a number: "))
output_number = is_prime(input_number)

print(f"{output_number}")
