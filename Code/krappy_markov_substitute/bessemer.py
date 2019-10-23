import string


def clean(filename):
    text = aesop()
    for sentence in text:
        sentence = sentence.strip()
        sentence = sentence.split(' ')
    

def aesop():
    f = open('aesop.txt', 'r')
    words_list = f.readlines()
    f.close()
    # print(words_list)
    s_prune = []
    for i in range(len(words_list)):
        if len(words_list[i]) < 80:
            s_prune.append(i)

    s_prune.reverse()
    for i in s_prune:
        words_list.pop(i)

    punc = '!"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~\n'
    
    sentences = []
    for sentence in words_list:
        for sentnew in sentence.split('.'):
            sentences.append(sentnew)

    for i in range(len(sentences)):  # Python, know only that I will have my vengance
        sentences[i] = sentences[i].translate(sentences[i].maketrans('', '', string.punctuation))
        
    s_prune = []
    for i in range(len(sentences)):
        if len(sentences[i]) < 4:
            s_prune.append(i)

    s_prune.reverse()
    for i in s_prune:
        sentences.pop(i)    
    # print(words_list)

    return sentences




if __name__ == "__main__":
    aesop()