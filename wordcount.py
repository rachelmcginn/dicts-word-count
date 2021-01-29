# put your code here.

def wordcount(file_name):
    the_file = open(file_name)
    all_words = []

    for line in the_file:
        line = line.rstrip()
        all_words.extend(line.split(' '))

    word_count = {}
    for word in all_words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    
    for word, count in word_count.items():
        print(f"{word} {count}")

wordcount('test.txt')



