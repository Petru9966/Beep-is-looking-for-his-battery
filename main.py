#Beep asks for his battery
print("Have you seen my spare battery?")
answer=input()
if (answer=="yes"):
  print("Where should I look:")
  answer=input()
  if (answer=="in the bedroom"):
    print("Where in the bedroom should I look?")
    answer=input()
    if ("answer==under the bed"):
      print("I found some trash but not my battery!")
    else:
      print("I do not know wher to find my battery!")
  if (answer=="in the bathroom"):
    print("Where in the bathroom should I look?")
    answer=input()
    if (answer=="in the bathtub"):
      print("I found a condom but not my battery!")
    else:
      print("I found some wet surfaces but not my battery!")
  if ("answer==in the lab:"):
    print("Where in the lab should I look?")
    answer=input()
    if (answer=="on the table"):
      print("Yes! I found my battery!")
    else:
      print("Found some tools but not my battery!")
            
else:
  print("I will look for the battery without your help, human!")

