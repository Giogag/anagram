"""
    load the dictionary file as a list of words
    make an empty list to hold the palindromes
    loop through each word in the wordlist:
        if  word sliced is the same as the normal one:
            append it to the palindromes list

    print the palindromes list.


"""
import load_dictionary

word_list = load_dictionary.load("dictionary")

paledin = []

for item in word_list:
 if item == item[::-1]:
  paledin.append(item)
print(*paledin, sep='\n')