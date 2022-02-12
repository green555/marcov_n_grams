"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)
    one_string = file.read().strip()

          

    return one_string


def make_chains(text_string, N):
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
    
    
    
    words = text_string.split()
    n = N
    for i in range(len(words) - n):
        key_n_words_list = words[i : i + n]        
        key_n_words = tuple(key_n_words_list)
        
        #chains[key_n_words] = list(chains.get(key_n_words, None)).append(words[i + n])
        if chains.get(key_n_words):
            chains[key_n_words].append(words[i + n])
        else:
            chains[key_n_words] = [words[i + n]]          
          
 
  
    return chains


def make_text(chains, N):
    """Return text from chains."""

    start_key = choice(list(chains.keys()))
    n = N
    words = []
    
    while True:

        words[len(words):] = list(start_key)        
        word_nrd = choice(chains[start_key])
        words.append(word_nrd)
        new_key = tuple(words[-n:])
        start_key = new_key
        if chains.get(start_key) == None:
            break
    
            
    
   

    # your code goes here

    return ' '.join(words)


input_path = sys.argv[1]
n = int(input("Please enter an integer: "))

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)


print(random_text)
