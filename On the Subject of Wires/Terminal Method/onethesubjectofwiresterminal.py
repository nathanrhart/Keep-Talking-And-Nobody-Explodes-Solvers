print("Keep Talking And Nobody Explodes - Kronorox Solvers")
print("On the Subject of Wires (Terminal Method)")
print("Version 1.0")
print(" ")
#Always start by asking the serial number
def makethedatabase():
  wiredb = []
  wirenum = 1
  serialnumber = input("Is the last digit of the serial number odd? (y/n): ")
  if serialnumber.lower() == "y" or "y" in serialnumber.lower():
    wiredb.append("y")
  elif serialnumber.lower() == "n" or "n" in serialnumber.lower():
    wiredb.append("n")
  else:
    print("Incorrect input!")
    makethedatabase()
  print("Type the colours of the wire, or press ENTER if you've finished!")
  while len(wiredb) < 7:
    addwires = input("What is wire number " + str(wirenum) + ": ")
    answer = ""
    if "r" in addwires and "e" in addwires and "d" in addwires:
      answer = "red"
      wiredb.append(answer)
      print("Wire " + str(wirenum) + " is " + answer + "!")
      wirenum += 1
    elif "b" in addwires and "l" in addwires and "u" in addwires and "e" in addwires:
      answer = "blue"
      wiredb.append(answer)
      print("Wire " + str(wirenum) + " is " + answer + "!")
      wirenum += 1
    elif "w" in addwires and "h" in addwires and "i" in addwires and "t" in addwires and "e" in addwires:
      answer = "white"
      wiredb.append(answer)
      print("Wire " + str(wirenum) + " is " + answer + "!")
      wirenum += 1
    elif "b" in addwires and "l" in addwires and "a" in addwires and "c" in addwires and "k" in addwires:
      answer = "black"
      wiredb.append(answer)
      print("Wire " + str(wirenum) + " is " + answer + "!")
      wirenum += 1
    elif "y" in addwires and "e" in addwires and "l" in addwires and "o" in addwires and "w" in addwires:
      answer = "yellow"
      wiredb.append(answer)
      print("Wire " + str(wirenum) + " is " + answer + "!")
      wirenum += 1
    elif addwires == "" and len(wiredb) > 3:
      return decidepath(wiredb)
    else:
      print("Incorrect input!")
  decidepath(wiredb)
  return

def decidepath(wiredb):
  print(wiredb)
  if len(wiredb) == 4: #three wires PLUS the serial number
    print("you have three wires, " + str(wiredb[1]) + ", " + str(wiredb[2]) + ", and " + str(wiredb[3]) + ".")
    return threewires(wiredb)
  elif len(wiredb) == 5:
    print("you have four wires, " + str(wiredb[1]) + ", " + str(wiredb[2]) + ", " + str(wiredb[3]) + ", and " + str(wiredb[4]) + ".")
    return fourwires(wiredb)
  elif len(wiredb) == 6:
    print("you have five wires, " + str(wiredb[1]) + ", " + str(wiredb[2]) + ", " + str(wiredb[3]) + ", " + str(wiredb[4]) + ", and " + str(wiredb[5]) + ".")
    return fivewires(wiredb)
  elif len(wiredb) == 7:
    print("you have six wires, " + str(wiredb[1]) + ", " + str(wiredb[2]) + ", " + str(wiredb[3]) + ", " + str(wiredb[4]) + ", " + str(wiredb[5]) + ", and " + str(wiredb[6]) + ".")
    return sixwires(wiredb)
  else:
    print("Your database was")
    return makethedatabase()

def threewires(wiredb):
  if "red" in wiredb:
    print("cut the second wire")
    return
  elif wiredb[3] == "white":
    print("cut the last wire")
    return
  elif wiredb.count("blue") > 1:
    if wiredb[3] == "blue":
      print("cut the last wire")
    else:
      print("cut the second wire")
    return
  else:
    print("cut the last wire")
    return

def fourwires(wiredb):
  if wiredb.count("red") > 1 and wiredb[0] == "y":
    for wire in range(len(wiredb),1,-1):
      if wiredb[wire] == "red":
        print("cut the " + numbertowords[wire] + " wire")
        return
  elif wiredb[4] == "yellow" and wiredb.count("red") == 0:
    print("cut the first wire")
    return
  elif wiredb.count("blue") == 1:
    print("cut the first wire")
    return
  elif wiredb.count("yellow") > 1:
    print("cut the last wire")
    return
  else:
    print("cut the second wire")
    return

def fivewires(wiredb):
  if wiredb[5] == "black" and wiredb[0] == "y":
    print("cut the fourth wire")
    return
  elif wiredb.count("red") == 1 and wiredb.count("yellow") > 1:
    print("cut the first wire")
    return
  elif wiredb.count("black") == 0:
    print("cut the second wire")
    return
  else:
    print("cut the first wire")

def sixwires(wiredb):
  if wiredb.count("yellow") == 0 and wiredb[0] == "y":
    print("cut the third wire")
    return
  elif wiredb.count("yellow") == 1 and wiredb.count("white") > 1:
    print("cut the fourth wire")
    return
  elif wiredb.count("red") == 0:
    print("cut the last wire")
    return
  else:
    print("cut the fourth wire")
    return
  

#function for turning the number in the wiredatabase into a word
def numbertowords(num):
  if num == 1:
    return("first")
  if num == 2:
    return("second")
  if num == 3:
    return("third")
  if num == 4:
    return("fourth")
  if num == 5:
    return("fifth")
  if num == 6:
    return("last")
  
  

makethedatabase()


