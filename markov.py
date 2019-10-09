"""Generate Markov text from text files."""

from random import choice
file = open("green-eggs.txt")

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
    for key, value in chains.items():
        print(key, value)

    return chains

chains = make_chains(text_string)

def make_text(chains):
    """Return text from chains."""

    words = []

    first_value = list(chains.values())[0]
    random_value = choice(first_value)
    second_word_first_key = list(chains.keys())[0][1]
    first_word_first_key = list(chains.keys())[0][0]
    words.append(first_word_first_key)
    words.append(second_word_first_key)
    words.append(random_value)
    new_tuple = tuple(words[-2:])

    while True:
        if new_tuple in chains:
            words.append(choice(chains[new_tuple]))
            new_tuple = tuple(words[-2:])
        else:
            break

    # print(words)
    # print (" ".join(words))
    return " ".join(words)
print(make_text(chains))

# print(make_text(make_chains("text_string")))


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
