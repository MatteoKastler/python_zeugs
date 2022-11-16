import random

symbol = ["Rock", "Lizard", "Spock", "Scissors", "Paper"]
#1 schlägt 2 usw
def getWinner(a, b):
    if(a == b):return 0
    if((a+1)%(len(symbol)) == b): return 1
    if((a+3)%(len(symbol)) == b): return 1
    return 2

if __name__ == '__main__':
    player = -1
    for i in range(len(symbol)):
        print(f'{i}: {symbol[i]}')
    player = int(input("Please choose a weapon"))
    while(player == -1 or type(player) != int or player > 4):
        player = int(input("try again"))

    comp = random.randint(0,len(symbol)-1)
    result = getWinner(player, comp)
    print(f'\nPlayer choice: {symbol[player]}')
    print(f'Computer choice {symbol[comp]}')
    if(result == 1):
        print("You won")
    elif(result == 2):
        print("Computer won")
    else:
        print("Draw")
