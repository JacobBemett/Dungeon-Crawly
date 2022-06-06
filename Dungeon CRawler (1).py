import tkinter as tk
import random                   #Importing necessary modules
import time

Stamina = 0
Health = 0
Levels = 5

Number=False
Letter=False
print("Difficulty?")
while Letter==False:
    Difficulty= input("Easy (E), Medium (M), or Hard (H)? ")                                    #Setting the difficulty     
    if Difficulty.lower() == "e" or Difficulty.lower() == "m" or Difficulty.lower() == "h":     #Verifying the input
        Letter=True
print("")
while Number==False:
    Levels= input("How many levels? ")                                    #Setting the levels    
    Number=Levels.isnumeric()

Levels=int(Levels)
if Difficulty == "e":
    Health = Levels * 2
    Stamina = Levels * 2
elif Difficulty == "m":
    Health = Levels + 1
    Stamina = Levels + 2
    if Stamina < 1:                         #Health and Stamina set depending on level
        Stamina = 1
else:
    Health = Levels//2
    Stamina =Levels
    if Health < 1:
        Health = 1
    if Stamina < 1:
        Stamina = 1

MaxHealth=Health
MaxStamina=Stamina

print("")
print ("You will go through",Levels,"levels")
print ("Since you chose",  end = " ")
if Difficulty =="e":
       print ("easy",end = " ")                     #telling the user the result of their inputs
elif Difficulty =="m":
       print ("medium",end = " ")
else:
       print ("hard",end = " ")
print("difficulty, you have:")
print (Health,"health")
print (Stamina, "stamina")
print("")


Settings = ["Cave","Crypt","Castle"]
Situations=[["chest, it is locked", ["Look around for a key",0,random.randint(20,40),["You manage to find the key. Opening the chest, you find an old potion, increasing your health by 1",-1],["You can't find the key, so you give up and move on.",0]],["Try to pick the lock",1,random.randint(30,50),[]],["Break the chest",2,random.randint(10,15),]],
            "Monster","locked door","merchant","trap","guard","riddle","treasure room","fun little rune circle"]

Setting= random.randint(0,len(Settings)-1)
Setting= 0                          #avoiding randomising for prototyping
#print(Settings[Setting])

def ChosenOne():
    global Stamina
    print("You chose to",Situations[Situation][1][0])
    Stamina=Stamina-(Situations[Situation][1][1])
    #OptionOne.destroy()
    #OptionTwo.destroy()
    #OptionThree.destroy()
    #Decision.destroy()
    Window.destroy()
def ChosenTwo():
    global Stamina
    print("You chose to",Situations[Situation][2][0])
    Stamina=Stamina-(Situations[Situation][2][1])
    #OptionOne.destroy()
    #OptionTwo.destroy()
    #OptionThree.destroy()
    Window.destroy()
def ChosenThree():
    global Stamina
    print("You chose to",Situations[Situation][3][0])
    Stamina=Stamina-(Situations[Situation][3][1])
    #OptionOne.destroy()
    #OptionTwo.destroy()
    #OptionThree.destroy()
    Window.destroy()

time.sleep(1)
print ("You come across the", Settings[Setting]+ ". As you go to enter" , end = " " )
CurrentLevel=0
while CurrentLevel < Levels:
    Situation = random.randint(0,len(Situations)-1)
    Situation = 0       #avoiding randomising for prototyping
    print("you see a", end=" ")
    print(Situations[Situation][0])
    
    #print("Here are your choices")
    #print("1. Look around for a key (0 Stamina)")
    #print("2. Try to pick the lock (1 Stamina)")
    #print("3. Break the chest (2 Stamina)")
    #Choice=input("What do you do? (1,2 or 3):")
    Window = tk.Tk()
    #Tester = tk.Label(text="Hello, Tkinter")
    #Tester.pack()
    Decision = tk.Label(text="What do you do?")
    OptionOne = tk.Button(text=(Situations[0][1][0],"("+str(Situations[0][1][1]), "Stamina)"),width=30, height=3,bg="white",fg="black",command=ChosenOne)
    OptionTwo = tk.Button(text=(Situations[0][2][0],"("+str(Situations[0][2][1]), "Stamina)"),width=30, height=3,bg="white",fg="black",command=ChosenTwo)
    OptionThree = tk.Button(text=(Situations[0][3][0],"("+str(Situations[0][3][1]), "Stamina)"),width=30, height=3,bg="white",fg="black",command=ChosenThree)
    Decision.pack()
    OptionOne.pack()
    OptionTwo.pack()
    OptionThree.pack()
    tk.mainloop()
    
    CurrentLevel=CurrentLevel+1
