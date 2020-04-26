import random
while True:
    from Cricket import player_batting 
    from Cricket import computer_batting
    toss=int(input("plese enter your choice [1 or 2]"))
    x=random.randint(1,2)
    if toss==x:
        print("you won the toss")
        choice=input("enter your choice batting or feilding[b/f]")
        bat_score=0
        com_score=0
        if choice=="b":
            print("you choose to bat")
            player_batting(bat_score,com_score)
        if choice=="f":
            print("you chooseto feild first")
            score=0
            p_score=0
            computer_batting(score,p_score)
    else:
        print("computer won the toss")
        k=random.randint(1,2)
        if k==1:
            print("computer wants to bat ")
            score=0
            p_score=0
            computer_batting(score,p_score)
        else:
            print("computer wants to feild")
            x=0
            y=0
            player_batting(x,y)
    print("thanks for playing")
    m=input("Are you willing to play a another match [Y/N]")
    if m==('n' or 'N'):
        print("bye")
        break
    else:
        continue