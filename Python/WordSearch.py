import pandas as pd #this was a bad idea. don't used pandas for simple data
import math #I needed to round down to whole numbers
import re #using regex because it makes replacing things a lot easier. it is later used to get rid of all numbers


def importWords():
     listOfWords = [] #holds list of words...duh
     amount = int(input("How many words are you finding: ")) #asking how many words the user wants which isn't ideal but you said I could use any method I want
     for i in range(amount): #not optimized for the user but gets the job done
          word = input(f"Word {i+1} (All Caps): ")
          listOfWords.append(word)
          listOfWords.append(word[::-1]) #appending it backwards, I don't think you actually showed this but I used it in a different project
     return listOfWords

def importBoard(): #Does everything needed before searching
     file = input("Please Input The File Name: ") #Asking for csv file of board
     board = pd.read_csv(file,header=None) #makes pandas read it
     
     #separate each set of lines into their own lists
     #Horizontal
     lines = [] #local var used to contain the lines of given direction
     listOfLetters = [] #this will later be put together to form the lines
     for i in range(len(board)): #every line
          letter = board[i:(i+1)] #grabbing only the letter i need
          listOfLetters.append(letter) #putting it in the list
     for i in range(len(listOfLetters)): #iterating through the letters to put them together
          index = str(listOfLetters[i]).find("\n") #finding where pandas puts certain data that I don't need
          whatToAdd = 4+(math.floor(i/10)) #the numbers after the \n cause problems when more than one digit so I fixed that
          lines.append(str(listOfLetters[i])[index+whatToAdd:]) #append to lines
     horizontalLines = []
     for eachLine in lines:
          horizontalLines.append(eachLine.replace(" ","")) #put it all together
     
     #Vertical
     lines = []
     listOfLetters = []
     for i in range(len(board)):
          letter = board.iloc[:,[i]] #searches by row and col...very useful
          listOfLetters.append(letter)
     for i in range(len(listOfLetters)):
          index = str(listOfLetters[i]).find("\n")
          lines.append(str(listOfLetters[i]).replace("\n","")[9:]) #pandas doesn't add as much data I don't need but it is always 9 characters of it
     numbers = []
     for i in range(len(board)): #I think this was part of testing but I have no clue why I put it here but since my code works it is now part of "history"
          numbers.append(str(i))
     cleanLines = [] #holds lines without numbers
     i = 0 #artificial for i in range
     for cleanLine in lines:
          cleanLines.append(re.sub(r'[0-9]', '', cleanLine)) #remove all numbers from the data because we don't need them
          i += 1
     verticalLines = []
     for eachLine in cleanLines:
          verticalLines.append(eachLine.replace(" ","")) #adding the clean lines

     return [board,horizontalLines,verticalLines]

def searchHorizontally(word,board,display): #display is the placeholder board or final board that will be shown
     index = board.find(word) #find the word
     if index != -1: #if it finds it
          display = display[:index] + word + display[index+len(word):] #from start to where the word is in regular board then but on display put the letter than the rest of the board
     return display #Modified board

def searchVertically(word,board,lineList):
     col = 0 #will track what column it is on
     for eachLine in lineList:
          index = eachLine.find(word) #find it
          if index != -1:#if it finds it
               if index > 0: #if no on edge of the board
                    startingPosition = (col+(index*len(lineList))+1) #Colomn + the amount of character in each row
                    for i in range(len(word)): #for the word
                         board = board[:startingPosition] + word[i] + board[(startingPosition)+1:] #from where the word is on the original to the rest of the board
                         startingPosition += len(lineList)+1
               if index == 0: #if on the edge of the board
                    startingPosition = (col+(index*len(lineList)))
                    for i in range(len(word)):
                         board = board[:startingPosition] + word[i] + board[(startingPosition)+1:]
                         startingPosition += len(lineList)+1
          col += 1
     return board



def search_words_diagonal(word_search, words): #I'm going to be honest I did a whole lot of research around this and eventually got very lost and decide to ask GPT on where to START, I'll do my best to comment this and put it into my own words, after GPT spit out something I ended up having to almost completely re-write it in order for it to work.
    #Determining the dimensions of the board to limit our search and be able to use any size word search
    rows = len(word_search)
    cols = len(word_search[0])

    #creating a list that will hold the lines and placeholders ("-")
    blanked_board = [['-']*cols for _ in range(rows)]  # Initialize a new blanked board with hyphens
    
    #nested function since this is only used here. Used to find if the word can be found and where
    def check_diagonal(start_row, start_col, delta_row, delta_col, word):
        #define where the starting row and column is
        row, col = start_row, start_col
        #go through each character in word
        for char in word:
            #make sure the given values are actually in the board, i was getting an issue where it didn't like the indexes of certain words and adding this helped
            if not (0 <= row < rows and 0 <= col < cols and word_search[row][col] == char):
                return False
            #updating based on direction the word. makes searching both ways MUCH easier
            row = (row + delta_row) % rows
            col = (col + delta_col) % cols
        return True #If the word is there then it returns true
    
    for word in words: #going through each word. I initially has it loop outside of the function like the horizontal and vertical but it wanted to keep overwriting other words
        for i in range(rows): #each position
            for j in range(cols):
                for delta_row, delta_col in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:  #check ALL possible directions. I spent like an hour trying to figure out why it only searched to the left
                    if check_diagonal(i, j, delta_row, delta_col, word): #if word can be found from position
                        row, col = i, j  #starting row and column. makes it a heck of a lot less confusing
                        for char in word: #update the blank board with new word
                            blanked_board[row][col] = char
                            #updating through direction
                            row = (row + delta_row) % rows
                            col = (col + delta_col) % cols

    return blanked_board #list of lines


data = importBoard() #will hold the list of data so that it only runs once
wordSearchBoard=data[0] #the board
wordList = importWords() #list of words

#TODO:  Between these two print statements, you will run all of your searches.\

#parrels strings that has:
finalBoard = "" #the board
displayBoard = "" #placeholders

for eachLine in data[1]: #adding each line to the board using the horizontalLines list from earlier
     finalBoard += f"{eachLine}\n"

#Diagonal
blanked_board = search_words_diagonal(data[1],wordList) #making a list of lines for the placeholder board
for line in blanked_board: #put every line together
     displayBoard += "".join(line)+"\n"

#Horizonital
for eachWord in wordList: #for each word...search for it
     displayBoard = searchHorizontally(eachWord,finalBoard,displayBoard)

#Vertical
for eachWord in wordList: #for each word...search for it
     displayBoard = searchVertically(eachWord,displayBoard,data[2])

#printing final board
print(f'''
      
Answer Board
      
{finalBoard}

Display Board

{displayBoard}


''')

f = open("WordSearchAnswers.txt", "w") #open and write to file
f.write(displayBoard) #write the display board
f.close()