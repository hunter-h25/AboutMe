def wordFrequency(text):
    #Simplifies the text to a readable form
    newText = text.lower()
    rmList = [".","!","?",",","(",")",";",":","'"]
    for i in range(0,len(rmList)):
        newText = newText.replace(rmList[i],"")

    display = ""
    ocrList = []

    #Makes a list of all the words in the text
    wordList = newText.split()


    #Checks if word has ocurred before. If it has it will skip it and add an occurence, if it hasn't then it will add it to the final display
    while True:
        for i in range(0,len(wordList)):
            if not wordList[i] in ocrList:
                ocr = wordList.count(wordList[i])
                display += f"{wordList[i]}:\t{ocr}\n"
                ocrList.append(wordList[i])
        break        
    return display

paragraph = input("What do you want to analyze:\n")
output = wordFrequency(paragraph)
print(output)
