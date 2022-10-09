print("let's play a game")
print("if you don't know what to do, type : help")
money = 0
date_count = 0
win = False
while win == False:
      answer = input("what you wanna do : ")
      if answer == 'help':
            print('Type')
            print('pet -> pet a dog')
            print('feed -> feed a dog($1)')
            print('work -> get $4')
            print('sugar -> hangout with some cute girl($10)')
            print('ask for relationship -> if she OK, you win ; need $20 with 3 hangouts')
      if answer == 'pet':
            print("your dog love you even you're a loser")
      if answer == 'feed' and money >= 1:
            print("your dog eat it so lovely")
            money = money - 1
            print("you have $ " + str(money) + " left")
      if answer == 'feed' and money < 1:
            print("you don't have enought money")
            print("you have $ " + str(money) + " left")
      if answer == 'work':
            money = money + 4
            print("you have $ " + str(money) + " left")
      if answer == 'sugar' and money >= 3:
            print("she kindna like you")
            print("you have $ " + str(money) + " left")
            money = money - 3
            date_count = date_count + 1
      if answer == 'sugar' and money <= 3:
            print("you're too poor and ugly to hangout with a girl")
            print("you have $ " + str(money) + " left, go to work")
      if answer == 'ask for relationship' and money >= 20 and date_count >= 3:
            print("you're able to fuck her for free")
            print('you win')
            win = True
      if answer == 'ask for relationship' and money <= 20 and date_count <= 3:
            print('She said "No! you too poor and too ugly to have free sex"')
      if answer == 'ask for relationship' and money <= 20 and date_count >= 3:
            print('She said "No! you too poor to have free sex"')

      if win == True:
            break

## Nawakoon


