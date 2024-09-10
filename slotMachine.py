import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3


symbol_count = {
    "A": 14,
    "B": 16,
    "C": 20,
    "D": 32
}
symbol_value = {
    "A": 7,
    "B": 6,
    "C": 5,
    "D": 4
}


def check_winnings(Columns, lines, bet, value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = Columns[0][line]
        for colum in Columns:
            symbol_to_check = colum[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += value[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spine(rows, cols, symbol_count):
    all_symbols = []
    for symbol, symbol_count in symbol_count.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    Columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        Columns.append(column)

    return Columns


def print_solot_machine(Colums):
    for row in range(len(Colums[0])):
        for i, column in enumerate(Colums):
            if i != len(Colums) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input('what would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('amount most be greater than 0 and less than 1000.')
        else:
            print('please enter a number.')

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('enter a valid number of lines.')
        else:
            print('please enter a number.')
    return lines


def get_bet():
    while True:
        amount = input('what would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'amount must be between ${MIN_BET} and ${MAX_BET}')
        else:
            print('please enter a number.')

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f'you do not have enough to bet that amount, your current balance is ${balance}')
        else:
            break
    print(
        f'You are betting ${bet} on {lines} lines. Total bet is equal to: {total_bet}')

    slots = get_slot_machine_spine(ROWS, COLS, symbol_count)
    print_solot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'you won: ${winnings}')
    print('you won on lines:', *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f'current balance is ${balance}')
        answer = input('press enter to play (q to quit)')
        if answer == 'q':
            break
        balance += spin(balance)

    print(f'you left with ${balance}')


main()
