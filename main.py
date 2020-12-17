import signal
import sys
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def signal_handler(sig, frame):
    print('Finished by user!')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

class Round:
    def __init__(self):
        self.estimated = random.triangular(0.5, 2, 1)
        self.p = random.triangular(0,1)
        self.p100 = self.p * 100
        self.multiplier = self.estimated / self.p

    def print(self):
        print(f"You have a {self.p100:.2f}% of probability to multiply your bet by x{self.multiplier:.2f} ({self.estimated:.2f})")

    def play(self, bet):
        n = random.uniform(0,1)
        win = n < self.p
        if win:
            return int(bet * self.multiplier)
        return 0



print('Welcome!')
budget = 10000

def getInput():
    n = 0
    data = input()
    try:
        n = int(data)
    except:
        print('Must be integer')
        return -1
    if n < 0 or n > budget:
        print(f"Must be 0 < input < {budget}")
        return -1
    return n

round = 50

while round > 0:
    cls()
    print(f"--------------")
    print(f"Round {round}")
    print(f"Budget {budget}")
    r = Round()
    r.print()
    bet = -1
    while bet < 0:
        bet = getInput()
    budget = budget - bet
    budget = budget + r.play(bet)
    round = round - 1

print(f"Game finished with {budget}")