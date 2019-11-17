import sys
from hiptr import NormalHistogram
import bessemer

def read_in(normal_histogram):
    opened_file = open('fish.txt') # 
    text_body = opened_file.readlines()
    opened_file.close()

    words = []
    for line in text_body:
        for word in line.strip().split(' '):
            words.append(word)

    for word in words:
        normal_histogram.add(word)
    normal_histogram.build_percents()

def sample_some_words(normal_histogram):
    for count in range(int(sys.argv[1])):
        print(normal_histogram.choice(), end=' ')
    print()
    print()


if __name__ == "__main__":
    histogram = NormalHistogram('Jerry')
    read_in(histogram)
    sample_some_words(histogram)


