import random
import sys

f=open("four letter words.txt","r")

words=[]
for line in f:
    words.append(line.strip())

def chooseWord():
    return random.choice(words)

def getCowsAndBuffalo(guess):
    cows=buffalo=0

    for i in range(0,4):
        if word[i]==guess[i]:
            buffalo+=1
        if guess[i] in word:
            cows+=1
    cows=cows-buffalo
    return [cows,buffalo]

def chkGuess(guess):
    flag=0
    if len(guess)!=4:
        if guess=="I quit":
            print("Word is :",word,"\nYou LOSE...!!")
            gameEnd()
            return 1
        else:
            print("invalid word")
            return 1

def gameEnd():
    response=input("Enter C for continue and X for end game :")
    if response=='C' or response=='c':
        global word
        word=chooseWord()
        return 1
    else:
        exit()

word=chooseWord()
print(word)
while(1):
    guess=input("Enter your word : ")
    x=chkGuess(guess)
    if x==1:
        continue

    lst=getCowsAndBuffalo(guess)
    if lst[1]!=4:
        print("cows :",lst[0],"buffalo :",lst[1])
    else:
        print("Your guess is right\nThe word is",word)
        x=gameEnd()
        if x==1:
            continue
