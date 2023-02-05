

class calculator():

    print("Menu:")
    print("""
    1 - Addition
    2 - Subtraction
    3 - Multiplication
    4 - Division
    0 - Exit
    """)


  

try:
    option = int(input("choice option, 0 to 4: "))
    if 1 <= option <= 4:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter a second number: "))

except:
            
    print("Elige una opcion del 1 al 4")

else:        
    
    
    if option == 1:
        print (num1 + num2)                  
    elif option == 2:
        print (num1 + num2)
    elif option == 3:
        print(num1*num2)
    elif option == 4:
        print(num1//num2)
    elif option == 0:
        print("Adios")
    else:
        print("Vuelve a intentarlo")  
    
