count = 1
my_dict = {}
new_dict = {}


#list_jersey = sorted(list_jersey) #Sort the new "list"

while count <= 5:
  jersey_num = int(input("Enter player %d's jersey number:\n" % count)) #User input for jersey number
  rate_num = int(input("Enter player %d's rating:\n" % count)) #User input for rating
  my_dict[jersey_num] = rate_num #Create a dictionary with key = jersey number and value = rating
  list_jersey = list(my_dict.keys()) #Turn dictionary keys into list
  list_jersey = sorted(list_jersey) #Sort the new "list"
  count += 1
  print()#Print empty line


print("ROSTER")
for i in list_jersey:
  print("Jersey number: %d, Rating: %d" % (i, my_dict[i]))
  
while True:
  list_jersey = list(my_dict.keys()) #Turn dictionary keys into list
  list_jersey = sorted(list_jersey) #Sort the new "list"
  print()
  print("MENU") #Print out the menu
  print("a - Add player")
  print("d - Remove player")
  print("u - Update player rating")
  print("r - Output players above a rating")
  print("o - Output roster")
  print("q - Quit") 
  option = input("\nChoose an option:\n")
  if option == "q": #If user enters "q"
    exit()
  elif option == "o": #If user enters "o"
    print()
    print("ROSTER")
    for i in list_jersey:
      print("Jersey number: %d, Rating: %d" % (i, my_dict[i]))
  elif option == "a": #If user enters "a"
    jersey_num2 = int(input("Enter a new player's jersey number:\n"))
    rate_num2 = int(input("Enter the player's rating:"))
    new_dict[jersey_num2] = rate_num2
    my_dict.update(new_dict)
  elif option == "d": #If user enters "d"
    jersey_remove = int(input("Enter a jersey number:\n"))
    my_dict.pop(jersey_remove)
  elif option == "u": #If user enters "u"
    jersey_update = int(input("Enter a jersey number:\n"))
    rate_update = int(input("Enter a new rating for player:\n"))
    my_dict[jersey_update] = rate_update
  elif option == "r": #If user enters "r"
    rate_above = int(input("Enter a rating:\n"))
    print()
    print("ABOVE %d" % rate_above)
    for jersey, rate in sorted(my_dict.items()):
      if rate > rate_above:
        print("Jersey number: %d, Rating: %d" % (jersey, rate))
      if rate <= rate_above:
        continue
