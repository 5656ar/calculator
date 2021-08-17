import one
import two
import three
import four


PLUS = 1
MINUS = 2
MULTIPLY = 3
DIVIDE = 4
QUIT = 5

def main():
    choice = 0
    while choice != QUIT :
        display_menu()
        choice = int(input("Enter you choice: "))
        print('')
        
        if choice == PLUS:
            num1 = int(input('Enter the first number: ')) 
            num2 = int(input('Enter the second number: ')) 
            print('The summation is' , one.add(num1,num2))
            print('')
    
        
        elif choice == MINUS:
            num1 = int(input('Enter the first number: ')) 
            num2 = int(input('Enter the second number: ')) 
            print('The summation is' , two.subtract(num1,num2))
            print('')
    
        
        elif choice == MULTIPLY:
            num1 = int(input('Enter the first number: ')) 
            num2 = int(input('Enter the second number: ')) 
            print('The summation is' , three.multiply(num1,num2))
            print('')
    
        
        elif choice == DIVIDE:
            num1 = int(input('Enter the first number: ')) 
            num2 = int(input('Enter the second number: ')) 
            print('The summation is' , four.divide(num1,num2))
            print('')
    
        
        elif choice == QUIT:
            print('Exiting the program...')
            print('')
    
            
        else:
            print('Error: invalid selection.')
            print('')
    
        
    
    
def display_menu():
    print('         MENU')
    print('1) PLUS')
    print('2) MINUS')
    print('3) MULTIPLY')
    print('4) DIVIDE')
    print('5) Quit')
    print('')

main()