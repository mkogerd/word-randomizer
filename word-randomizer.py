import json
import sys
import random

# Read in our dictionary dictionary
with open('english-words/words_dictionary.json') as f:
    english_dict = json.load(f)

# Do some rough input validation
if (len(sys.argv) < 2):
    raise ValueError('Please provide a single character as an argument.')

letter = sys.argv[1]
if (len(letter) is not 1):
        raise ValueError('first argument must be a single character.')

# grab and shuffle a list of only the letters we are interested in
words_starting_with_letter = [word for word in english_dict.keys() if word[0] == letter]
random.shuffle(words_starting_with_letter)

print('Randomized {} words starting with "{}". Press enter to display one word at a time.'.format(len(words_starting_with_letter), letter))

for word in words_starting_with_letter:
    # Print out
    # raw_input is python 2 specific, must be changed to input() for py3
    raw_input('')
    print(word)
