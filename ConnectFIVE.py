for x in range(1,7):
    print("")
    print("|", end="")
    for y in range(1, 8):
        print("_", end="")
        print("|", end="")
notanythingyouwant=[["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E", "E", "E"]]
twoplayer=0
wincheck=True
while wincheck==True:
    userchoice=input("What slot would you want to choose?")
    for i in range(5, -1, -1):
        if notanythingyouwant[i][int(userchoice)-1]=="E" and twoplayer%2==1:
            notanythingyouwant[i][int(userchoice)-1]="O"
            twoplayer=twoplayer+1
            print(notanythingyouwant)
            break
        elif notanythingyouwant[i][int(userchoice)-1]=="E" and twoplayer%2==0:
            notanythingyouwant[i][int(userchoice)-1]="0"
            twoplayer=twoplayer+1
            print(notanythingyouwant)
            break
def winner(notanythingyouwant):
    for p in range(6):
        for o in range(4):
            if notanythingyouwant[p][o]==notanythingyouwant[p][o+1]==notanythingyouwant[p][o+2]==notanythingyouwant[p][o+3]=="O":
                print("You win? O player?")
            elif notanythingyouwant[p][o]==notanythingyouwant[p][o+1]==notanythingyouwant[p][o+2]==notanythingyouwant[p][o+3]=="0":
                print("0 idn't 0 anymore")
            elif notanythingyouwant[p][o]==notanythingyouwant[p+1][o]==notanythingyouwant[p+2][o]==notanythingyouwant[p+3][o]=="O":
                print("Victory! O!")
            elif notanythingyouwant[p][o]==notanythingyouwant[p+1][o]==notanythingyouwant[p+2][o]==notanythingyouwant[p+3][o]=="0":
                print("You got n0thing!")
    for q in range(7):
        for r in range(3):
            if notanythingyouwant[q][r]==notanythingyouwant[q][r+1]==notanythingyouwant[q][r+2]==notanythingyouwant[q][r+3]=="O":
                print("OOOOOOOOOOhhh!")
            elif notanythingyouwant[q][r]==notanythingyouwant[q][r+1]==notanythingyouwant[q][r+2]==notanythingyouwant[q][r+3]=="0":
                print("0 really ZEROED in")
            elif notanythingyouwant[q][r]==notanythingyouwant[q+1][r]==notanythingyouwant[q+2][r]==notanythingyouwant[q+3][r]=="O":
                print("No OOpses, just 00pses.")
            elif notanythingyouwant[q][r]==notanythingyouwant[q+1][r]==notanythingyouwant[q+2][r]==notanythingyouwant[q+3][r]=="0":
                print("0 wins")
    for s in range(3):
        for t in range(3):
            if notanythingyouwant[s][t]==notanythingyouwant[s+1][t+1]==notanythingyouwant[s+2][t+2]==notanythingyouwant[s+3][t+3]=="O":
                print("O. You have been chosen")
            elif notanythingyouwant[s][t]==notanythingyouwant[s+1][t+1]==notanythingyouwant[s+2][t+2]==notanythingyouwant[s+3][t+3]=="0":
                print("0 is more effective then a Japanese fighter plane")
            elif notanythingyouwant[s][t]==notanythingyouwant[s+1][t+1]==notanythingyouwant[s+2][t+2]==notanythingyouwant[s+3][t+3]=="O":
                print("O beats 0")
            elif notanythingyouwant[s][t]==notanythingyouwant[s+1][t+1]==notanythingyouwant[s+2][t+2]==notanythingyouwant[s+3][t+3]=="0":
                print("0 is even higher then first place")
    for u in range(3):
        for v in range(3):