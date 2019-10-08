"""Generate Markov text from text files."""

from random import choice
# file = open("green-eggs.txt")

def open_and_read_file(file):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # your code goes here
    contents = open("green-eggs.txt").read()
    return contents
print(open_and_read_file("green-eggs.txt"))

text_string = open_and_read_file("green-eggs.txt")
def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    
    words = text_string.split()
    chains = {}

    for i, word in enumerate(words):
        if i < len(words)-1:
            bigram = (words[i], words[i+1])
        if i < len(words)-2:
            value = words[i+2]
            if bigram not in chains:
                chains[bigram] = [value]
            else:
                chains[bigram].append(value)



    print(chains)
    return sorted(key)
print(make_chains(text_string))

    # return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
