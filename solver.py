from english_words import get_english_words_set
words = get_english_words_set(['web2'], lower=True)

five_words = []

for word in words:
    if len(word) == 5:
        five_words.append(word)

words = five_words.copy()
words_left = []

while words != '':
    del words_left[:]
    letter = input('What Letter do you know?')
    color = input('What color is the letter? (g, y, b)')
    if color == 'g':
        position = int(input('What position is the letter? (1-5)'))
        for word in words:
            if word[position - 1] == letter:
                words_left.append(word)
    elif color == 'y':
        position = int(input('What position is the letter? (1-5)'))
        for word in words:
            if letter in word and word[position] != letter:
                words_left.append(word)
    elif color == 'b':
        words_left = words.copy()
        for word in words:
            if letter in word:
                words_left.remove(word)

    print(*words_left)
    words = words_left.copy()



