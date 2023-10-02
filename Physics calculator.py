# Import custom functions from the Physics_calculator_functions file
import Physics_calculator_functions as func

# Function for the credits
def Menu_credits():
    while True:
        print("Physics Calculator Program Credits")
        print("----------------------------")
        print("Author: Nathan Isaac")
        print("Version: Alpha 2.0")
        print("Date: October 2, 2023")
        print("GitHub Repository:")
        print("Testers: Thomas, Dennis, Rico and Lars")
        print("This calculator is based on the Applied Physics course from the Amsterdam Institute of Applied Sciences")
        user_input = input("Press enter to return to the main menu: ")
        match user_input:
            case _: # Go back to the previous menu
                func.clear_screen()
                break 

# Function for the help menu
def Menu_help():
    while True:
        # Display menu options for Help menu
        user_input = input('What do you need help with?\n1. How does this calculator work?\n2. I get an error message, what can I do?\nB to go back\nQ to stop\nInput: ')
        match user_input:
            case 'B'|'b': # Go back to the previous menu
                func.clear_screen()
                break  
            case 'Q'|'q': # Quit function
                func.Quit_program()
            case '1':
                func.clear_screen()
                print('In the input screen, type the number corresponding to the type of calculation you want to perform.')
                print('The options are always displayed above the input square.')
            case '2':
                func.clear_screen()
                print('If you get an error, there will be a message displayed explaining what went wrong.')
                print('Possible error messages:')
                print('- Invalid input: The input you provided was not recognized by the calculator.')
                print('- Value error: You entered an unexpected value as input. Please double-check the required input format.')
                print('- Division by zero: This means that a division by zero occurred during the calculation. Check your input values.')
                print('- Infinity error: This means that the numbers in you calculation became too large and reached infinity. Check your input values.')
            case _:
                func.Invalid_input_NotRecognized()

# Function to handle the menu for Newton's equations
def Menu_Newton_Equations():
    while True:
        # Display menu options for Newton's equations
        user_input = input('What law of Newton would you like to calculate?\n1. newton\'s first law\n2. newton\'s second law\n3. newton\'s third law\nB to go back\nQ to stop\nInput: ')
        match user_input:
            case 'B'|'b': # Go back to the previous menu
                func.clear_screen()
                break  
            case 'Q'|'q': # Quit function
                func.Quit_program()
            case '1':
                func.Newtons_first_law()
            case '2':
                func.Newtons_second_law()
            case '3':
                func.Newtons_third_law()            
            case _:
                func.Invalid_input_NotRecognized()

# Function to handle the menu for Newtonian movement equations
def Menu_Newton_movement_equations():
    func.Newtonian_movement()

# Function to handle the menu for Force equations
def Menu_Force_equations():
    while True:
        # Display menu options for Force equations
        user_input = input('What force would you like to calculate?\n1. Gravity\n2. Air resistance\n3. Static friction\n4. Dynamic friction\n5. Spring force\n6. Centripetal force\nB to go back\nQ to stop\nInput: ')
        match user_input:
            case 'B'|'b': # Go back to the previous menu
                func.clear_screen()
                break  
            case 'Q'|'q': # Quit function
                func.Quit_program()
            case '1':
                func.gravity()
            case '2':
                func.air_resistance()
            case '3':
                func.friction_static()
            case '4':
                func.friction_dynamic()
            case '5':
                func.spring_force() 
            case '6':
                func.centripedal_force()
            case _:
                func.Invalid_input_NotRecognized()        
            
# Main menu function for the entire program
def Main_menu():
    func.clear_screen()
    while True:
        # Explanation of how the program works
        explanation = "Input the number corresponding to the calculation you want to perform"
        print(explanation)
        
        # Menu options for the first question
        library = "Options:\n1. Newton equations\n2. Newtonian movement equations\n3. Force\nH for the help menu\nC for credits\nQ to quit"
        print(library)
        
        # Prompt the user to choose an option
        start_question = input('What would you like to calculate?: ')
        match start_question:

            # Quit the program
            case 'Q'|'q':
                func.Quit_program()
            
            # Help menu
            case 'H'|'h':
                func.clear_screen()
                Menu_help()
            
            # Newton equations
            case '1':
                func.clear_screen()
                Menu_Newton_Equations()
                        
            # Newtonian movement equations
            case '2':
                func.clear_screen()
                Menu_Newton_movement_equations()
                
            # Force equations
            case '3':
                func.clear_screen()
                Menu_Force_equations()
              
            # Credits    
            case 'c'|'C':
                func.clear_screen()
                Menu_credits()    
                
            # Invalid input
            case _:
                func.Invalid_input_NotRecognized()

Main_menu() # Start the program
