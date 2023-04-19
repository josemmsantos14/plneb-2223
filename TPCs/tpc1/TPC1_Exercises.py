import unidecode 

#Exercise 1--------------------------------
def cap_name():
    flag = 0
    while(flag == 0):
        ans = input("What is your name: ")

        if ans.isalpha():
            print(ans.upper(),"\n")
            flag = 1
        else:
            print("Insert a valid name.")

# cap_name()

#Exercise 2---------------------------------

def print_even_numbers():
    list=[]
    even = []
    flag = 0
    while(True):
        number = input("Enter a number or [Enter] to exit: ")
        if number.isnumeric():
            list.append(int(number))
        elif not number and len(list)>0:
            break
        elif not number and len(list)==0:
            print("Input is empty.\n")
            return
        else:
            print("Introduce a valid number.")

    if (all([isinstance(item, int) for item in list])):
        for item in list:
            if item % 2 == 0:
                even.append(item)
            else:
                continue
        if len(even) == 0:
            print("The list dont have even numbers.\n")
        else:
            print("Even numbers: ",even,"\n")
    else:
        print("Not valid input.\n")
    

# print_even_numbers()

#Exercise 3---------------------------------
def print_lines_reverse(fileName):
    print(fileName)
    file = open(fileName, "r")
    lines = file.readlines()
    lines.reverse()
    for line in lines:
        line1 = line.replace("\n","") 
        print(line1)

# print_lines_reverse("exercise3.txt")

#Exercise 4---------------------------------

def more_occurrences(fileName):
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
    for item in finalWords[:10]:
        print("\"", item[0],"\": ",item[1])

# more_occurrences("exercise4.txt")

#Exercise 5---------------------------------

def clean_text():
    text = input("Text: ")
    textLow = text.lower()
    textLow = unidecode.unidecode(textLow)
    print(textLow)
    punctuation = [",",".",";","?","!","-",":",")","\""]
    formated = ""
    for i in range(len(textLow)):
        if textLow[i] in punctuation:
            if i == len(textLow)-1:
                formated = formated + textLow[i]
            else:
                if textLow[i-1] != " " and textLow[i+1] != " ":
                    formated = formated + " " + textLow[i]+ " "
                elif textLow[i-1] != " " and textLow[i+1] == " ":
                    formated = formated + " " + textLow[i]
                else:
                    formated = formated + textLow[i] + " "
        else:
            formated = formated + textLow[i]

    print("formated: ",formated)

# clean_text()

#FUNCTION EXERCISES---------------------------------------------------------
#Exercise 1---------------------------------

def reverse_str():
    word = input("Word: ")
    word = word[::-1]
    print(word)

# reverse_str()

#Exercise 2---------------------------------

def letter_counter():
    word = input("Word: ")
    letter = input("Letter: ")
    counter = word.count(letter.upper()) + word.count(letter.lower())
    print("The word \"%s\" have %s letters \"%s\"." % (word, counter, letter))

# letter_counter()

#Exercise 3---------------------------------

def vowels_counter():
    word = input("Word: ")
    vowels="aeiou"
    counter = 0
    for i in word:
        if i in vowels:
            counter +=1
    print("The word \"%s\" have %s vowels." %(word,counter))

# vowels_counter()

#Exercise 4/5---------------------------------

def case_changer():
    word = input("Word: ")
    case = input("U or L: ")
    if case.upper() == "U":
        resultWord = word.upper()
    elif case.upper() == "L":
        resultWord = word.lower()
    else:
        print("Error.")
    print("Result: ",resultWord)

# case_changer()


