print("--- Fibonacci ---")

number = int (input("Enter the number:"))
fibonacci = [1,1]

def Controller(number):
    if number < 0:
        print("Number is not be negative")
        return False 
    elif number == 0:
        print("Febonacci = 0")
        return False
    else:
        return True  
    
controller = Controller(number)   

if controller == True:
    for x in range(1,number):
        fibo = fibonacci[x] + fibonacci[x-1]
        if fibo > number:
            break
        fibonacci.append(fibo)

print(fibonacci)