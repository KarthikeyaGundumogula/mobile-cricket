import random
def player_batting(bat_score,com_score):
    while True:
        print("your current score is",bat_score)
        b_y=int(input("your turn"))
        c_x=random.randint(1,10)
        print("computer-",c_x)
        if c_x==b_y:
            print("out")
            break
        else:
            bat_score=bat_score+b_y
    print('your total score is ', bat_score)
    print('you have to feild now')
    while True:
        print("computer's present score is ",com_score)
        c_s=random.randint(1,10)
        p_s=int(input("your turn"))
        print("computer hits ",c_s)
        if c_s==p_s:
            print('out')
            break
        else:
            com_score=com_score+c_s
    print("computer score is ",com_score)
    if bat_score<com_score:
        print("you lost")
    elif com_score<bat_score:
        print("you won")
    else:
        print("match is tied")
def computer_batting(score,p_score):
    print("you have to feild now")
    while True:
        y=random.randint(1,10)
        print("computer's current score ",score)
        x=int(input("your turn"))
        print("computer scored ",y)
        if y==x:
            print('out')
            break
        else:
            score=score+y
    print("compuer score is ", score)
    while True:
        print("your current score is ",p_score)
        p_x=int(input("your turn"))
        p_y=random.randint(1,10)
        print("computer-",p_y)
        if p_x==p_y:
            print("out")
            break
        else:
            p_score=p_score+p_x
    print("your score is ",p_score)
    if score<p_score:
        print("you won")
    elif score > p_score:
        print("you lost")
    else:
        print(' match tied')