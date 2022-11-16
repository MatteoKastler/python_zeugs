
symbol = ["Rock", "Lizard", "Spock", "Scissors", "Paper"]
#1 schlägt 2 usw
def getWinner(a, b):
    if(a == b):return 0
    if((a+1)%(len(symbol)) == b): return 1
    if((a+3)%(len(symbol)) == b): return 1
    return 2

player = -1
if __name__ == '__main__':
    for i in range(len(symbol)):
        print(f'{i}: {symbol[i]}')
    player = int(input("Please choose a weapon"))
    while(player == -1 or type(player) != int or player > 4):
        player = int(input("try again"))
    result = getWinner(player, 0)
    if(result == 1):
        print("Du hast gewonnen")
    elif(result == 2):
        print("Computer hat gewonnen")
    else:
        print("Gleiche Waffe gewählt")
