import unidecode 

#Exercise 1--------------------------------
def capName():
    flag = 0
    while(flag == 0):
        ans = input("What is your name: ")

        if ans.isalpha():
            print(ans.upper())
            flag = 1
        else:
            print("Insert a valid name.")

# capName()

#Exercise 2---------------------------------

def printEven(list):
    even = []
    if (all([isinstance(item, int) for item in list])):
        for item in list:
            if item % 2 == 0:
                even.append(item)
            else:
                continue
        if len(even) == 0:
            print("The list dont have even numbers.")
        else:
            print("Even numbers: ",even)
    else:
        print("Not valid input.")
    

# printEven([323,4,55,2,4,1,4,5,6,6,76,7,6,4,53,4])

#Exercise 3---------------------------------
def printLinesRev(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    lines.reverse()
    for line in lines:
        line1 = line.replace("\n","") 
        print(line1)


# printLinesRev("notes.txt")

#Exercise 4---------------------------------

def moreOccur(fileName):
    formatedLines = []
    file = open(fileName, "r")
    lines = file.readlines()
    for line in lines:
        newLine = line.replace("\n","")
        if newLine != "":
            formatedLines.append(newLine)

    wordsDic = {}
    for line in formatedLines:
        for word in line.split():
            if word not in wordsDic:
                wordsDic[word] = 1
            else:
                wordsDic[word]=wordsDic[word]+1

    finalWords = sorted(wordsDic.items(), key=lambda x:x[1], reverse=True)
    for item in finalWords:
        print("\"", item[0],"\": ",item[1])

# moreOccur("notes.txt")

#Exercise 5---------------------------------

def cleanText(text):
    textLow = text.lower()
    textLow = unidecode.unidecode(textLow)
    print(textLow)
    punctuation = [",",".",";"]
    formated = ""
    for i in range(len(textLow)):
        if textLow[i] in punctuation:
            if i == len(textLow)-1:
                formated = formated + textLow[i]
            else:
                if textLow[i+1] != " ":
                    formated = formated + textLow[i]+ " "
                else:
                    formated = formated + textLow[i]
        else:
            formated = formated + textLow[i]

    print("formated: ",formated)

# cleanText("ola o meu nome É José Sántos e eu sou estudante do mestrado em engenharia BiomédiCa.Atualmente sou trabalhador e estudante,e deslocado.")

#FUNCTION EXERCISES---------------------------------------------------------
#Exercise 1---------------------------------

def reverseStr(word):
    word = word[::-1]
    print(word)

# reverseStr("jose")

#Exercise 2---------------------------------

def letterCounter(word, letter):
    counter = word.count(letter.upper()) + word.count(letter.lower())
    print("The word \"%s\" have %s letters \"%s\"." % (word, counter, letter))

# letterCounter("esternocleidomastoideo", "o")

#Exercise 3---------------------------------

def vowelsCounter(word):
    vowels="aeiou"
    counter = 0
    for i in word:
        if i in vowels:
            counter +=1
    print("The word \"%s\" have %s vowels." %(word,counter))

# vowelsCounter("esternocleidomastoideo")

#Exercise 4/5---------------------------------

def caseChanger(word, case):
    if case.upper() == "U":
        resultWord = word.upper()
    elif case.upper() == "L":
        resultWord = word.lower()
    else:
        print("Error.")
    print("Result: ",resultWord)

# caseChanger("OAkslLEasEE", "U")


