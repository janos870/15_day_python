# total = 0
#
# for n in range(1, 11):
#     total += n
#
# print(total)

for n in range(1, 101):
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)