"""
load dictionary as list
create empty list for paligrams
for x in dictionary list:
    get word length
    if word length is greater than 1:
        loop through all letters
        if fragment of word in front is in the dictionary and letters after it form a palindrom:
            append word into pali list
        if fragment at the end of the word is in word list and letters before it form a palindrom:
            append reverse word and word to pali list
sort dictionary alfabeticly
"""
import load_dictionary

word_list = load_dictionary.load("2of4brif")

def find_paligram():
    """this will find all paligrams and sort it into one list"""
    palingrams = []
    for word in word_list:
        word_leng = len(word)
        word_flip = word[::-1]
        if word_leng > 1:
            for i in range(word_leng):
                if word[i:] == word_flip[:word_leng - i] and word_flip[word_leng - i:] in word_list:
                    palingrams.append((word, word_flip[word_leng - i:]))
                if word[:i] == word_flip[word_leng - i:] and word_flip[:word_leng - i] in word_list:
                    palingrams.append((word_flip[:word_leng - i], word))

    return palingrams

pali = find_paligram()

pali_sorted = sorted(pali)

print("\nNumber of paligrams found = {}\n".format(len(pali_sorted)))

print(pali_sorted)

for first, second in pali_sorted:
    print(f"{first} {second}")