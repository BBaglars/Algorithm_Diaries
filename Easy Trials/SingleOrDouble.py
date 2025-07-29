print("--- Single Or Double --- /n/n/n")

def SingleOrDoubleController(number):
    if number % 2 == 0:
        print("Your number is double!")
    else:
        print("Your number is single!") 

def Controller(number):
    if number < 0:
        print("Number is not be negative")
        return False 
    else:
        return True  
    

number = int (input("Please enter the number: "))

controller = Controller(number)   

if controller == True:
    SingleOrDoubleController(number)
else:
    print("Please enter a integer")
