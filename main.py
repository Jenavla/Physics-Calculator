# Import custom functions from the Physics_calculator_functions file
import Physics_calculator_functions as func
import logging

# Function for the credits
def menu_credits():
    while True:
        logging.info("menu_credits() was called")
        print("Physics Calculator Program Credits")
        print("----------------------------")
        print("Author: Nathan Isaac")
        print("version: Alpha 2.0")
        print("Date: October 2, 2023")
        print("GitHub Repository: https://github.com/Jenavla/Physics-Calculator/tree/main")
        print("Testers: Thomas, Dennis, Rico and Lars")
        print("This calculator is based on the Applied Physics course from the Amsterdam Institute of Applied Sciences")
        user_input = func.log_user_input("Press enter to return to the main menu: ")
        match user_input:
            case _: # Go back to the previous menu
                func.basicfunctions.clear_screen()
                break 

# Function for the help menu
def menu_help():
    while True:
        logging.info("menu_help() was called")
        # Display menu options for Help menu
        user_input = func.log_user_input('What do you need help with?\n1. How does this calculator work?\n2. I get an error message, what can I do?\nB to go back\nQ to stop\nInput: ')
        match user_input:
            case 'B'|'b': # Go back to the previous menu
                func.basicfunctions.clear_screen()
                break  
            case 'Q'|'q': # quit function
                func.basicfunctions.quit_program()
            case '1':
                func.basicfunctions.clear_screen()
                print('In the main menu, you\'ll see a list of options such as Newton equations, Newtonian movement equations, etc.')
                print('To select an option, type the corresponding number or letter and press Enter.')
                print('For example, if you want to work on Newton equations, you can type \'1\' and press Enter.')
                print('Depending on your choice, you may enter submenus specific to the selected category.')
                print('For example, if you chose Newton equations, you\'ll be presented with options like Newton\'s first law, Newton\'s second law, and so on.')
                print('After selecting a specific calculation, you\'ll be prompted to input the necessary values. Follow the prompts and enter the required data.')
                print('Once you\'ve provided the required inputs, the program will calculate the result and display it on the screen in a clear and concise format.')    
                print('At any point, you can navigate back to the previous menu by typing \'B\'. This allows you to change your calculation choice or return to the main menu.')
                print('If you want to exit the program, you can type \'Q\' in the main menu or in most submenus.')
            case '2':
                func.basicfunctions.clear_screen()
                print('If you get an error, there will be a message displayed explaining what went wrong.')
                print('Possible error messages:')
                print('- invalid input: The input you provided was not recognized by the calculator.')
                print('- value error: You entered an unexpected value as input. Please double-check the required input format.')
                print('- Division by zero: This means that a division by zero occurred during the calculation. Check your input values.')
                print('- Infinity error: This means that the numbers in you calculation became too large and reached infinity. Check your input values.')
                print('- Unexpected error: This means you encountered an error the program doesnt recognize. Please contact the creator if this happens.')
                print('- Logarithm error: You got a zero or a negative number in a logarithm. Check your input values')
                print('- Root error: You got a zero or negative number in a root. Check your input values')
            case _:
                func.errorhandling.invalid_input_notrecognized()

# Function to handle the menu for newton's equations
def menu_newton_equations():
    while True:
        logging.info("menu_newton_equations() was called")
        # Display menu options for newton's equations
        user_input = func.log_user_input('What law of newton would you like to calculate?\n1. newton\'s first law\n2. newton\'s second law\n3. newton\'s third law\nB to go back\nQ to stop\nInput: ')
        match user_input:
            case 'B'|'b': # Go back to the previous menu
                func.basicfunctions.clear_screen()
                break  
            case 'Q'|'q': # quit function
                func.basicfunctions.quit_program()
            case '1':
                func.newtons_laws.newtons_first_law()
            case '2':
                func.newtons_laws.newtons_second_law()
            case '3':
                func.newtons_laws.newtons_third_law()            
            case _:
                func.errorhandling.invalid_input_notrecognized()

# Function to handle the menu for Force equations
def menu_force_equations():
    while True:
        logging.info("menu_force_equations() was called")
        # Display menu options for Force equations
        user_input = func.log_user_input('What force would you like to calculate?\n1. Gravity\n2. Air resistance\n3. Static friction\n4. Dynamic friction\n5. Spring force\n6. Centripetal force\nB to go back\nQ to stop\nInput: ')
        match user_input:
            case 'B'|'b': # Go back to the previous menu
                func.basicfunctions.clear_screen()
                break  
            case 'Q'|'q': # quit function
                func.basicfunctions.quit_program()
            case '1':
                func.force.gravity()
            case '2':
                func.force.air_resistance()
            case '3':
                func.force.friction_static()
            case '4':
                func.force.friction_dynamic()
            case '5':
                func.force.spring_force() 
            case '6':
                func.force.centripedal_force()
            case _:
                func.errorhandling.invalid_input_notrecognized()        

# Function to handle the menu for energy equations        
def menu_energy_equations():
        while True:
            logging.info("menu_energy_equations() was called")
            # Display menu options for energy equations
            user_input = func.log_user_input('What energy would you like to calculate?\n1. Gravitational potential energy\n2. Kinetic energy\n3. Kinetic rotation energy\nB to go back\nQ to stop\nInput: ')
            match user_input:
                case 'B'|'b': # Go back to the previous menu
                    func.basicfunctions.clear_screen()
                    break  
                case 'Q'|'q': # quit function
                    func.basicfunctions.quit_program()
                case '1':
                    func.energy.gravitational_potential_energy()
                case '2':
                    func.energy.kinetic_energy()
                case '3':
                    func.energy.kinetic_energy_rotation()
                case _:
                    func.errorhandling.invalid_input_notrecognized()        
                
# Function to handle the menu for thermodynamica
def menu_thermodynamic_equations():
        while True:
            logging.info("menu_thermodynamic_equations() was called")
            # Display menu options for thermodynamica
            user_input = func.log_user_input('What would you like to calculate?\n1. 1D heat expansion\n2. 2D heat expansion\n3. 3D heat expansion\n4. Isobaric work\n5. Isotherm work\n6. First law\nB to go back\nQ to stop\nInput: ')
            match user_input:
                case 'B'|'b': # Go back to the previous menu
                    func.basicfunctions.clear_screen()
                    break  
                case 'Q'|'q': # quit function
                    func.basicfunctions.quit_program()
                case '1':
                    func.thermodynamics.length_expansion()
                case '2':
                    func.thermodynamics.area_expansion()
                case '3':
                    func.thermodynamics.volume_expansion()
                case '4':
                    func.thermodynamics.isobaric_heat_work()
                case '5':
                    func.thermodynamics.isotherm_heat_work()
                case '6':
                    func.thermodynamics.thermo_first_law()
                case _:
                    func.errorhandling.invalid_input_notrecognized()        
                           
# Main menu function for the entire program
def main_menu():
    func.basicfunctions.clear_screen()
    while True:
        logging.info("main_menu() was called")
        # Explanation of how the program works
        explanation = "Input the number corresponding to the calculation you want to perform"
        print(explanation)
        
        # Menu options for the first question
        library = "Options:\n1. newton equations\n2. newtonian movement equations\n3. Force\n4. Energy\n5. Momentum\n6. Impulse\n7. Thermodynamics\nH for the help menu\nC for credits\nQ to quit"
        print(library)
        
        # Prompt the user to choose an option
        start_question = func.log_user_input('What would you like to calculate?: ')
        match start_question:

            # quit the program
            case 'Q'|'q':
                func.basicfunctions.quit_program()
            
            # Help menu
            case 'H'|'h':
                func.basicfunctions.clear_screen()
                menu_help()
            
            # newton equations
            case '1':
                func.basicfunctions.clear_screen()
                menu_newton_equations()
                        
            # newtonian movement equations
            case '2':
                func.basicfunctions.clear_screen()
                func.movement.newtonian_movement()
                
            # Force equations
            case '3':
                func.basicfunctions.clear_screen()
                menu_force_equations()
                
            # Energy equations
            case '4':
                func.basicfunctions.clear_screen()
                menu_energy_equations()
            
            # Momentum equations
            case '5':
                func.basicfunctions.clear_screen()
                func.momentum_impulse.momentum()
                
            # Impulse equations
            case '6':
                func.basicfunctions.clear_screen()
                func.momentum_impulse.impulse()
              
            # Thermodynamic equations
            case '7':
                func.basicfunctions.clear_screen()
                menu_thermodynamic_equations()
            
            # Credits    
            case 'c'|'C':
                func.basicfunctions.clear_screen()
                menu_credits()    
                
            # invalid input
            case _:
                func.errorhandling.invalid_input_notrecognized()

# Start the program by calling the main menu function
if __name__ == "__main__":
    logging.info('Physics Calculator Program Started')
    main_menu()

