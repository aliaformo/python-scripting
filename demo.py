f = open('some_file.txt', 'r')
file_data = f.read()
f.close()
print(file_data)

'''Hello!!
You've read the contents of this file!'''

# ------


file = open('another_file.txt', 'w')
file.write('Hello World!')
f.close()
# Created the another... file

# ----------------------------------------------------------------

with open('with_method.txt', 'r') as f:
    file_data_with = f.read()
print(file_data_with)

# Trying The with method to handle files!!!

# ----------------------------------------------------------------

with open("camelot.txt") as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

'''We
're the
knights of the round table
We dance whenever we're able'''


# ----------------------------------------------------------------
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)
# ["We're the knights of the round table", "We dance whenever we're able"]


# ----------------------------------------------------------------

'''Write a function called create_cast_list that takes a filename as input and returns a list of actors' names. It will be run on the file flying_circus_cast.txt (this information was collected from IMDB.com). Each line of that file consists of an actor's name, a comma, and then some (messy) information about roles they played in the programme. You'll need to extract only the name and add it to a list. You might use the .split() method to process each line.
'''


def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(',')[0]
            cast_list.append(name)
    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
print(cast_list)

['Graham Chapman',
 'Eric Idle',
 'Terry Jones',
 'Michael Palin',
 'Terry Gilliam',
 'John Cleese']
