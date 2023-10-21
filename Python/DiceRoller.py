import random

print("Dice Roller!")
print("-------------")

again = ""

while again != "n":
  print()
  diceAmt = int(input("How many dice are you wanting to roll? "))
  print()
  diceSide = int(input("How many sides are on each dice? "))
  total = 0
  print()
  for i in range(1,diceAmt+1):
    diceNum = random.randint(1,diceSide)
    total = total+diceNum
    
  print("Dice Total:",total)
  print()

  again = input("Do you want to roll again?(y/n) ")
