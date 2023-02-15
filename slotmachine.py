import random

MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100


def deposit():
    while True:
        cash = input("Add cash here!\n")
        if cash.isdigit():
            cash = int(cash)
            if cash > 0:
                break
            else:
                print("Please enter a valid amount")
        else:
            print("Please enter some digits")
    return cash


def line():
    while True:
        lines = input("select the number of line(or lines) you want bet on : ")
        if lines.isdigit():
            lines = int(lines)
            if 0 <= lines <= 3:
                break
            else:
                print("Please enter a number between 0 to 3")
        else:
            print("Please enter some digits")
    return lines


def bets():
    while True:
        amount = input("what amount you would like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter a number between {MIN_BET} and {MAX_BET}")
        else:
            print("Add digits or numbers please")
    return amount


def summary():
    while True:
        global be
        global de
        global li
        total_bet = be*li
        current_balance = de-(be*li)
        if current_balance >= 0:
            print(f"you have bet {be} on each line ,so the total bet becomes {total_bet} with balance {current_balance}")
            break
        else:
            select = input("oops your bet exceeds the balance!\nwhat would you like, add more balance (type balance) or lower down your bet (type bet) or lower your no. of lines you want to bet on (type lines)")
            if select == "bet":
                be = bets()
            if select == "balance":
                de += deposit()
            if select == "lines":
                li = line()
            else:
                print("Please choose from the above provided options")
    return


def spin():
    symbols = ["A", "B", "C", "D"]
    collection = []
    while len(collection) <= 9:
        a = random.choice(symbols)
        collection.append(a)
    for i in range(0, 3):
        print(f"{collection[3*i]} | {collection[(3*i)+1]} | {collection[(3*i)+2]}")
    return


def winlose():
    global winning
    global lose
    if li >= 1:
        if list[0] == list[1] == list[2]:
            winning += be
        else:
            lose += be
    if li >= 2:
        if list[3] == list[4] == list[5]:
            winning += be
        else:
            lose += be
    if li >= 3:
        if list[6] == list[7] == list[8]:
            winning += be
        else:
            lose += be
    return winning, lose


de = deposit()
while True:
    li = line()
    be = bets()
    su = summary()
    sp = spin()
    winning = 0
    lose = 0
    wi = winlose()
    print(f"So you win {winning} and lose {lose}")
    de += winning - lose
    print(f"Your net balance becomes {de}")

    while True:
        replay = input("wanna play again (yes or no)?")
        if replay == "yes":
            break
        if replay == "no":
            exit()
        else:
            print("please enter from the provided options")
            continue
    continue
