for x in range(1, 4):
    print("")
    print("|", end="")
    for y in range(1, 4):
        print("_", end="")
        print("|", end="")
twoplayer=0
even=[0,2,4,6,8]
odd=[1,3,5,7,9]
anythingyouwant=[["0","0","0"], ["0","0","0"], ["0","0","0"]]
def winchecker(anythingyouwant):    
    for i in range(3):
        if anythingyouwant[i][0]==anythingyouwant[i][1]==anythingyouwant[i][2]=="X" or anythingyouwant[i][0]==anythingyouwant[i][1]==anythingyouwant[i][2]=="O":
            print("We have a winner! Take that loser. You lost. Loser. Losers lose. That's why you're a loser. Bozo.")
            return False
        elif anythingyouwant[0][i]==anythingyouwant[1][i]==anythingyouwant[2][i]=="X" or anythingyouwant[0][i]==anythingyouwant[1][i]==anythingyouwant[2][i]=="O":
            print("Someone won. Horray.")
            return False
        elif anythingyouwant[0][0]==anythingyouwant[1][1]==anythingyouwant[2][2]=="X" or anythingyouwant[0][0]==anythingyouwant[1][1]==anythingyouwant[2][2]=="O":
            print("You won. Winner. Because Winners win.")
            return False
        elif anythingyouwant[2][0]==anythingyouwant[1][1]==anythingyouwant[0][2]=="X" or anythingyouwant[2][0]==anythingyouwant[1][1]==anythingyouwant[0][2]=="O":
            print("The game has ended because someone was a fool! A fool!")
            return False
        else:
            return True
def boardupdate(anythingyouwant):
    for x in range(0, 3):
        print("")
        print("|", end="")
        for y in range(0, 3):
            if anythingyouwant[x][y]=="0":
                print("_", end="")
                print("|", end="")
            else:
                print(anythingyouwant[x][y], end="")
                print("|", end="")
b=True
while b==True:
    anyrowyouwant=input("What row would you like?")
    if int(anyrowyouwant)<=3 and int(anyrowyouwant) >=1:
        pass
    else:
        print("Ha! Now the program will end because you can't follow simple instructions. Loser.")
    anycolumnyouwant=input("What column would you like?")
    if int(anycolumnyouwant)<=3 and int(anycolumnyouwant)>=1:
        pass
    else:
        print("Ha! Now the program will end because you can't follow simple instructions. Bozo.")
#if anycolumnyouwant and ResourceWarning:
#    print("Gold")
#if anythingyouwant==anythingyouwant:
#    print("hi", end="")
    anythingyouwant[int(anyrowyouwant)-1][int(anycolumnyouwant)-1]
    if anythingyouwant[int(anyrowyouwant)-1][int(anycolumnyouwant)-1]=="0" and twoplayer%2==1:
        anythingyouwant[int(anyrowyouwant)-1][int(anycolumnyouwant)-1]="X"
        twoplayer=twoplayer+1
    elif anythingyouwant[int(anyrowyouwant)-1][int(anycolumnyouwant)-1]=="0" and twoplayer%2==0:
        anythingyouwant[int(anyrowyouwant)-1][int(anycolumnyouwant)-1]="O"
        twoplayer=twoplayer+1
    else:
        print("Occupied")
    boardupdate(anythingyouwant)
    b=winchecker(anythingyouwant)