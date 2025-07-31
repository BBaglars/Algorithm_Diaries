print("--- Single Or Double ---")

def SingleOrDoubleController(number):
    if number % 2 == 0:
        print("Your number is double!")
    else:
        print("Your number is single!") 
    
number = int (input("Please enter the number: "))

SingleOrDoubleController(number)

