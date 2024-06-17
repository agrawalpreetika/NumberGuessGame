import random
import os
def clear_console():
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear')
# def clear_console():
#     print("\033[H\033[J", end="")

def border(str1):
    border='-'*(len(str1)-14)
    print(border)
    print('| {} |'.format(str1))
    print(border)




win="\033[42m\033[1m\033[97m Perfect! You've cracked the mystery number. \033[0m"
incorrect="\033[45m\033[1m\033[97m Incorrect guess! Try again. \033[0m"
loss="\033[1m\033[97m\033[41m Oh no, you've exhausted all your guesses! Better luck next time! \033[0m"
newgame="\033[46m\033[1m\033[97m START NEW GAME! \033[0m"

while True:
    clear_console()
    print()
    print(">>>",'\033[1m'+'\033[95m'+'\033[4m'+"WELCOME TO NUMBER GUESSING GAME"+'\033[0m'+" <<<")

    print()

    print('''\033[94m\033[1mRules:\033[0m
    > The Oracle chooses a number between 1 and 100.
    > You have 10 elusive chances to uncover it.
    > Clues: "Lower..." for guesses too high, "Higher..." for guesses too low.''')

    print()

    print('\033[94m'+'\033[1m'+"Let's Begin...."+'\033[0m')
    num=random.randrange(1,100)

    list1=[]

    for i in range(10):
        if i!=0:
            print("Your Previous Guesses:",end=" ")
            for j in list1: print(j,end=" ")

        print()

        guess=int(input("GUESS {} Enter the number :".format(i+1)))
        list1.append(guess)

        if (guess==num):
            border(win)
            print()
            break
        else:
            if i==9:
                print("\n\033[1m\033[91mINCORRECT\033[0m\n\033[1mThe number is \033[93m{}\033[0m".format(num))
                border(loss)
            else:
                border(incorrect)
                if (guess<num):
                    print("\033[1mLOWER...\033[0m")
                else:
                    print("\033[1mHIGHER...\033[0m")
                print()

    border(newgame)
    inp=input("y/n : ")
    if inp.lower()=='n':
        break
