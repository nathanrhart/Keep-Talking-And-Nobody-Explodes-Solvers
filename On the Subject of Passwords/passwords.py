print("Keep Talking And Nobody Explodes - Kronorox Solvers")
print("On the Subject of Passwords")
print("Version 1.01")
print(" ")
print("Remember to rack through the first six(using the arrows), then move to the second set of letters, and so on")
#Loading the file, opening it, then adding it to the list, then closing
def loadwords():
  words = open("passwordslist.txt", "r")#open the file, read only access
  wordlist = []#our shiny new empty list to fill
  for line in words: #only letters 1-5 to stop "\n" being added
    wordlist.append(str(line[0:5]))
  words.close()#close the file, we weren't born in a barn!
  return(wordlist)

def lettercheck(letters):#This checks the input to make sure it wasn't put in wrong
  if len(letters) != 6:#the input has to be six long
    return False
  for i in letters.lower():#the input has to be a letter(we lower case it briefly)
    if i not in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
      return False
  else: return True
#with our checker ready, lets input the words!

#Inputting the letters available
def letter_one(columns):#making the first list of letters
  letterlist_one = input("Input first letters: ")
  if letterlist_one == "admin":#some debugging to skip to the solver
    return solver(["sccccc","tccccc","uccccc","dccccc","yccccc"],loadwords())
  if lettercheck(letterlist_one) == True: #if the format is correct
    print("Okay!")#if they get it right, tell them
    columns.append(letterlist_one.upper())#add it to the list of columns
    letter_two(columns)#move to the next set of letters
  else:
    print("You made a mistake!")#they made a fucky wucky
    letter_one(columns)#do it again, but right this time
def letter_two(columns):
  letterlist_two = input("Input second letters:")
  if lettercheck(letterlist_two) == True:
    print("Okay!")
    columns.append(letterlist_two.upper())
    letter_three(columns)
  else:
    print("You made a mistake!")
    letter_two(columns)
def letter_three(columns): 
  letterlist_three = input("Input third letters: ")
  if lettercheck(letterlist_three) == True:
    print("Okay!")
    columns.append(letterlist_three.upper())
    letter_four(columns)
  else:
    print("You made a mistake!")
    letter_three(columns)
def letter_four(columns):
  letterlist_four = input("Input fourth letters:")
  if lettercheck(letterlist_four) == True:
    print("Okay!")
    columns.append(letterlist_four.upper())
    letter_five(columns)
  else:
    print("You made a mistake!")
    letter_four(columns)
def letter_five(columns):
  letterlist_five = input("Input fifth letters: ")
  if lettercheck(letterlist_five) == True:
    print("Okay!")
    columns.append(letterlist_five.upper())
    print("Solving...")
    solver(columns,loadwords())
  else:
    print("You made a mistake!")
    letter_five(columns)
#okay good you've inputted your letters and they're correct! time to check em!

def solver(columns,wordlist):#import the inputted words, and the list of words
  newwordlist = [] #make a new wordlist we'll use to alter(to stop list editing failures, lazy af)
  for word in range(0, len(wordlist) ):#for every word in the word list
    newwordlist.append(wordlist[word])#add that word to our new word list, this is a bad way of doing this

  #print the table of the letters youve added
  for column in range (0, len(columns)):#for every column in the list of inputted columns
    for row in range (0,len(columns[column])):#and for every row in the list of inputted columns
      print(str(columns[column][row] + " "), end="")#print each letter, then add a space, don't add a new line
    print("")#print the new line once the row is printed

  #time to check the inputs!
  for word in range(0, len(wordlist)):#for every word in the wordlist
    for letter in range(0, len(wordlist[word]) ):#and for every letter in every word in the wordlist
      if wordlist[word][letter] not in columns[letter]:#check if the letter is in that column
        try:#just in case the word has already been taken out of our list
          newwordlist.remove(wordlist[word])#remove the word it can't be from our new list
        except:"Word already removed!"
  try:
    print("The answer is: " + str(newwordlist[0].upper()) )#print our new word list!
  except: print("I can't find the word, are you sure you inputted right?!")

def play():#play script to launch the commands
  columns=[]
  letter_one([])
play()
