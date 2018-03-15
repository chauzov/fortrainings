# task: fill this script with comments about every
# line and method, explain what it will do

#set line counter to 0
line_number = 0
# open the file with the name 'file' with the descriptor a_file
with open('file') as a_file:
    # enumerate lines in the file
    for a_line in a_file:
        # increase the line counter with every line
        line_number += 1
        # print the line counter right-justified and reserved 4-character space, print a line from the file withot spaces on the end
        print('{0:>4} {1}'.format(line_number, a_line.rstrip()))
