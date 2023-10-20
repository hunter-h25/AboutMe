import random

print("Hangman")
print("--------")
print()

winCounter = 0
loseCounter = 5
gList = []
index = 0

#List of words that can be used as an answer and how the computer choses it
list = ["winner","loser","penelope","shark","winter","obscure","lopside","jackfrost","places"]
word = random.choice(list)

#Determines the length of the word and displays it to the player
char = len(word)
print(len(word), "Letters")
print()
underscores = "_" * char

#In-game loop until the player either wins or loses
while True:
  index = 0
  print(underscores,"                   Lives:",loseCounter)
  print()
  guess = input("Letter (lowercase): ")

  #Checks if the user had already guessed that letter and adds it to a list of other guesses   
  if guess in gList:
     print("You Have Already Guessed That!")
     continue
  gList.append(guess)

  #Checks how many times the player's guess occurs in the word
  ocr = word.count(guess)

  #If the guess occurs more than once then it will repeat the procces however many times it occurs
  if ocr > 1:
    for i in range(1,ocr+1):

      #This is how the computer finds where the guess is in the word
      index = word.find(guess,index+1)
      print()
      print("The letter,",guess,"is present in the word at letter number: ", index+1)  
      print()

      #Gets rid of the underscore that takes the place of the correct letter and removes it and replaces it with the letter
      underscores = underscores[:index] + underscores[index + 1: ]
      underscores = underscores[:index] + guess + underscores[index:]
      winCounter += 1

      if winCounter == char:
        print("You Got It!")
        break

  #If the player's guess only occurs once then the computer will only attempt to locate the first occurance of the given letter
  elif ocr == 1:
    index = word.find(guess,index)
    print()
    print("The letter,",guess,"is present in the word at letter number: ", index+1)  
    print()

    underscores = underscores[:index] + underscores[index + 1: ]
    underscores = underscores[:index] + guess + underscores[index:]
    winCounter += 1

    if winCounter == char:
      print("You Got It!")
      break
  
  #If the guess does not appear in the word then it subtracts from the amount of tries they have left
  else:  
    print('That is not in the word')
    print()
    loseCounter -=1
    if loseCounter == 0:
      print()
      print("You Lost!")
      print("The word was:",word)
      break
print(word)
