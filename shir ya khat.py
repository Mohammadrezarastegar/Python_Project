while 1>0:
    player_1 = input("lotfan entekhab konid : shir ya khat ?")
    player_1 = str.lower(player_1)
    if player_1 == "shir":
        print("player_1 : 🦁")
    elif player_1 == "khat":
        print("player_1 : ➖")
    else:
        print("entekhab shoma ghalat mibashad")
    import random as rn
    randint = rn.randint(1 , 2)
    davar = randint
    if davar == 1:
        print("davar : 🦁")
    elif davar == 2:
        print("davar : ➖")
    if player_1 == "shir" and davar == 1:
        print("player_1 barande : 😊 ")
    elif player_1 == "shir" and davar == 2:
        print("player_1 bazande ☹️")
    elif player_1 == "khat" and davar == 1:
        print("player_1 bazande ☹️")
    elif player_1 == "khat" and davar == 2:
        print("player_1 barande : 😊")