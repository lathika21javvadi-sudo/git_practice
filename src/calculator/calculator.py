def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def main(): 
    print("Simple Calculator") 
    print("1. Add") 
    print("2. Subtract") 
    print("3. Multiply") 
    
    choice = input("Choose an operation (1/2/3): ") 
    
    a = float(input("Enter first number: ")) 
    b = float(input("Enter second number: ")) 
    if choice == "1": print("Result:", add(a, b)) 
    elif choice == "2": print("Result:", sub(a, b)) 
    elif choice == "3": print("Result:", mul(a, b)) 
    else: print("Invalid choice") 

if __name__ == "__main__": 
    main()