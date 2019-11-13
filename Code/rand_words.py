import random
import sys
import cProfile

def sample_words():
    f = open('/usr/share/dict/words')
    words_list = f.readlines()
    length = len(words_list)

    print()
    for i in range(int(sys.argv[1])):
        print(words_list[int(random.random() * length)])

if __name__ == "__main__":
    cProfile.run('sample_words()')
    