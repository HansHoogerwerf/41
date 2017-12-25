import copy
import csv

abc = list("abdefghijklmnorstuv")
sentence = []
matrix = [
    [0,0,0,0,0,0,0,0,0,0,0,0,3,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,2,1,0,0,1,0,1,1,0,3,0,1,0,5,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,1,0,2,0,0,0,1,0,0],
    [0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,4,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,2],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0],
    [0,0,0,3,0,0,3,0,0,0,0,0,0,0,0,1,0,0,1],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
    [2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

for i, row in enumerate(matrix):
    result1 = 0
    result2 = 0
    for value in row:
        result1 += value
    for j in range(0, len(matrix)):
        result2 += matrix[j][i]
    print(abc[i], result1, result2)

class step:
    def __init__(self,index, options, previous, matrix):
        self.index = index
        self.options = options
        self.previous = previous
        self.currentMatrix = copy.deepcopy(matrix)


def findNextChars(index, matrix):
    result = []
    for i, v in enumerate(matrix[index]):
        if(v > 0):
            result.append((abc[i], v, i))
    return result



def procesStep(prevStep, sentence):
    for char in prevStep.options:
        matrix = copy.deepcopy(prevStep.currentMatrix)
        matrix[prevStep.index][char[2]] -= 1
        options = findNextChars(char[2], matrix)
        # print(options)
        if(len(options) == 0 and len(sentence) == 74):
            print(sentence)
            return
        s = step(char[2], options, prevStep, matrix)
        # matrix[index][chars[2]] -= 1

        procesStep(s, copy.copy(sentence + abc[char[2]]))

    # matrix[index][chars[c][2]] -= 1
    # print(matrix[index][chars[c][2]])
    # chooseCharacter(chars[c][2])

def posibleWord(word, matrix):
    m = copy.deepcopy(matrix)
    for char in word:
        if char not in abc:
            return (None, None,False)

    chars = findNextChars(abc.index(word[0]), m)
    removeChar = word[0]
    word = word[1:]
    if(len(word) == 0):
        return (m, findNextChars(abc.index(removeChar[0]), m), True)
    for c in chars:
        # print(c)
        try:
            if(c[0] == word[0]):
                index = abc.index(removeChar)
                m[index][c[2]] -= 1
                return posibleWord(word, m)
        except:
            pass
            # print("ERROR",word)
    return (m, findNextChars(abc.index(removeChar[0]), m), False)

words = []
possibleWords = []

def findWords(m):
    for word in words:
        if posibleWord(word, m)[2]:
            possibleWords.append(word)
            print(word)


with open('lijst.txt', newline='') as csvfile:
    wordreader = csv.reader(csvfile, delimiter='/', quotechar='|')
    for row in wordreader:
        word = str.lower(row[0])

        words.append(word)
    # findWords(matrix)
    # with open('1.txt', newline='') as t1:
    #     wordreader1 = csv.reader(t1, delimiter='}', quotechar='|')
    #     for row in wordreader1:
    #         word = str.lower(row[0])
    #         if word not in words:
    #             words.append(word)
    #     with open('2.txt', newline='') as t2:
    #         wordreader2 = csv.reader(t2, delimiter='}', quotechar='|')
    #         for row in wordreader2:
    #             word = str.lower(row[0])
    #             if word not in words:
    #                 words.append(word)
    #         with open('3.txt', newline='') as t3:
    #             wordreader3 = csv.reader(t3, delimiter='}', quotechar='|')
    #             for row in wordreader3:
    #                 word = str.lower(row[0])
    #                 if word not in words:
    #                     words.append(word)
    #             with open('4.txt', newline='') as t4:
    #                 wordreader4 = csv.reader(t4, delimiter='}', quotechar='|')
    #                 for row in wordreader4:
    #                     word = str.lower(row[0])
    #                     if word not in words:
    #                         words.append(word)


print(len("ookheeftsluitheteilandsluitmeteenverbindingmethetvastelandendijken"))
testwords = [
    # 'meteenverbindingmethetvasteland',
    # misschien eiland?
    # 'meteenverbindingmethetvastelanden',
    # 'sluitheteiland',
    # 'dijken',

    # 'het',
    'sluit',
    # 'meteenverbindingmethetvastelandendijkenvan',

    # 'heteilandje',
    'ookheeft',
    'meteenverbindingmethetvastelandendijken',
    'sluitheteiland',

]

m = copy.deepcopy(matrix)
for tw in testwords:
    answer = posibleWord(tw, m)
    print(tw, answer[1], answer[2])
    m = copy.deepcopy(answer[0])

# findWords(m)


#
# index = abc.index("n")
# options = findNextChars(index, m)
# s = step(index, options, None, m)
# sentence = "ookheeftsluitheteilandsluitmeteenverbindingmethetvastelandendijken"
# procesStep(s, sentence)
# for i, row in enumerate(m):
#     options = findNextChars(i, m)
#     print(options)
#     # matrix[prevStep.index][char[2]] -= 1
#     s = step(i, options, None, m)
#     procesStep(s, abc[i])


