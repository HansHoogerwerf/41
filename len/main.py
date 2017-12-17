__author__ = 'Hans'
import copy
print(len('FiJnEkErStDaGeNToegewenst!'))



speelboord = [
    '!ONNrOOgOenrrE!k!r!k!',
    '!EaaaeOggnDrrErEJJJE!',
    '!ENNNeOggnrDrErErwwE!',
    '!EOONeOggeDDJEnEwwrE!',
    '!EnONeOgnnDDAEnEkkkEr',
    '!EEaaeOgUDnDnEnEEEEEk',
    'rnOnnnOJnDnDnErkwwwww',
    'FFFFFFFFFFFFFFFFFFFFF',
    'AnOnOOOtgDnnEEEnwJJJw',
    'nnOaaEeSnDnEUnEnwwwwJ',
    'AnJtttOgnDDEEAnEJwwww',
    'nJJEttggEDDEEAnnUJIwe',
    'rnJEEttEEDnEUDJIIwIee',
    'JJJJJJJgnDnEUJUUIUIee',
    '!ntttttgSnEEDUUEUIwww',
    'OEEEaAtiSEEnDEEEwUeJU',
    'rAr!rAOiSnEDUEEUEUeUE',
    'UAr!!AOiSnnDSEEEEUUEE',
    'UArrrJOiSSSSEEEUUUEEE',
    'UAAAAJOiSiSEEEEEEEUEU',
    'UUUUUUOiiiSSDAJJUEEEE'
]

testboard = [
    ['t','e','s','t'],
    ['k','e','s','t'],
    ['k','k','k','k'],
    ['r','e','r','s']
]


def printspeelboord(boord):
    for i in range(0, len(boord)):
        boord[i] = list(boord[i])
        # print(boord[i])


def findPosibility(boord, position, touchedplaces):
    positions = []
    check = touchedplaces[position[0]][position[1]]
    if check == False and boord[position[0]][position[1]] != " ":
        positions.append(position)
        touchedplaces[position[0]][position[1]] = True
        #bottom check
        #bounds check
        if(len(touchedplaces) > position[0] + 1):
            # check if not touched
            if(touchedplaces[position[0] + 1][position[1]] == False):
                # check if the same
                if(boord[position[0]][position[1]] == boord[position[0] + 1][position[1]]):
                    positions = positions + (findPosibility(boord, ((position[0] + 1), position[1]), touchedplaces))
        #right check
        #bounds check
        if(len(touchedplaces[0]) > position[1] + 1):
            # check if not touched
            if(touchedplaces[position[0]][position[1] + 1] == False):
                # check if the same
                if(boord[position[0]][position[1]] == boord[position[0]][position[1] + 1]):
                    positions = positions + (findPosibility(boord, ((position[0]), position[1] + 1), touchedplaces))
        # left check
        if(position[1] - 1 >= 0):
            # check if not touched
            if(touchedplaces[position[0]][position[1] - 1] == False):
                # check if the same
                if(boord[position[0]][position[1]] == boord[position[0]][position[1] - 1]):
                    positions = positions + (findPosibility(boord, ((position[0]), position[1] - 1), touchedplaces))
        #top check
        if(position[0] - 1 >= 0):
            if(touchedplaces[position[0] - 1][position[1]] == False):
                # check if the same
                if(boord[position[0]][position[1]] == boord[position[0] - 1][position[1]]):
                    positions = positions + (findPosibility(boord, ((position[0] - 1), position[1]), touchedplaces))
        return positions
    else:
        return positions


def findPosibilities(boord, letter):
    posibilties = []
    touchedPlaces = []
    for i in range(0, len(boord)):
        touchedPlaces.append([])
    for i in range(0, len(touchedPlaces)):
        for j in range(0, len(boord[0])):
            touchedPlaces[i].append(False)
    for i in range(0, len(boord)):
        for j in range(0, len(boord[i])):
            posibilty = findPosibility(boord, (i,j), touchedPlaces)
            if(len(posibilty) > 1):
                posibilties.append(posibilty)
    return posibilties

def prettyPrintPosibility(posibilty, boord):
    print("posibility", posibilty)
    print("size:", len(posibilty))
    print("symbol:", boord[posibilty[0][0]][posibilty[0][1]])
    tempList = copy.deepcopy(boord)
    print("Current board:")
    for row in boord:
        print(row)
    print("Location of posibility:")
    for i in range(0, len(tempList)):
        for j in range(0, len(tempList[i])):
            if((i, j) not in posibilty):
                tempList[i][j] = " "
        print(tempList[i])
    return boord[posibilty[0][0]][posibilty[0][1]]

def removePosibility(posibility, boord):
    for location in posibility:
        # print(location)
        boord[location[0]][location[1]] = " "


def fixBoord(boord):
    #remove empty colums
    rowlenght = len(boord[0])
    collenght = len(boord)
    for i in range(0, rowlenght):
        if(emptyCol(boord, i)):
            for j in range(0, collenght):
                boord[j].pop(i)
            # call itself to reset
            fixBoord(boord)
            break
    # #remove empty rows
    # for i in range(0, len(boord)):
    #     if(emptyRow(boord, i)):
    #         boord.pop(i)
    #         fixBoord(boord)
    #         break
    #now that we have the right dimension again we will use gravity
    usedGrav = False
    for i in reversed(range(0, len(boord))):
        for j in range(0, len(boord[i])):
            if(boord[i][j] == " "):
                replaceWith = " "
                for k in reversed(range(0, i)):
                    if boord[k][j] != " ":
                        usedGrav = True
                        replaceWith = copy.copy(boord[k][j])
                        boord[k][j] = " "
                        break
                boord[i][j] = replaceWith
    if usedGrav:
        fixBoord(boord)


def emptyCol(boord, colIndex):
    for row in boord:
        if (row[colIndex] != " "):
            return False
    return True

def emptyRow(boord, rowIndex):
    for col in boord[rowIndex]:
        if (col != " "):
            return False
    return True



def main(boord):
    printspeelboord(boord)
    sentence = ""
    while(True):
        print("Current sentence:", sentence)
        letterChoice = input("Do you want to specify a letter? (y/n)")
        letter = ""
        if(str.lower(letterChoice) == 'y'):
            letter = input("Which letter? (a-z/A-Z/!)")
        posibilties = findPosibilities(boord, letter)
        posibilties = sorted(posibilties, key=lambda p: len(p), reverse = True)
        for posibilty in posibilties:
            symbol = prettyPrintPosibility(posibilty, boord)
            if(letter == "" or symbol == letter):
                d = input("Remove this option? (y/n)")
                if(str.lower(d) == 'y'):
                    print("remove!")
                    removePosibility(posibilty, boord)
                    fixBoord(boord)
                    sentence += symbol
                    break
        if len(posibilties) == 0:
            print("done")
            print(sentence)
            break
main(speelboord)



# letters = []
# for row in speelboord:
#     for letter in row:
#         if letter not in letters:
#             letters.append(letter)
# print(sorted(letters))