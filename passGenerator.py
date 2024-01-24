'''Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. Your function should not accept any arguments and should reference the global variable word_list to build the password. To help with this, check out the choice/sample function associated with the random module in the Standard Library.
'''


import random
# We begin with an empty `word_list`
word_file = "words.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# TODO: Add your function generate_password below
def generate_password():
    return ''.join(random.sample(word_list, 3))
  # return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

# It should return a string consisting of three random words
# concatenated together without spaces

# Now we test the function
password = generate_password()
print(password)  # 'peepedtwicewhat'