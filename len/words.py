from _codecs import encode

__author__ = 'Hans'
import csv
import copy

def itemInString(item, string):
    return item in string

def testFunc(string, subarray):
    for item in subarray:
        if itemInString(item, string) == False:
            return False
    return True



allowedChars = "abdeghilnostu"
ac = 'abc'
allowedCharsPoints = {
    "a":188461,
    "b":565383,
    "d":696149,
    "e":88447,
    "g":265341,
    "h":796023,
    "i":388069,
    "l":164207,
    "n":492621,
    "o":447863,
    "s":433589,
    "t":300767,
    "u":902301
}

possibilities = [
    'habben',
    'aabbgilssttu',
    'allo',
    'aaeehhossttu',
    'aaglou',
    'aensst',
    'aaghhlssttuu',
    'aaghou',
    'aehins',
    'hi',
    'dan',
    'hut',
    'eggiilst',
    'atuu',
    'abdinnu',
    'euu',
    'aabbddeggiils',
    'nu',
    'aeehhlssttuu'
]
possibilitiesPoints = [
    696318,
    994738,
    186634,
    937474,
    818450,
    818450,
    184092,
    377231,
    999091,
    293830,
    725605,
    893049,
    394922
]
possibilitiesAnwers = {
    696318: [],
    994738: [],
    186634: [],
    937474: [],
    818450: [],
    387210: [],
    184092: [],
    377231: [],
    999091: [],
    293830: [],
    725605: [],
    893049: [],
    394922: []
}

words = []

def encrypt(word):
    result = 0
    for char in word[0]:
        result += allowedCharsPoints[char]
    return result % 1e6



def toManyChars(p, word):
    for char in p:
        c1 = p.count(char)
        c2 = word.count(char)
        if(c1 != c2):
            return False
    return True

def findPosibilties():
    poplist = []
    for i, word in enumerate(words):
        words[i] = (word, {})
        for char in word:
            if(char not in allowedChars):
                poplist.append(i)
                break
            words[i][1][char] = word.count(char)
    for p in reversed(range(0, len(poplist))):
        words.pop(poplist[p])
    for word in words:
        e = encrypt(word)
        if(e in possibilitiesPoints):
            possibilitiesAnwers[e].append(word[0])
    for p in possibilitiesPoints:
        print(p, possibilitiesAnwers[p])

def bruteforce():
    for i, char in enumerate(ac):
        result = ""
        for j in  range(i, len(ac)):
            for k in range(0,2):
                result += ac[j]
                words.append(copy.copy(result))
                print(result)
        for j in  range(0, 1):
            for k in range(0,2):
                result += ac[j]
                words.append(copy.copy(result))
                print(result)
#
# print(["lastig"])
# print(encrypt(["lastig"]))
# print(["he"])
# print(encrypt(["he"]))
bruteforce()
# print(words)
findPosibilties()


# with open('lijst.txt', newline='') as csvfile:
#     wordreader = csv.reader(csvfile, delimiter='/', quotechar='|')
#     for row in wordreader:
#         word = str.lower(row[0])
#         words.append(word)
#
#     with open('1.txt', newline='') as t1:
#         wordreader1 = csv.reader(t1, delimiter='}', quotechar='|')
#         for row in wordreader1:
#             word = str.lower(row[0])
#             words.append(word)
#         with open('2.txt', newline='') as t2:
#             wordreader2 = csv.reader(t2, delimiter='}', quotechar='|')
#             for row in wordreader2:
#                 word = str.lower(row[0])
#                 words.append(word)
#             with open('3.txt', newline='') as t3:
#                 wordreader3 = csv.reader(t3, delimiter='}', quotechar='|')
#                 for row in wordreader3:
#                     word = str.lower(row[0])
#                     words.append(word)
#                 with open('4.txt', newline='') as t4:
#                     wordreader4 = csv.reader(t4, delimiter='}', quotechar='|')
#                     for row in wordreader4:
#                         word = str.lower(row[0])
#                         words.append(word)
#                     findPosibilties()


    # for p in possibilities:
    #     print()

        # for word in allwords(p, len(p)):
        #     if(toManyChars(p, word)):
        #         if(word in words):
        #             print(p, word)


