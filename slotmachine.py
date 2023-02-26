# Slot Machine Rules
# Maximum bet can't be more than 5000
# Maximum number of lines to bet on can't be more than 3

import random

MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 5000

def calc(reel_slots, lines, bets):
    profit = 0
    loss = 0

    row1 = row2 = row3 = 0
    row1 += reel_slots[0] == reel_slots[1] == reel_slots[2]
    row2 += reel_slots[3] == reel_slots[4] == reel_slots[5]
    row3 += reel_slots[6] == reel_slots[7] == reel_slots[8]
    total = row1+row2+row3

    if(total >= lines):
        profit += bets*lines
    else:
        loss += bets*(lines-total)
        profit += bets*total

    return profit, loss
    

def spin(reel_slots):
    symbol_list = ["A", "B", "C"]

    while len(reel_slots) <= 9:
        symbol = random.choice(symbol_list)
        reel_slots.append(symbol)

    random.shuffle(reel_slots)

    for i in range(0, 3):
        print(f"{reel_slots[3*i]} | {reel_slots[(3*i)+1]} | {reel_slots[(3*i)+2]}")


def status(bets, balance, lines):
    while True:
        total_bet = bets * lines
        current_balance = balance - (bets * lines)
        
        if current_balance >= 0:
            print(f"You have bet {bets} on each line, so the total bet becomes {total_bet}")
            break
        else:
            select = input("Oops your bet exceeds the balance!\nWhat would you like?\n1: Add more balance (type balance)\n2: Lower down your bet (type bet)\n3: Lower your number of lines you want to bet on (type lines)\n")
            if select == "bet":
                bets = bets()
            elif select == "balance":
                balance += deposit()
            elif select == "lines":
                lines = line()
            else:
                print("Please choose from the above provided options only")
    return


def chooseBets():
    while True:
        amount = input("What amount you would like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter a number between {MIN_BET} and {MAX_BET}")
        else:
            print("Add digits or numbers please")
    
    return amount


def chooseLines():
    while True:
        lines = input("Select the number of line(or lines) you want bet on : ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a number between 1 to 3")
        else:
            print("Please enter some digits")
    
    return lines


def deposit():
    while True:
        cash = input("Add cash here! ")
        if cash.isdigit():
            cash = int(cash)
            if cash > 0:
                break
            else:
                print("Please enter a valid amount")
        else:
            print("Please enter some digits")
    
    return cash


if __name__ == '__main__':
    reel_slots = [] # For storing random combinations of symbols
    balance = deposit() # Returns cash amount to start the game
    
    while True:
        lines = chooseLines() # Returns the number of line selected by user
        
        bets = chooseBets() # Returns the amount of cash selected by user to bet upon each line
        
        status(bets, balance, lines) # Provides a comprehensive state of balance and the machine
        
        spin(reel_slots) # Prints the generated slot machine output

        profit, loss = calc(reel_slots, lines, bets) # Calculates loss and profit for user and returns as a tuple
        print(f"So you win {profit} and loss {loss}")
        
        balance += profit - loss # Adds the final scenario to the existing balance
        print(f"Your net balance becomes {balance}")

        while True:
            replay = input("Want to play again (yes or no)?")
            if replay == "yes":
                break
            if replay == "no":
                exit()
            else:
                print("Please enter from the provided options only")
                continue
        continue
