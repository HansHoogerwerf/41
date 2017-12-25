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

def findNextChars(index):
    result = []
    for i, v in enumerate(matrix[index]):
        if(v > 0):
            result.append((abc[i], v, i))
    return result

def chooseCharacter(index):
    result = 0
    result2 = 0
    for value in row:
        result += value
    for j in range (0, len(matrix)):
        result2 += matrix[j][i]
    if(result > result2):
        print(result, result2)
    sentence.append(abc[index])
    print('Current sentence:', ''.join(sentence))
    chars = findNextChars(index)
    print(chars)
    c = int(input("What value do you want to use? (0-n)"))
    matrix[index][chars[c][2]] -= 1
    print(matrix[index][chars[c][2]])
    chooseCharacter(chars[c][2])

for i, row in enumerate(matrix):
    result = 0
    result2 = 0
    for value in row:
        result += value
    for j in range (0, len(matrix)):
        result2 += matrix[j][i]
    if(result > result2):
        print("start:")
        print(i)
        chooseCharacter(i)

