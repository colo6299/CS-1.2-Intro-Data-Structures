import sys
from random import random, randrange

def scrambler():
    # I'm guessing the blacklisted function is random.sample()? 
    # I used it for hist stuff in my spaceman, I think
    # No worries, I'll do something wacky for this :)

    end_chance = 0.01
    run_count = 0

    argl = sys.argv
    argl.pop(0)
    lehn = len(argl)

    while random() > end_chance:  # lol
        dindex = (10 * randrange(len(argl))) % lehn
        doutdex = (10 * randrange(len(argl))) % lehn
        hole_dir = argl[dindex]
        argl[dindex] = argl[doutdex]
        argl[doutdex] = hole_dir

        run_count += 1

    for word in argl:
        print(word, end=' ')
    
    print(f'\nThe mixer ran {run_count} times\n')

        
if __name__ == "__main__":
    scrambler()        
        



