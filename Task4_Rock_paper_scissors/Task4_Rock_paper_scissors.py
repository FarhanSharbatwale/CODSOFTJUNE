import random
import string

com_option = ['Rock' , 'Paper', 'Scissor']

while True:
    print("-----Rock, paper, scissor-----")
    print("1. Play a round\n2. Exit")
    choice = int(input("Enter a choice : "))
    
    if choice == 1:
        print("\nSelect option :\n1. Rock\n2. Paper\n3. Scissor")
        option = int(input("Enter option no : "))
        comp_choice = random.choice(com_option) 
        if option == 1:
            print(f"Computer : {comp_choice} , User : Rock")
            if comp_choice == 'Paper':               
                print("You Lost")
            elif comp_choice == 'Scissor':
                print("You Won")
            else:
                print("It's a tie")

        elif option == 2:
            print(f"Computer : {comp_choice} , User : Paper")
            if comp_choice == 'Rock':
                print("You Won")
            elif comp_choice == 'Scissor':
                print("You Lost")
            else:
                print("It's a tie")

        elif option == 3:
            print(f"Computer : {comp_choice} , User : Scissor")
            if comp_choice == 'Rock':
                print("You Lost")
            elif comp_choice == 'Paper':
                
                print("You Won")
            else:
                print("It's a tie")
        
        else:
            print("Enter a valid choice...")
        print()

    elif choice == 2:
        print("\nGame Exited...\n")
        break
    
    else:
        print("Enter a valid choice...")
