import random

# Initialise an empty list that will be used to store the 6 lucky numbers!

def get_lotto():
    lotteryNumbers = []

    for i in range(0, 6):
        number = random.randint(1, 50)
        while number in lotteryNumbers:
            number = random.randint(1, 50)
        lotteryNumbers.append(number)

    return lotteryNumbers

numbers = get_lotto()

# Display the list on screen:
print("numbers:")
print(numbers)