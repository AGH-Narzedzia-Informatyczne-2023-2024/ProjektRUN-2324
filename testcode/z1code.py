print("CAR GAME Version1. commands: help,start,stop,exit.")
print("")

moving=False

while(True):
    command=input(">")

    if command == "help":
        print("start - to start a car")
        print("stop - to stop a car")
        print("quit - to exit our game")
    elif (command=="start" and moving==False):
        print("Car started... Ready to go!")
        moving=True
    elif (command=="start" and moving==True):
        print("The car is already going :D.")
    elif (command=="stop" and moving==True):
        print("The car has stopped!")
        moving=False
    elif (command=="stop" and moving==False):
        print("The car is already stopped :D.")  
    elif(command=="exit"):
        break
    else:
        print("Sorry, i dont understand..")  
        
print("====Thank you for playing our game====")