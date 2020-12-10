""" Program author name: Analia Treviño-Flitton
- This function creates a dictionary from a file read in with two strings on each line.
- The first string will serve as the dictionary key and the second string as the value
"""


def dictionary_builder(file_name):
    # Open & Read into list
    openfile = open(file_name, 'r').readlines()

    # Create empty dictionary
    misc = {}

    for line in openfile:
        # Remove space from ends & split each line(list) into another list
        line = line.rstrip("\n").split()

        # Write 1st position to key & 2nd to value for each item in line(list)
        for i in line:
            misc[line[0]] = (line[1])

    # Print
    print("The completed dictionary is:\n", misc, "\n\n\n")


dictionary_builder('builder_input.txt')
