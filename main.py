import random

def get_lotto():
    lotteryNumbers = []

    for i in range(0, 6):
        number = random.randint(1, 45)
        while number in lotteryNumbers:
            number = random.randint(1, 45)
        lotteryNumbers.append(number)

    return lotteryNumbers

numbers = get_lotto()

print("numbers:")
print(numbers)

list = [0]*46

for i in range(1000):
    x = random.randint(1, 45)
    list[x] = list[x]+1

print(list[1:])