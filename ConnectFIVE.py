notanythingyouwant=[["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"]]
twoplayer=0
wincheck=True
def boardupdate(notanythingyouwant):
    for x in range(0, 6):
        print("")
        print("|", end="")
        for y in range(0, 7):
            if notanythingyouwant[x][y]=="E":
                print("_", end="")
                print("|", end="")
            else:
                print(notanythingyouwant[x][y], end="")
                print("|", end="")
def winner(notanythingyouwant):
    for p in range(6):
        for o in range(4):
            if notanythingyouwant[p][o]==notanythingyouwant[p][o+1]==notanythingyouwant[p][o+2]==notanythingyouwant[p][o+3]=="O":
                print("You win? O player?")
                return False
            elif notanythingyouwant[p][o]==notanythingyouwant[p][o+1]==notanythingyouwant[p][o+2]==notanythingyouwant[p][o+3]=="0":
                print("0 idn't 0 anymore")
                return False
    for q in range(3):
        for r in range(7):
            if notanythingyouwant[q][r]==notanythingyouwant[q+1][r]==notanythingyouwant[q+2][r]==notanythingyouwant[q+3][r]=="O":
                print("OOOOOOOOOOhhh!")
                return False
            elif notanythingyouwant[q][r]==notanythingyouwant[q+1][r]==notanythingyouwant[q+2][r]==notanythingyouwant[q+3][r]=="0":
                print("0 really ZEROED in")
                return False
    for s in range(3):
        for t in range(4):
            if notanythingyouwant[s][t]==notanythingyouwant[s+1][t+1]==notanythingyouwant[s+2][t+2]==notanythingyouwant[s+3][t+3]=="O":
                print("O. You have been chosen")
                return False
            elif notanythingyouwant[s][t]==notanythingyouwant[s+1][t+1]==notanythingyouwant[s+2][t+2]==notanythingyouwant[s+3][t+3]=="0":
                print("0 is more effective then a Japanese fighter plane")
                return False
    for u in range(3):
        for v in range(3, 6):
            if notanythingyouwant[u][v]==notanythingyouwant[u+1][v-1]==notanythingyouwant[u+2][v-2]==notanythingyouwant[u+3][v-3]=="O":
                print("No OOpses, just 00pses")
                return False
            elif notanythingyouwant[u][v]==notanythingyouwant[u+1][v-1]==notanythingyouwant[u+2][v-2]==notanythingyouwant[u+3][v-3]=="0":
                print("0 1")
                return False
    return True
while wincheck==True:
    userchoice=input("What slot would you want to choose?")
    for i in range(5, -1, -1):
        if notanythingyouwant[i][int(userchoice)-1]=="E" and twoplayer%2==1:
            notanythingyouwant[i][int(userchoice)-1]="O"
            twoplayer=twoplayer+1
            break
        elif notanythingyouwant[i][int(userchoice)-1]=="E" and twoplayer%2==0:
            notanythingyouwant[i][int(userchoice)-1]="0"
            twoplayer=twoplayer+1
            break
    boardupdate(notanythingyouwant)
    wincheck=winner(notanythingyouwant)