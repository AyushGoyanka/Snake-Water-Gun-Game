import random
import pygame

'''
1 for snake
-1 for Water
0 for Gun
'''


def gameplay():
    print("Hey,Welcome to Snake-Water-Gun-Game!!")
    computer=random.choice([-1,0,1])
    yourchoice=input("Enter Your Choice:\n1.s for Snake\n2.w for Water\n3.g for Gun\n").lower()
    yourdict={"s":1,"w":-1,"g":0}

    if yourchoice not in yourdict:
       print("Invalid Input!!")
       return

    revdict={1:"Snake",-1:"Water",0:"Gun"}
    you=yourdict[yourchoice]


    print(f"\nYou Chose {revdict[you]}\ncomputer chose {revdict[computer]}\n")

    if(computer==you):
       print("Game Draw!!")
    else:
      if(computer==1 and you==-1):
         print("You Loose!!")
      elif(computer==1 and you==0):
         print("You Win!!")
      elif(computer==-1 and you==1):
         print("You win!!")
      elif(computer==-1 and you==0):
         print("You Loose!!")
      elif(computer==0 and you==1):
         print("You Loose!!")
      elif(computer==0 and you==-1):
         print("You Win!!")
      else:
         print("Sorry,Something went Wrong!!")


while True:
    gameplay()
    n=input("\nDo You wants to play Game again(y/n):\n").lower()
    if(n!="y"):
        print("Thanks For Playing!!,Goodbye!!")
        break

