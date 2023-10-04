import sys
import os
import math
import logging

# Start a log or update a log if one is already there
logging.basicConfig(filename='physics_calculator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Function to log user inputs and return them
def log_user_input(prompt):
    user_input = input(prompt)
    logging.info(f'User input: {user_input}')
    return user_input

# Function to log calculation results
def log_result(result):
    logging.info(f'Result: {result}')

# function to clear the terminal
def clear_screen():
    # check the operating system and clear the screen accordingly
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for linux and macOS
        os.system('clear')
        
# function to quit the program
def quit_program():
    """
    This function quits the program and displays a goodbye message.
    """
    logging.info('Physics Calculator Program Ended')
    clear_screen()
    print("goodbye")
    sys.exit()  

# function for handling invalid inputs when a division by zero occurs
def invalid_input_zerodivisionerror():
    """
    This function prints an error message for when a division by zero is made.
    """
    logging.info('!Invalid input ZeroDivisionError')
    clear_screen()
    print("invalid input, you got a division by zero")
    
# function for handling invalid inputs when a non-numerical value is entered
def invalid_input_valueerror():
    """
    This function prints an error message for when a non-numerical value is entered.
    """
    logging.info('!Invalid input ValueError')
    clear_screen()
    print("invalid input, please input a valid numerical value")

# function for handling invalid inputs when a command isn't recognized
def invalid_input_notrecognized():
    """
    This function prints an error message for when a command a user made isn't recognized.
    """
    logging.info('!Invalid input NotRecognized')
    clear_screen()
    print("This program does not recognize that command. Please try again.")

# function for handling when a number becomes infinity
def invalid_input_infinityerror():
    """
    This function prints an error message when a number reaches infinity
    """
    logging.info('!Invalid input InfinityError')
    clear_screen()
    print('The result is infinity. Please check your input values.')

# function for handling an error that isnt expected by the program
def invalid_input_exceptionerror():
    """
    This function prints an error message when an error occured that wasn't expected
    """
    logging.info('!!!Invalid input ExceptionError')
    clear_screen()
    print("an unexpected error occurred")

# function for handling when a logarithm has a number of zero or lower in it
def invalid_input_logarithmerror():
    """
    This function prints an error message when a logarithm contains a number of zero or lower
    """
    logging.info('!Invalid input logarithmerror')
    clear_screen()
    print("you got a logarithm with a number that was zero or lower, which isnt possible")

# function for handling when a root has a number of zero or lower in it
def invalid_input_rooterror():
    """
    This function prints an error message when a root contains a zero or lower
    """
    logging.info('!Invalid input rooterror')
    clear_screen()
    print("you got a root with a number that was zero or lower, which isnt possible")
    
# function for handling multiple plus and minus signs
def compact_signs(number_str):
    # continue looping until no more consecutive plus or minus signs are found
    while True:
        # Replace consecutive double minus signs with a single plus sign
        # Replace combinations of plus and minus signs with a single minus sign
        new_str = number_str.replace("--", "+").replace("+-", "-").replace("-+", "-").replace("++", "+")
        
        # if the modified string is the same as the original string, exit the loop
        if new_str == number_str:
            break
        
        # Update the original string with the modified one for the next iteration
        number_str = new_str

    # after handling consecutive signs, check the count of plus and minus signs
    if number_str.count('+') > 1:
        # if there are more than one plus signs, simplify to a single plus sign
        number_str = '+'
    elif number_str.count('-') > 1:
        # if there are more than one minus signs, simplify to a single minus sign
        number_str = '-'

    # Return the simplified number string
    return number_str

# function for handling calculations related to newton's first law
def newtons_first_law():
    """
    This function handles calculations related to newton's first law.
    it provides options to calculate momentum, mass, and velocity.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("newtons_first_law() was called")
        user_input = log_user_input("What would you like to calculate?\n1. Momentum\n2. Mass\n3. velocity\nb to go back\nQ to stop\ninput: ")  # User input
        
        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            
            case 'Q' | 'q':  # quit program
                quit_program()
            
            case '1':  # calculate the momentum
                clear_screen()
                try:  # Try to convert user input to numbers
                    mass = abs(float(compact_signs(log_user_input("What is your mass (kg)? "))))
                    velocity = float(compact_signs(log_user_input("What is your velocity (m/s)? ")))
                    momentum = mass * velocity
                    
                    log_result(momentum)

                    if math.isinf(momentum):
                        invalid_input_infinityerror()
                    else:
                        print('Your momentum is: ', momentum, 'N')
                       
                except ValueError:  # Handle invalid input
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
                    
            case '2':  # calculate the Mass
                clear_screen()
                try:
                    momentum = float(compact_signs(log_user_input("What is your momentum (N)? ")))
                    velocity = float(compact_signs(log_user_input("What is your velocity (m/s)? ")))
                    
                    if velocity == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    
                    mass = abs(momentum / velocity)  # Mass has to be absolute
                    
                    log_result(mass)
                    
                    if math.isinf(mass):
                        invalid_input_infinityerror()
                    else:
                        print('Your mass is: ', mass, 'kg')
                    
                except ValueError:  # Handle invalid input
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
                    
            case '3':  # calculate velocity
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input("What is your mass (kg)? "))))
                    momentum = float(compact_signs(log_user_input("What is your Momentum (N)? ")))
                    
                    if mass == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    
                    velocity = momentum / mass
                    
                    log_result(velocity)
                    
                    if math.isinf(velocity):
                        invalid_input_infinityerror()
                    else:
                        print('Your velocity is: ', velocity, 'm/s')
                    
                except ValueError:  # Handle invalid input
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
                    
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to newton's Second law
def newtons_second_law():
    """
    This function handles calculations related to newton's Second law.
    it provides options to calculate mass, acceleration, and force.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("newtons_second_law() was called")
        user_input = log_user_input("What do you want to calculate?\n1. Mass\n2. acceleration\n3. force\nb to go back\nQ to stop\ninput: ")  # User input
        
        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break 
            
            case 'Q' | 'q':  # quit program
                quit_program()        
            
            case '1':  # calculate mass
                clear_screen()
                try:  # Try to convert user input to numbers
                    force = float(compact_signs(log_user_input('What is your force (N)? ')))
                    acceleration = float(compact_signs(log_user_input('What is your acceleration (m/s^2)? ')))
                    
                    if acceleration == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    
                    mass = abs(force / acceleration)  # Mass has to be absolute
                    
                    log_result(mass)
                    
                    if math.isinf(mass):
                        invalid_input_infinityerror()
                    else:
                        print('Your mass is', mass, 'kg')
                
                except ValueError:  # Handle invalid input
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            
            case '2':  # calculate acceleration
                clear_screen()
                try:
                    force = float(compact_signs(log_user_input('What is your force (N)? ')))
                    mass = abs(float(compact_signs(log_user_input('What is your mass (kg)? '))))
                    
                    if mass == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    
                    acceleration = force / mass
                    
                    log_result(acceleration)
                    
                    if math.isinf(acceleration):
                        invalid_input_infinityerror()
                    else:
                        print('Your acceleration is', acceleration, 'm/s')
                
                except ValueError:  # Handle invalid input
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
           
            case '3':  # calculate force
                clear_screen()
                try:
                    acceleration = float(compact_signs(log_user_input('What is your acceleration (m/s^2)? ')))
                    mass = abs(float(compact_signs(log_user_input('What is your mass (kg)? '))))
                    force = mass * acceleration
                    
                    log_result(force)
                    
                    if math.isinf(force):
                        invalid_input_infinityerror()
                    else:
                        print('Your force is', force, 'N')
                
                except ValueError:  # Handle invalid input
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to newton's Third law
def newtons_third_law():
    """
    This function handles calculations related to newton's Third law.
    it checks if two forces are equal based on input masses and accelerations.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("newtons_third_law() was called")
        user_input = log_user_input('What would you like to calculate?\n1. check if the forces are equal\nb to go back\nQ to stop\ninput: ')  # User input
       
        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break 
      
            case 'Q' | 'q':  # quit program
                quit_program()      
      
            case '1':  # calculate if the two forces are equal
                clear_screen()
                try:  # Try to convert user input to numbers
                    m1 = abs(float(compact_signs(log_user_input('input mass 1 (kg): '))))
                    a1 = float(compact_signs(log_user_input('input acceleration 1 (m/s^2): ')))
                    m2 = abs(float(compact_signs(log_user_input('input mass 2 (kg): '))))
                    a2 = float(compact_signs(log_user_input('input acceleration 2 (m/s^2): ')))

                    f1 = m1 * a1
                    f2 = m2 * a2
                    
                    log_result(f1, f2)
                    
                    if math.isinf(f1) or math.isinf(f2):
                        invalid_input_infinityerror()
                    else:
                        if f1 == f2:
                            print('They are equal, value is:', f1, 'N')
                        else:
                            print('They are not equal, the values are: f1 =', f1, 'N and f2 =', f2, 'N')
                
                except ValueError:  # Handle invalid input
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            
            case _:  # Handle invalid option
                invalid_input_notrecognized()
             
# function for handling calculations related to newtonian distance 
def newtonian_movement():
    """
    This function handles calculations related to newtonian distance.
    it calculates newtonian distance based on original distance, original velocity, time, and acceleration.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("newtonian_movement() was called")
        user_input = log_user_input('What would you like to calculate?\n1. distance\n2. velocity\n3. acceleration\nb to go back\nQ to stop\ninput: ') # User input
       
        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break 
      
            case 'Q' | 'q':  # quit program
                quit_program()   
                
            case '1':
                clear_screen()
                try:
                    x0 = float(compact_signs(log_user_input('input starting distance (m): '))) 
                    v0 = float(compact_signs(log_user_input('input starting velocity (m/s): ')))  
                    a = float(compact_signs(log_user_input('input acceleration (m/s^2): ')))
                    t = abs(float(compact_signs(log_user_input('input time (s): '))))
                    
                    x = x0 + v0 * t + 0.5 * a * t ** 2
                    
                    log_result(x)
                    
                    if math.isinf(x):
                        invalid_input_infinityerror()
                    else:
                        print('Your final distance is', x, 'm')
                        
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            
            case '2':
                clear_screen()
                try:
                    v0 = float(compact_signs(log_user_input('input starting velocity (m/s): ')))
                    a = float(compact_signs(log_user_input('input starting acceleration (m/s^2): ')))
                    t = abs(float(compact_signs(log_user_input('input time (s): '))))
                 
                    v = v0 + a * t
                    
                    log_result(v)
                    
                    if math.isinf(v):
                        invalid_input_infinityerror()
                    else:
                        print('Your velocity is', v, 'm/s')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            
            case '3':
                clear_screen()
                try:
                    v = float(compact_signs(log_user_input('input velocity (m/s): ')))
                    v0 = float(compact_signs(log_user_input('input starting velocity (m/s): ')))
                    t = abs(float(compact_signs(log_user_input('input time (s): '))))
                    
                    if t == 0:
                        invalid_input_zerodivisionerror()
                        continue

                    a = (v - v0) / t
                    
                    log_result(a)
                    
                    if math.isinf(a):
                        invalid_input_infinityerror()
                    else:
                        print('Your acceleration is', a, 'm/s^2')
                        
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
                 
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to gravity force
def gravity():
    """
    This function handles calculations related to gravity.
    it calculates gravity based on mass and the gravitational constant.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("gravity() was called")
        user_input = log_user_input('What would you like to calculate?\n1. gravity\n2. Mass\n3. gravitational constant\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    g_constant = float(compact_signs(log_user_input('input gravitational constant (m/s^2): ')))

                    f_g = mass * g_constant
                    
                    log_result(f_g)
                    
                    if math.isinf(f_g):
                        invalid_input_infinityerror()
                    else:
                        print('Your force of gravity is', f_g, 'N')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    g_constant = float(compact_signs(log_user_input('input gravitational constant (m/s^2): ')))
                    f_g = float(compact_signs(log_user_input('input force of gravity (N): ')))

                    if g_constant == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    mass = abs(f_g / g_constant)
                    
                    log_result(mass)
                    
                    if math.isinf(mass):
                        invalid_input_infinityerror()
                    else:
                        print('Your mass is', mass, 'kg')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    f_g = float(compact_signs(log_user_input('input force of gravity (N): ')))

                    if mass == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    g_constant = f_g / mass
                    
                    log_result(g_constant)
                    
                    if math.isinf(g_constant):
                        invalid_input_infinityerror()
                    else:
                        print('Your gravitational constant is', g_constant, 'm/s^2')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to air resistance
def air_resistance():
    """
    This function handles calculations related to air resistance.
    it calculates air resistance based on the air resistance coefficient, density, surface area, and velocity.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("air_resistance() was called")
        user_input = log_user_input('What would you like to calculate?\n1. air resistance\n2. air resistance coefficient\n3. air density\n4. Surface area\n5. velocity\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    c_w = float(compact_signs(log_user_input('input air resistance coefficient: ')))
                    density = float(compact_signs(log_user_input('input air density (kg/m^3): ')))
                    surface_area = float(compact_signs(log_user_input('input surface area (m^2): ')))
                    velocity = float(compact_signs(log_user_input('input velocity (m/s): ')))

                    f_air = 0.5 * c_w * density * surface_area * velocity ** 2
                    
                    log_result(f_air)
                    
                    if math.isinf(f_air):
                        invalid_input_infinityerror()
                    else:
                        print('Your air resistance is', f_air, 'N')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    density = float(compact_signs(log_user_input('input air density (kg/m^3): ')))
                    surface_area = float(compact_signs(log_user_input('input surface area (m^2): ')))
                    velocity = float(compact_signs(log_user_input('input velocity (m/s): ')))
                    f_air = float(compact_signs(log_user_input('input air resistance (N): ')))

                    if density == 0 or surface_area == 0 or velocity == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    c_w = (2 * f_air) / (density * surface_area * velocity ** 2)
                    
                    log_result(c_w)
                    
                    if math.isinf(c_w):
                        invalid_input_infinityerror()
                    else:
                        print('Your air resistance coefficient is', c_w)
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    c_w = float(compact_signs(log_user_input('input air resistance coefficient: ')))
                    surface_area = float(compact_signs(log_user_input('input surface area (m^2): ')))
                    velocity = float(compact_signs(log_user_input('input velocity (m/s): ')))
                    f_air = float(compact_signs(log_user_input('input air resistance (N): ')))

                    if surface_area == 0 or c_w == 0 or velocity == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    density = (2 * f_air) / (surface_area * c_w * velocity ** 2)
                    
                    log_result(density)
                    
                    if math.isinf(density):
                        invalid_input_infinityerror()
                    else:
                        print('Your density is', density, 'kg/m^3')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '4':
                clear_screen()
                try:
                    c_w = float(compact_signs(log_user_input('input air resistance coefficient: ')))
                    density = float(compact_signs(log_user_input('input air density (kg/m^3): ')))
                    velocity = float(compact_signs(log_user_input('input velocity (m/s): ')))
                    f_air = float(compact_signs(log_user_input('input air resistance (N): ')))

                    if c_w == 0 or velocity == 0 or density == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    surface_area = (2 * f_air) / (density * c_w * velocity ** 2)
                    
                    log_result(surface_area)
                    
                    if math.isinf(surface_area):
                        invalid_input_infinityerror()
                    else:
                        print('Your surface area is', surface_area, 'm^2')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '5':
                clear_screen()
                try:
                    c_w = float(compact_signs(log_user_input('input air resistance coefficient: ')))
                    density = float(compact_signs(log_user_input('input air density (kg/m^3): ')))
                    surface_area = float(compact_signs(log_user_input('input surface area (m^2): ')))
                    f_air = float(compact_signs(log_user_input('input air resistance (N): ')))

                    if density == 0 or surface_area == 0 or c_w == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    if (2 * f_air) / (density * c_w * surface_area) <= 0:
                        invalid_input_rooterror()
                        continue
                    velocity = math.sqrt((2 * f_air) / (density * c_w * surface_area))
                    
                    log_result(velocity)
                    
                    if math.isinf(velocity):
                        invalid_input_infinityerror()
                    else:
                        print('Your velocity is', velocity, 'm/s')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to static friction
def friction_static():
    """
    This function handles calculations related to static friction.
    it calculates static friction based on normal force and the static friction coefficient.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("friction_static() was called")
        user_input = log_user_input('What would you like to calculate?\n1. Static friction\n2. normal force\n3. Static friction coefficient\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    normal_force = float(compact_signs(log_user_input('input normal force (N): ')))
                    c_s_friction = float(compact_signs(log_user_input('input static friction coefficient: ')))

                    s_friction = normal_force * c_s_friction
                    
                    log_result(s_friction)
                    
                    if math.isinf(s_friction):
                        invalid_input_infinityerror()
                    else:
                        print('Your static friction is', s_friction, 'N')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    c_s_friction = float(compact_signs(log_user_input('input static friction coefficient: ')))
                    s_friction = float(compact_signs(log_user_input('input static friction (N): ')))

                    if c_s_friction == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    normal_force = s_friction / c_s_friction
                    
                    log_result(normal_force)
                    
                    if math.isinf(normal_force):
                        invalid_input_infinityerror()
                    else:
                        print('Your normal force is', normal_force, 'N')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    normal_force = float(compact_signs(log_user_input('input normal force (N): ')))
                    s_friction = float(compact_signs(log_user_input('input static friction (N): ')))

                    if normal_force == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    c_s_friction = s_friction / normal_force
                    
                    log_result(c_s_friction)
                    
                    if math.isinf(c_s_friction):
                        invalid_input_infinityerror()
                    else:
                        print('Your static friction coefficient is', c_s_friction)
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to dynamic friction
def friction_dynamic():
    """
    This function handles calculations related to dynamic friction.
    it calculates dynamic friction based on normal force and the dynamic friction coefficient.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("friction_dynamic() was called")
        user_input = log_user_input('What would you like to calculate?\n1. dynamic friction\n2. normal force\n3. dynamic friction coefficient\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    normal_force = float(compact_signs(log_user_input('input normal force (N): ')))
                    c_d_friction = float(compact_signs(log_user_input('input dynamic friction coefficient: ')))

                    d_friction = normal_force * c_d_friction
                    
                    log_result(d_friction)
                    
                    if math.isinf(d_friction):
                        invalid_input_infinityerror()
                    else:
                        print('Your dynamic friction is', d_friction, 'N')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    c_d_friction = float(compact_signs(log_user_input('input dynamic friction coefficient: ')))
                    d_friction = float(compact_signs(log_user_input('input dynamic friction (N): ')))

                    if c_d_friction == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    normal_force = d_friction / c_d_friction
                    
                    log_result(normal_force)
                    
                    if math.isinf(normal_force):
                        invalid_input_infinityerror()
                    else:
                        print('Your normal force is', normal_force, 'N')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    normal_force = float(compact_signs(log_user_input('input normal force (N): ')))
                    d_friction = float(compact_signs(log_user_input('input dynamic friction (N): ')))

                    if normal_force == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    c_d_friction = d_friction / normal_force
                    
                    log_result(c_d_friction)
                    
                    if math.isinf(c_d_friction):
                        invalid_input_infinityerror()
                    else:
                        print('Your dynamic friction coefficient is', c_d_friction)
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to spring force
def spring_force():
    """
    This function handles calculations related to spring force.
    it calculates spring force based on the spring constant and the stretch of the spring.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("spring_force() was called")
        user_input = log_user_input('What would you like to calculate?\n1. Spring force\n2. Spring constant\n3. Stretch\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    spring_c = float(compact_signs(log_user_input('input spring constant (N/m): ')))
                    stretch = float(compact_signs(log_user_input('input stretch (m): ')))

                    force_spring = spring_c * stretch
                    
                    log_result(force_spring)
                    
                    if math.isinf(force_spring):
                        invalid_input_infinityerror()
                    else:
                        print('Your spring force is', force_spring, 'N')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    stretch = float(compact_signs(log_user_input('input stretch (m): ')))
                    force_spring = float(compact_signs(log_user_input('input spring force (N): ')))

                    if stretch == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    spring_c = force_spring / stretch
                    
                    log_result(spring_c)
                    
                    if math.isinf(spring_c):
                        invalid_input_infinityerror()
                    else:
                        print('Your spring constant is', spring_c, 'N/m')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    spring_c = float(compact_signs(log_user_input('input spring constant (N/m): ')))
                    force_spring = float(compact_signs(log_user_input('input spring force (N): ')))

                    if spring_c == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    stretch = force_spring / spring_c
                    
                    log_result(stretch)
                    
                    if math.isinf(stretch):
                        invalid_input_infinityerror()
                    else:
                        print('Your stretch is', stretch, 'm')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()
    
# function for handling calculations related to centripedal force
def centripedal_force():
    """
    This function handles calculations related to centripedal force.
    it calculates centripedal force based on mass, velocity and radius.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("centripedal_force() was called")
        user_input = log_user_input('What would you like to calculate?\n1. centripedal force\n2. Mass\n3. velocity\n4. Radius\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    velocity = float(compact_signs(log_user_input('input stretch (m): ')))
                    radius = float(compact_signs(log_user_input('input radius (m): ')))

                    if radius == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    f_mpz = (mass * velocity ** 2) / radius
                    
                    log_result(f_mpz)
                    
                    if math.isinf(f_mpz):
                        invalid_input_infinityerror()
                    else:
                        print('Your centripedel force is', f_mpz, 'N')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    velocity = float(compact_signs(log_user_input('input stretch (m): ')))
                    radius = float(compact_signs(log_user_input('input radius (m): ')))
                    f_mpz = abs(float(compact_signs(log_user_input('input centripedal force (N): '))))

                    if velocity == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    mass = abs((f_mpz * radius) / velocity ** 2)
                    
                    log_result(mass)
                    
                    if math.isinf(mass):
                        invalid_input_infinityerror()
                    else:
                        print('Your mass is', mass, 'kg')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    radius = float(compact_signs(log_user_input('input radius (m): ')))
                    f_mpz = abs(float(compact_signs(log_user_input('input centripedal force (N): '))))

                    if mass == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    if ((f_mpz * radius) / mass) <= 0:
                        invalid_input_rooterror()
                        continue
                    velocity = math.sqrt((f_mpz * radius) / mass)
                    
                    log_result(velocity)
                    
                    if math.isinf(velocity):
                        invalid_input_infinityerror()
                    else:
                        print('Your velocity is', velocity, 'm/s')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '4':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    velocity = float(compact_signs(log_user_input('input stretch (m): ')))
                    f_mpz = abs(float(compact_signs(log_user_input('input centripedal force (N): '))))

                    if f_mpz == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    radius = (mass * velocity ** 2) / f_mpz
                    
                    log_result(radius)
                    
                    if math.isinf(radius):
                        invalid_input_infinityerror()
                    else:
                        print('Your radius is', radius, 'm')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
                
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to gravitational potential energy
def gravitational_potential_energy():
    """
    This function handles calculations related to gravitational potential energy.
    it calculates gravitational potential energy based on mass, gravitational acceleration, and height.
    """
    clear_screen()
    while True:  # loop for navigating back
        user_input = log_user_input('What would you like to calculate?\n1. gravitational potential energy\n2. Mass\n3. gravitational acceleration\n4. Height\nb to go back\nQ to stop\ninput: ')
        logging.info("gravitational_potential_energy() was called")
        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    gravitational_acceleration = float(compact_signs(log_user_input('input gravitational acceleration (m/s^2): ')))
                    height = float(compact_signs(log_user_input('input height (m): ')))

                    gravitational_energy = mass * gravitational_acceleration * height
                    
                    log_result(gravitational_energy)
                    
                    if math.isinf(gravitational_energy):
                        invalid_input_infinityerror()
                    else:
                        print('Your gravitational potential energy is', gravitational_energy, 'J')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    gravitational_energy = float(compact_signs(log_user_input('input gravitational potential energy (J): ')))
                    gravitational_acceleration = float(compact_signs(log_user_input('input gravitational acceleration (m/s^2): ')))
                    height = float(compact_signs(log_user_input('input height (m): ')))

                    if height == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    mass = abs(gravitational_energy / (gravitational_acceleration * height))
                    
                    log_result(mass)
                    
                    if math.isinf(mass):
                        invalid_input_infinityerror()
                    else:
                        print('Your mass is', mass, 'kg')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    gravitational_energy = float(compact_signs(log_user_input('input gravitational potential energy (J): ')))
                    height = float(compact_signs(log_user_input('input height (m): ')))

                    if height == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    gravitational_acceleration = gravitational_energy / (mass * height)
                    
                    log_result(gravitational_acceleration)
                    
                    if math.isinf(gravitational_acceleration):
                        invalid_input_infinityerror()
                    else:
                        print('Your gravitational acceleration is', gravitational_acceleration, 'm/s^2')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '4':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    gravitational_acceleration = float(compact_signs(log_user_input('input gravitational acceleration (m/s^2): ')))
                    gravitational_energy = float(compact_signs(log_user_input('input gravitational potential energy (J): ')))

                    if gravitational_acceleration == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    height = gravitational_energy / (mass * gravitational_acceleration)
                    
                    log_result(height)
                    
                    if math.isinf(height):
                        invalid_input_infinityerror()
                    else:
                        print('Your height is', height, 'm')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()
  
# function for handling calculations related to kinetic energy              
def kinetic_energy():
    """
    This function handles calculations related to kinetic energy.
    it calculates kinetic energy based on mass and velocity.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("kinetic_energy() was called")
        user_input = log_user_input('What would you like to calculate?\n1. kinetic energy\n2. Mass\n3. velocity\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    velocity = float(compact_signs(log_user_input('input velocity (m/s): ')))

                    kinetic_energy = 0.5 * mass * velocity**2
                    
                    log_result(kinetic_energy)
                    
                    if math.isinf(kinetic_energy):
                        invalid_input_infinityerror()
                    else:
                        print('Your kinetic energy is', kinetic_energy, 'J')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    velocity = float(compact_signs(log_user_input('input velocity (m/s): ')))
                    kinetic_energy = float(compact_signs(log_user_input('input kinetic energy (J): ')))

                    if velocity == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    mass = abs(2 * kinetic_energy / velocity**2)
                    
                    log_result(mass)
                    
                    if math.isinf(mass):
                        invalid_input_infinityerror()
                    else:
                        print('Your mass is', mass, 'kg')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    kinetic_energy = float(compact_signs(log_user_input('input kinetic energy (J): ')))

                    if mass == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    if (2 * kinetic_energy / mass) <= 0:
                        invalid_input_rooterror()
                        continue
                    velocity = math.sqrt(2 * kinetic_energy / mass)
                    
                    log_result(velocity)
                    
                    if math.isinf(velocity):
                        invalid_input_infinityerror()
                    else:
                        print('Your velocity is', velocity, 'm/s')
                except ValueError:
                    print(kinetic_energy)
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to kinetic energy rotation
def kinetic_energy_rotation():
    """
    This function handles calculations related to kinetic energy of rotation.
    it calculates kinetic energy of rotation based on the moment of inertia and angular velocity.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("kinetic_energy_rotation() was called")
        user_input = log_user_input('What would you like to calculate?\n1. kinetic energy of rotation\n2. Moment of inertia\n3. angular velocity\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    moment_of_inertia = float(compact_signs(log_user_input('input moment of inertia (kgm^2): ')))
                    angular_velocity = float(compact_signs(log_user_input('input angular velocity (rad/s): ')))

                    kinetic_energy_rotation = 0.5 * moment_of_inertia * angular_velocity**2
                    
                    log_result(kinetic_energy_rotation)
                    
                    if math.isinf(kinetic_energy_rotation):
                        invalid_input_infinityerror()
                    else:
                        print('Your kinetic energy of rotation is', kinetic_energy_rotation, 'J')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    angular_velocity = float(compact_signs(log_user_input('input angular velocity (rad/s): ')))
                    kinetic_energy_rotation = float(compact_signs(log_user_input('input kinetic energy of rotation (J): ')))

                    if angular_velocity == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    moment_of_inertia = 2 * kinetic_energy_rotation / (angular_velocity**2)
                    
                    log_result(moment_of_inertia)
                    
                    if math.isinf(moment_of_inertia):
                        invalid_input_infinityerror()
                    else:
                        print('Your moment of inertia is', moment_of_inertia, 'kgm^2')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    moment_of_inertia = float(compact_signs(log_user_input('input moment of inertia (kgm^2): ')))
                    kinetic_energy_rotation = float(compact_signs(log_user_input('input kinetic energy of rotation (J): ')))

                    if moment_of_inertia == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    if (2 * kinetic_energy_rotation / moment_of_inertia) <= 0:
                        invalid_input_rooterror()
                        continue
                    angular_velocity = math.sqrt(2 * kinetic_energy_rotation / moment_of_inertia)
                    
                    log_result(angular_velocity)
                    
                    if math.isinf(angular_velocity):
                        invalid_input_infinityerror()
                    else:
                        print('Your angular velocity is', angular_velocity, 'rad/s')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to momentum
def momentum():
    """
    This function handles calculations related to momentum.
    it calculates momentum based on mass and velocity.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("momentum() was called")
        user_input = log_user_input('What would you like to calculate?\n1. Momentum\n2. Mass\n3. velocity\nb to go back\nQ to stop\ninput: ')
    
        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    velocity = float(compact_signs(log_user_input('input velocity (m/s): ')))

                    momentum_result = mass * velocity
                    
                    log_result(momentum_result)
                    
                    if math.isinf(momentum_result):
                        invalid_input_infinityerror()
                    else:
                        print('Your momentum is', momentum_result, 'kgm/s')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    velocity = float(compact_signs(log_user_input('input velocity (m/s): ')))
                    momentum_result = float(compact_signs(log_user_input('input momentum (kgm/s): ')))

                    if velocity == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    mass = abs(momentum_result / velocity)
                    
                    log_result(mass)
                    
                    if math.isinf(mass):
                        invalid_input_infinityerror()
                    else:
                        print('Your mass is', mass, 'kg')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(log_user_input('input mass (kg): '))))
                    momentum_result = float(compact_signs(log_user_input('input momentum (kgm/s): ')))

                    if mass == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    velocity = momentum_result / mass
                    
                    log_result(velocity)
                    
                    if math.isinf(velocity):
                        invalid_input_infinityerror()
                    else:
                        print('Your velocity is', velocity, 'm/s')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to impulse
def impulse():
    """
    This function handles calculations related to impulse.
    it calculates impulse based on the force and radius.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("impulse() was called")
        user_input = log_user_input('What would you like to calculate?\n1. impulse\n2. force \n3. Radius \nb to go back\nQ to stop\ninput: ')
    
        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    force = float(compact_signs(log_user_input('input force (N): ')))
                    radius = float(compact_signs(log_user_input('input radius (m): ')))

                    impulse = force * radius
                    
                    log_result(impulse)
                    
                    if math.isinf(impulse):
                        invalid_input_infinityerror()
                    else:
                        print('Your impulse is', impulse, 'Nm')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    radius = float(compact_signs(log_user_input('input radius (m): ')))
                    impulse = float(compact_signs(log_user_input('input impulse (Nm): ')))

                    if radius == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    force = impulse / radius
                    
                    log_result(force)
                    
                    if math.isinf(force):
                        invalid_input_infinityerror()
                    else:
                        print('Your force is', force, 'N')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    force = float(compact_signs(log_user_input('input force (N): ')))
                    impulse = float(compact_signs(log_user_input('input impulse (Nm): ')))

                    if impulse == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    radius = impulse / force
                    
                    log_result(radius)
                    
                    if math.isinf(radius):
                        invalid_input_infinityerror()
                    else:
                        print('Your radius is', radius, 'm')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to length expansion
def length_expansion():
    """
    This function handles calculations related to the formula delta l = alpha * l0 * delta T.
    it calculates the change in length based on the linear expansion coefficient,
    the initial length, and the change in temperature.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("length_expansion() was called")
        user_input = log_user_input('What would you like to calculate?\n1. change in length\n2. linear expansion coefficient\n3. initial length\n4. change in Temperature\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    alpha = float(compact_signs(log_user_input('input linear expansion coefficient (C^-1): ')))
                    initial_length = float(compact_signs(log_user_input('input initial length (m): ')))
                    delta_temperature = float(compact_signs(log_user_input('input change in temperature (delta T): ')))

                    delta_length = alpha * initial_length * delta_temperature
                    
                    log_result(delta_length)
                    
                    print('change in length is', delta_length, 'm')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    initial_length = float(compact_signs(log_user_input('input initial length (m): ')))
                    delta_length = float(compact_signs(log_user_input('input change in length (delta m): ')))
                    delta_temperature = float(compact_signs(log_user_input('input change in temperature (delta T): ')))

                    if delta_temperature == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    alpha = delta_length / (initial_length * delta_temperature)
                    
                    log_result(alpha)
                    
                    print('linear expansion coefficient is', alpha, 'C^-1')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    alpha = float(compact_signs(log_user_input('input linear expansion coefficient (C^-1): ')))
                    delta_length = float(compact_signs(log_user_input('input change in length (delta m): ')))
                    delta_temperature = float(compact_signs(log_user_input('input change in temperature (delta T): ')))

                    if delta_temperature == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    initial_length = delta_length / (alpha * delta_temperature)
                    
                    log_result(initial_length)
                    
                    print('initial length is', initial_length, 'm')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '4':
                clear_screen()
                try:
                    alpha = float(compact_signs(log_user_input('input linear expansion coefficient (C^-1): ')))
                    initial_length = float(compact_signs(log_user_input('input initial length (m): ')))
                    delta_length = float(compact_signs(log_user_input('input change in length (delta m): ')))

                    if initial_length == 0 or alpha == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    delta_temperature = delta_length / (alpha * initial_length)
                    
                    log_result(delta_temperature)
                    
                    print('change in Temperature is', delta_temperature, '°C')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to area expansion
def area_expansion():
    """
    This function handles calculations related to the formula delta a = 2 * alpha * a0 * delta T.
    it calculates the change in area based on the linear expansion coefficient,
    the initial area, and the change in temperature.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("area_expansion() was called")
        user_input = log_user_input('What would you like to calculate?\n1. change in area\n2. linear expansion coefficient\n3. initial area\n4. change in Temperature\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    alpha = float(compact_signs(log_user_input('input linear expansion coefficient (C^-1): ')))
                    initial_area = float(compact_signs(log_user_input('input initial area (m^2): ')))
                    delta_temperature = float(compact_signs(log_user_input('input change in temperature (delta T): ')))

                    delta_area = 2 * alpha * initial_area * delta_temperature
                    
                    log_result(delta_area)
                    
                    print('change in area is', delta_area, 'm^2')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    initial_area = float(compact_signs(log_user_input('input initial area (m^2): ')))
                    delta_area = float(compact_signs(log_user_input('input change in area (delta m^2): ')))
                    delta_temperature = float(compact_signs(log_user_input('input change in temperature (delta T): ')))

                    if delta_temperature == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    alpha = delta_area / (2 * initial_area * delta_temperature)
                    
                    log_result(alpha)
                    
                    print('linear expansion coefficient is', alpha, 'C^-1')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    alpha = float(compact_signs(log_user_input('input linear expansion coefficient (C^-1): ')))
                    delta_area = float(compact_signs(log_user_input('input change in area (delta m^2): ')))
                    delta_temperature = float(compact_signs(log_user_input('input change in temperature (delta T): ')))

                    if delta_temperature == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    initial_area = delta_area / (2 * alpha * delta_temperature)
                    
                    log_result(initial_area)
                    
                    print('initial area is', initial_area, 'm^2')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '4':
                clear_screen()
                try:
                    alpha = float(compact_signs(log_user_input('input linear expansion coefficient (C^-1): ')))
                    initial_area = float(compact_signs(log_user_input('input initial area (m^2): ')))
                    delta_area = float(compact_signs(log_user_input('input change in area (delta m^2): ')))

                    if initial_area == 0 or alpha == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    delta_temperature = delta_area / (2 * alpha * initial_area)
                    
                    log_result(delta_temperature)
                    
                    print('change in Temperature is', delta_temperature, '°C')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to volume expansion
def volume_expansion():
    """
    This function handles calculations related to the formula delta v = 3 * alpha * v0 * delta T.
    it calculates the change in volume based on the volumetric expansion coefficient,
    the initial volume, and the change in temperature.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("volume_expansion() was called")
        user_input = log_user_input('What would you like to calculate?\n1. change in volume\n2. volumetric expansion coefficient\n3. initial volume\n4. change in Temperature\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    alpha = float(compact_signs(log_user_input('input volumetric expansion coefficient (C^-1): ')))
                    initial_volume = float(compact_signs(log_user_input('input initial volume (m^3): ')))
                    delta_temperature = float(compact_signs(log_user_input('input change in temperature (delta T): ')))

                    delta_volume = 3 * alpha * initial_volume * delta_temperature
                    
                    log_result(delta_volume)
                    
                    print('change in volume is', delta_volume, 'm^3')
                except ValueError:
                    invalid_input_valueerror()
                except Exception:
                    invalid_input_exceptionerror
            case '2':
                clear_screen()
                try:
                    initial_volume = float(compact_signs(log_user_input('input initial volume (m^3): ')))
                    delta_volume = float(compact_signs(log_user_input('input change in volume (delta m^3): ')))
                    delta_temperature = float(compact_signs(log_user_input('input change in temperature (delta T): ')))

                    if delta_temperature == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    alpha = delta_volume / (3 * initial_volume * delta_temperature)
                    
                    log_result(alpha)
                    
                    print('volumetric expansion coefficient is', alpha, 'C^-1')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    alpha = float(compact_signs(log_user_input('input volumetric expansion coefficient (C^-1): ')))
                    delta_volume = float(compact_signs(log_user_input('input change in volume (delta m^3): ')))
                    delta_temperature = float(compact_signs(log_user_input('input change in temperature (delta T): ')))

                    if delta_temperature == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    initial_volume = delta_volume / (3 * alpha * delta_temperature)
                    
                    log_result(initial_volume)
                    
                    print('initial volume is', initial_volume, 'm^3')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '4':
                clear_screen()
                try:
                    alpha = float(compact_signs(log_user_input('input volumetric expansion coefficient (C^-1): ')))
                    initial_volume = float(compact_signs(log_user_input('input initial volume (m^3): ')))
                    delta_volume = float(compact_signs(log_user_input('input change in volume (delta m^3): ')))

                    if initial_volume == 0 or alpha == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    delta_temperature = delta_volume / (3 * alpha * initial_volume)
                    
                    log_result(delta_temperature)
                    
                    print('change in Temperature is', delta_temperature, '°C')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculations related to isobaric work
def isobaric_heat_work():
    """
    This function handles calculations related to the formula W = p * delta v.
    it calculates work based on pressure, change in volume, and initial volume.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("isobaric_heat_work() was called")
        user_input = log_user_input('What would you like to calculate?\n1. Work\n2. Pressure\n3. change in volume\n4. initial volume\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    pressure = float(compact_signs(log_user_input('input pressure (Pa): ')))
                    delta_volume = float(compact_signs(log_user_input('input change in volume (delta v): ')))

                    work = pressure * delta_volume
                    
                    log_result(work)
                    
                    print('Work is', work, 'J')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    work = float(compact_signs(log_user_input('input work (J): ')))
                    delta_volume = float(compact_signs(log_user_input('input change in volume (delta v): ')))

                    if delta_volume == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    pressure = work / delta_volume
                    
                    log_result(pressure)
                    
                    print('Pressure is', pressure, 'Pa')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    pressure = float(compact_signs(log_user_input('input pressure (Pa): ')))
                    work = float(compact_signs(log_user_input('input work (J): ')))

                    if work == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    delta_volume = work / pressure
                    
                    log_result(delta_volume)
                    
                    print('change in volume is', delta_volume, 'm^3')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '4':
                clear_screen()
                try:
                    pressure = float(compact_signs(log_user_input('input pressure (Pa): ')))
                    work = float(compact_signs(log_user_input('input work (J): ')))

                    if pressure == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    initial_volume = work / (pressure)
                    
                    log_result(initial_volume)
                    
                    print('initial volume is', initial_volume, 'm^3')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

# function for handling calculation related to isotherm work
def isotherm_heat_work():
    """
    This function handles calculations related to isotherm work.
    it calculates work based on the provided formula.
    """
    clear_screen()
    while True:  # loop for navigating back
        logging.info("isotherm_heat_work() was called")
        user_input = log_user_input('What would you like to calculate?\n1. Work\n2. number of moles\n3. gas constant\n4. Temperature\n5. volume ratio\nb to go back\nQ to stop\ninput: ')

        match user_input:
            case 'b' | 'b':  # go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    n = float(compact_signs(log_user_input('input number of moles (mol): ')))
                    gas_constant = float(compact_signs(log_user_input('input gas constant (C^-1): ')))
                    temperature = float(compact_signs(log_user_input('input temperature (K): ')))
                    volume_ratio = float(compact_signs(log_user_input('input volume ratio (volume2/volume1): ')))

                    if volume_ratio <= 0:
                        invalid_input_logarithmerror() 
                        continue
                    # calculate work using the formula
                    work = n * gas_constant * temperature * math.log(volume_ratio)
                    
                    log_result(work)
                    
                    if math.isinf(work):
                        invalid_input_infinityerror()
                    else:
                        print('The work done is', work, 'J')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    work = float(compact_signs(log_user_input('input work done (J): ')))
                    gas_constant = float(compact_signs(log_user_input('input gas constant (C^-1): ')))
                    temperature = float(compact_signs(log_user_input('input temperature (K): ')))
                    volume_ratio = float(compact_signs(log_user_input('input volume ratio (volume2/volume1): ')))

                    if volume_ratio <= 0:
                        invalid_input_logarithmerror() 
                        continue
                    if gas_constant == 0 or temperature == 0 or math.log(volume_ratio) == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    # calculate the number of moles using the formula
                    n = work / (gas_constant * temperature * math.log(volume_ratio))
                    
                    log_result(n)
                    
                    if math.isinf(n):
                        invalid_input_infinityerror()
                    else:
                        print('The number of moles is', n)
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    work = float(compact_signs(log_user_input('input work done (J): ')))
                    n = float(compact_signs(log_user_input('input number of moles (mol): ')))
                    temperature = float(compact_signs(log_user_input('input temperature (K): ')))
                    volume_ratio = float(compact_signs(log_user_input('input volume ratio (volume2/volume1): ')))

                    if volume_ratio <= 0:
                        invalid_input_logarithmerror() 
                        continue
                    if n == 0 or temperature == 0 or math.log(volume_ratio) == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    # calculate the gas constant using the formula
                    gas_constant = work / (n * temperature * math.log(volume_ratio))
                    
                    log_result(gas_constant)
        
                    if math.isinf(gas_constant):
                        invalid_input_infinityerror()
                    else:
                        print('The gas constant is', gas_constant, 'C^-1')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '4':
                clear_screen()
                try:
                    work = float(compact_signs(log_user_input('input work done (J): ')))
                    n = float(compact_signs(log_user_input('input number of moles (mol): ')))
                    gas_constant = float(compact_signs(log_user_input('input gas constant (C^-1): ')))
                    volume_ratio = float(compact_signs(log_user_input('input volume ratio (volume2/volume1): ')))

                    if volume_ratio <= 0:
                        invalid_input_logarithmerror() 
                        continue
                    if n == 0 or gas_constant == 0 or math.log(volume_ratio) == 0:
                        invalid_input_zerodivisionerror()
                        continue
                    
                    # calculate the temperature using the formula
                    temperature = work / (n * gas_constant * math.log(volume_ratio))
                    
                    log_result(temperature)
                    
                    if math.isinf(temperature):
                        invalid_input_infinityerror()
                    else:
                        print('The temperature is', temperature, 'K')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '5':
                clear_screen()
                try:
                    work = float(compact_signs(log_user_input('input work done (J): ')))
                    n = float(compact_signs(log_user_input('input number of moles (mol): ')))
                    gas_constant = float(compact_signs(log_user_input('input gas constant (C^-1): ')))
                    temperature = float(compact_signs(log_user_input('input temperature (K): ')))

                    # calculate the volume ratio using the formula
                    volume_ratio = math.exp(work / (n * gas_constant * temperature))
                    
                    log_result(volume_ratio)
                    
                    if math.isinf(volume_ratio):
                        invalid_input_infinityerror()
                    else:
                        print('The volume ratio (volume2/volume1) is', volume_ratio)
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()
                
# function for handling calculation related to first law of thermodynamics
def thermo_first_law():
    """
    This function handles calculations related to the internal energy.
    It calculates internal energy based on Q (heat added) and W (work done).
    """
    clear_screen()
    while True:  # Loop for navigating back
        logging.info("thermo_first_law() was called")
        user_input = log_user_input('What would you like to calculate?\n1. Internal energy\n2. Heat added\n3. Work done\nB to go back\nQ to stop\nInput: ')

        match user_input:
            case 'B' | 'b':  # Go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # Quit program
                quit_program()
            case '1':
                clear_screen()
                try:
                    q = float(compact_signs(log_user_input('Input heat added (J): ')))
                    w = float(compact_signs(log_user_input('Input work done (J): ')))

                    delta_e_int = q - w
                    
                    log_result(delta_e_int)
                    
                    if math.isinf(delta_e_int):
                        invalid_input_infinityerror()
                    else:
                        print('The internal energy is', delta_e_int, 'J')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '2':
                clear_screen()
                try:
                    w = float(compact_signs(log_user_input('Input work done (J): ')))
                    delta_e_int = float(compact_signs(log_user_input('Input internal energy (J): ')))

                    q = delta_e_int + w
                    
                    log_result(q)
                    
                    if math.isinf(q):
                        invalid_input_infinityerror()
                    else:
                        print('The heat added is', q, 'J')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case '3':
                clear_screen()
                try:
                    q = float(compact_signs(log_user_input('Input heat added (J): ')))
                    delta_e_int = float(compact_signs(log_user_input('Input internal energy (J): ')))

                    w = q - delta_e_int
                    
                    log_result(w)
                    
                    if math.isinf(w):
                        invalid_input_infinityerror()
                    else:
                        print('The work done is', w, 'J')
                except ValueError:
                    invalid_input_valueerror()
                except Exception as e:
                    invalid_input_notrecognized()
            case _:  # Handle invalid option
                invalid_input_notrecognized()

