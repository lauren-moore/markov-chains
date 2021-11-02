"""Generate Markov text from text files."""
# import re
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    open_file = open(file_path)

    ##TODO: cleanup special characters with regex replace
        ##for i, word in enumerate(word_list):
            ##word_list[i] = re.sub('[^\w+]', '', word_list[i]).lower()

    return open_file.read()


def make_chains(text_string, input_num):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}


    text_list = text_string.replace("\n", " ").split(" ")
    text_list.remove("")

    for i in range(len(text_list) - input_num):

        tuple_prep = []
       
        for i_2 in range(input_num):
            tuple_prep.append(text_list[i + i_2])
        key = tuple(tuple_prep)

        value = text_list[i + input_num]
    
        if key not in chains:
            chains[key] = []
        chains[key].append(value)

    return chains


def make_text(chains, input_num, text_string_2):
    """Return text from chains."""
    text_list = text_string_2.replace("\n", " ").split(" ")
    text_list.remove("")

    words = []

    key = choice(list(chains.keys()))
    words.extend(list(key))

    # list(choice.keys())

    

    while True:
        
        next_word = choice(chains[key])
        words.append(next_word)

        dummy_list = []
        for x in range(1, input_num):
            dummy_list.append(key[x])
        dummy_list.append(next_word)
        key = tuple(dummy_list)
    
        if key == tuple(text_list[-input_num:]):
            break

    return ' '.join(words)




# Ask user for how many words they want in a key
    # e.g. 3 = use 3 words for the key
# user_num = int(input("input an int btwn 1-10 >"))
user_num = 3

# input_path = sys.argv[1]
input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
# Get a Markov chain
chains = make_chains(input_text, user_num)
# Produce random text
random_text = make_text(chains, user_num, input_text)
# Print result!
# print(random_text)


