values = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
currentplayer = "X"
count = 0  # number of spaces filled
winner = False
tie = False
#acceptableslots = [0,1,2,3,4,5,6,7,8]

def board(values):
    print("\n")
    # print("     |     |    ")
    print("  " + values[0] + "  |  " + values[1] + "  |  " + values[2] + "  ")
    print("_____|_____|_____")
    # print("     |     |    ")
    print("  " + values[3] + "  |  " + values[4] + "  |  " + values[5] + "  ")
    print("_____|_____|_____")
    # print("     |     |    ")
    print("  " + values[6] + "  |  " + values[7] + "  |  " + values[8] + "  ")
    print("     |     |    ")
def insertinput(slot, marker):
    while values[slot] != " ":
        print(" please choose another slot")
        slot = int(input("slot: "))
    values[slot] = marker
def checkwinner(marker):
    if values[0] == marker and values[1] == marker and values[2] == marker or \
        values[0] == marker and values[4] == marker and values[8] == marker or \
        values[0] == marker and values[3] == marker and values[6] == marker or \
        values[1] == marker and values[4] == marker and values[7] == marker or \
        values[2] == marker and values[4] == marker and values[6] == marker or \
        values[2] == marker and values[5] == marker and values[8] == marker or \
        values[3] == marker and values[4] == marker and values[5] == marker or \
        values[6] == marker and values[7] == marker and values[8] == marker:
        print(board(values))
        print(marker + " wins!")
        winner = True
        return True
    else:
        return False
def getplayer():
    if count == 0 or count == 2 or count == 4 or count == 6 or count == 8:
        return "X"
    else:
        return "0"

while winner == False and tie == False:
    currentplayer = getplayer()
    print(board(values))
    print("it is " + currentplayer + "'s turn")
    newslot = int(input("please provide slot: "))-1
    insertinput(newslot,currentplayer)
    count += 1

    # check if there is a winner below
    if checkwinner(currentplayer) == True:
        break
    # checking if the game should continue after below
    if count == 9:
        tie = True
if tie == True:
    print("game is a tie")

