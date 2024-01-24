'''Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then use it to print the flower name with the same first letter (from dictionary created in the first function).
'''
# Sample Output: ``` >>> Enter your First [space] Last name only: Bill Newman
# >>> Unique flower name with the first letter: Bellflower


def flower_dict(filename):
    flowers_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            letter = line.split(": ")[0].lower() 
            flower = line.split(": ")[1].strip()
            flowers_dict[letter] = flower
    return flowers_dict

# print(flower_dict('flowers.txt'))


def main():
    flower_d = flower_dict('flowers.txt')
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
## print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()
