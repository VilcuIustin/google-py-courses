import random

def print_result():
    for i in range(1, 10):
        print(table[i - 1], end=" ")
        if (i % 3 == 0):
            print()


def random_start():
    return random.randint(0,2)


def bot_move(symbol):
    maked = False
    if table[4] in ("0", "X"):
        for i in {1, 3, 7, 9}:
            if table[i-1] not in ("0", "X"):
                table[i-1] = symbol
                return
        for i in {2, 4, 6, 8}:
            if table[i-1] not in ("0", "X"):
                table[i-1] = symbol
                return
    else:
        table[4] = symbol


def player_move(table, choice, symbol):
    if table[choice - 1] in ("0", "X"):
        print("you can't do this move. You need to mark where nobody is on that position")
    else:
        table[choice - 1] = symbol


def create_table():
    my_table = list()
    for i in range(1, 10):
        my_table.append(str(i))
    return my_table


def show_message_victory(player):
    print("{} won this game".format(player))


def is_game_done():
    contor = 0
    j = 0
    for i in range(0, 9):
        if table[i] == "X":
            contor += 1
        elif table[i] == "0":
            contor -= 1
        j += 1
        if (j % 3 == 0):
            if contor == 3:
                show_message_victory("player")
                print_result()
                return True
            elif contor == -3:
                show_message_victory("bot")
                print_result()
                return True
            contor = 0
    print(contor)
    for i in range(0,9,4):
        if table[i] == "X":
            contor += 1
        elif table[i] == "0":
            contor -= 1
    if contor == 3:
        show_message_victory("player")
        print_result()
        return True
    elif contor == -3:
        show_message_victory("bot")
        print_result()
        return True
    contor=0
    for i in range(2,7,2):
        if table[i] == "X":
            contor += 1
        elif table[i] == "0":
            contor -= 1
    if contor == 3:
        show_message_victory("player")
        print_result()
        return True
    elif contor == -3:
        show_message_victory("bot")
        print_result()
        return True
    contor=0
    for j in range(0,3):
        contor = 0
        for i in range(j,9,3):
            if table[i] == "X":
                contor += 1
            elif table[i] == "0":
                contor -= 1
        if contor == 3:
            show_message_victory("player")
            print_result()
            return True
        elif contor == -3:
            show_message_victory("bot")
            print_result()
            return True
    return False



table = create_table()
start=random_start()
if(start==0):
    print("Bot start first")
else:
    print("Player start first")
ok=True
while is_game_done() == False:
    if(start==0):
        bot_move("0")
        print_result()
        if is_game_done() == True:
            break
        while ok!=False:
            pos = input("Please enter the position you want to mark.")
            try:
                player_move(table, int(pos), "X")
                ok=False
            except:
                print("Please enter a valid number(0-9)")
                pass
        ok=True
    else:
        print_result()
        while ok != False:
            pos = input("Please enter the position you want to mark.")
            try:
                player_move(table, int(pos), "X")
                ok = False
            except:
                print("Please enter a valid number(0-9)")
                pass
        ok = True
        if is_game_done() == True:
            break
        bot_move("0")




