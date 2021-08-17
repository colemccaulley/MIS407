"""Read a text file."""

with open("test.txt", "r") as file:
    line_number = 0
    for line in file:
        line_number += 1
        line = line.rstrip()
        print("Line {}: {}".format(line_number, line))
