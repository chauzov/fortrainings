# task: write method to generate Marco's replies

# coding=utf-8
import random
import os, sys

greeting = """
Hi,

"""

numberOfPhrases = 5

signature = """


John Doe
+1 555 800 3444
"""


dicList = []

with open('john.dic') as a_file:
    for line in a_file:
        dicList.append(line)

reply = greeting

for i in range(1, numberOfPhrases):
    pos = random.randrange(len(dicList))
    line = dicList[pos]
    dicList[pos] = dicList[-1]
    del dicList[-1]
    line = line.rstrip('\n')
    reply = reply + ' ' + line

reply = reply + signature

print reply
