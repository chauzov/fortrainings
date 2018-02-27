# task: fill this script with comments about every
# line and method, explain what it will do

line_number = 0
with open('file') as a_file:
    for a_line in a_file:
        line_number += 1
        print('{0:>4} {1}'.format(line_number, a_line.rstrip()))
