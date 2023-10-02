import sys
import os
import math

# Function to clear the terminal
def clear_screen():
    # Check the operating system and clear the screen accordingly
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')
        
# Function to quit the program
def Quit_program():
    """
    This function quits the program and displays a goodbye message.
    """
    clear_screen()
    print("Goodbye")
    sys.exit()  

# Function for handling invalid inputs when a division by zero occurs
def Invalid_input_ZeroDivisionError():
    """
    This function prints an error message for when a division by zero is made.
    """
    clear_screen()
    print("Invalid input, you got a division by zero")
    
# Function for handling invalid inputs when a non-numerical value is entered
def Invalid_input_ValueError():
    """
    This function prints an error message for when a non-numerical value is entered.
    """
    clear_screen()
    print("Invalid input, please input a valid numerical value")

# Function for handling invalid inputs when a command isn't recognized
def Invalid_input_NotRecognized():
    """
    This function prints an error message for when a command a user made isn't recognized.
    """
    clear_screen()
    print("This program does not recognize that command. Please try again.")

# Function for handling when a number becomes infinity
def Invalid_input_InfinityError():
    """
    This function prints an error message when a number reaches infinity
    """
    clear_screen()
    print('The result is infinity. Please check your input values.')

# Function for handling an error that isnt expected by the program
def invalid_input_exceptionerror():
    """
    This function prints an error message when a number reaches infinity
    """
    clear_screen()
    print("An unexpected error occurred")

# Function for handling multiple plus and minus signs
def compact_signs(number_str):
    # Continue looping until no more consecutive plus or minus signs are found
    while True:
        # Replace consecutive double minus signs with a single plus sign
        # Replace combinations of plus and minus signs with a single minus sign
        new_str = number_str.replace("--", "+").replace("+-", "-").replace("-+", "-").replace("++", "+")
        
        # If the modified string is the same as the original string, exit the loop
        if new_str == number_str:
            break
        
        # Update the original string with the modified one for the next iteration
        number_str = new_str

    # After handling consecutive signs, check the count of plus and minus signs
    if number_str.count('+') > 1:
        # If there are more than one plus signs, simplify to a single plus sign
        number_str = '+'
    elif number_str.count('-') > 1:
        # If there are more than one minus signs, simplify to a single minus sign
        number_str = '-'

    # Return the simplified number string
    return number_str

# Function for handling calculations related to Newton's First Law
def Newtons_first_law():
    """
    This function handles calculations related to Newton's First Law.
    It provides options to calculate momentum, mass, and velocity.
    """
    clear_screen()
    while True:  # Loop for navigating back
        
        user_input = input("What would you like to calculate?\n1. Momentum\n2. Mass\n3. Velocity\nB to go back\nQ to stop\nInput: ")  # User input
        
        match user_input:
            case 'B' | 'b':  # Go back to the previous menu
                clear_screen()
                break
            
            case 'Q' | 'q':  # Quit program
                Quit_program()
            
            case '1':  # Calculate the momentum
                clear_screen()
                try:  # Try to convert user input to numbers
                    mass = abs(float(compact_signs(input("What is your mass (kg)? "))))
                    velocity = float(compact_signs(input("What is your velocity (m/s)? ")))
                    momentum = mass * velocity
                    
                    if math.isinf(momentum):
                        Invalid_input_InfinityError()
                    else:
                        print('Your momentum is: ', momentum, 'N')
                       
                except ValueError:  # Handle invalid input
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
                    
            case '2':  # Calculate the Mass
                clear_screen()
                try:
                    momentum = float(compact_signs(input("What is your momentum (N)? ")))
                    velocity = float(compact_signs(input("What is your velocity (m/s)? ")))
                    
                    if velocity == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    
                    mass = abs(momentum / velocity)  # Mass has to be absolute
                    
                    if math.isinf(mass):
                        Invalid_input_InfinityError()
                    else:
                        print('Your mass is: ', mass, 'Kg')
                    
                except ValueError:  # Handle invalid input
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
                    
            case '3':  # Calculate velocity
                clear_screen()
                try:
                    mass = abs(float(compact_signs(input("What is your mass (kg)? "))))
                    momentum = float(compact_signs(input("What is your Momentum (N)? ")))
                    
                    if mass == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    
                    velocity = momentum / mass
                    
                    if math.isinf(velocity):
                        Invalid_input_InfinityError()
                    else:
                        print('Your velocity is: ', velocity, 'm/s')
                    
                except ValueError:  # Handle invalid input
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
                    
            case _:  # Handle invalid option
                Invalid_input_NotRecognized()

# Function for handling calculations related to Newton's Second Law
def Newtons_second_law():
    """
    This function handles calculations related to Newton's Second Law.
    It provides options to calculate mass, acceleration, and force.
    """
    clear_screen()
    while True:  # Loop for navigating back
       
        user_input = input("What do you want to calculate?\n1. Mass\n2. Acceleration\n3. Force\nB to go back\nQ to stop\nInput: ")  # User input
        
        match user_input:
            case 'B' | 'b':  # Go back to the previous menu
                clear_screen()
                break 
            
            case 'Q' | 'q':  # Quit program
                Quit_program()        
            
            case '1':  # Calculate mass
                clear_screen()
                try:  # Try to convert user input to numbers
                    force = float(compact_signs(input('What is your force (N)? ')))
                    acceleration = float(compact_signs(input('What is your acceleration (m/s^2)? ')))
                    
                    if acceleration == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    
                    mass = abs(force / acceleration)  # Mass has to be absolute
                    
                    if math.isinf(mass):
                        Invalid_input_InfinityError()
                    else:
                        print('Your mass is', mass, 'Kg')
                
                except ValueError:  # Handle invalid input
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            
            case '2':  # Calculate acceleration
                clear_screen()
                try:
                    force = float(compact_signs(input('What is your force (N)? ')))
                    mass = abs(float(compact_signs(input('What is your mass (Kg)? '))))
                    
                    if mass == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    
                    acceleration = force / mass
                    
                    if math.isinf(acceleration):
                        Invalid_input_InfinityError()
                    else:
                        print('Your acceleration is', acceleration, 'm/s')
                
                except ValueError:  # Handle invalid input
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
           
            case '3':  # Calculate force
                clear_screen()
                try:
                    acceleration = float(compact_signs(input('What is your acceleration (m/s^2)? ')))
                    mass = abs(float(compact_signs(input('What is your mass (Kg)? '))))
                    force = mass * acceleration
                    
                    if math.isinf(force):
                        Invalid_input_InfinityError()
                    else:
                        print('Your force is', force, 'N')
                
                except ValueError:  # Handle invalid input
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            
            case _:  # Handle invalid option
                Invalid_input_NotRecognized()

# Function for handling calculations related to Newton's Third Law
def Newtons_third_law():
    """
    This function handles calculations related to Newton's Third Law.
    It checks if two forces are equal based on input masses and accelerations.
    """
    clear_screen()
    while True:  # Loop for navigating back
       
        user_input = input('What would you like to calculate?\n1. Check if the forces are equal\nB to go back\nQ to stop\nInput: ')  # User input
       
        match user_input:
            case 'B' | 'b':  # Go back to the previous menu
                clear_screen()
                break 
      
            case 'Q' | 'q':  # Quit program
                Quit_program()      
      
            case '1':  # Calculate if the two forces are equal
                clear_screen()
                try:  # Try to convert user input to numbers
                    m1 = abs(float(compact_signs(input('Input mass 1 (Kg): '))))
                    a1 = float(compact_signs(input('Input acceleration 1 (m/s^2): ')))
                    m2 = abs(float(compact_signs(input('Input mass 2 (Kg): '))))
                    a2 = float(compact_signs(input('Input acceleration 2 (m/s^2): ')))

                    f1 = m1 * a1
                    f2 = m2 * a2
                    
                    if math.isinf(f1) or math.isinf(f2):
                        Invalid_input_InfinityError()
                    else:
                        if f1 == f2:
                            print('They are equal, value is:', f1, 'N')
                        else:
                            print('They are not equal, the values are: F1 =', f1, 'N and F2 =', f2, 'N')
                
                except ValueError:  # Handle invalid input
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            
            case _:  # Handle invalid option
                Invalid_input_NotRecognized()
             
# Function for handling calculations related to Newtonian distance 
def Newtonian_movement():
    """
    This function handles calculations related to Newtonian distance.
    It calculates Newtonian distance based on original distance, original speed, time, and acceleration.
    """
    clear_screen()
    while True:  # Loop for navigating back
       
        user_input = input('What would you like to calculate?\n1. Distance\n2. Speed\n3. Acceleration\nB to go back\nQ to stop\nInput: ') # User input
       
        match user_input:
            case 'B' | 'b':  # Go back to the previous menu
                clear_screen()
                break 
      
            case 'Q' | 'q':  # Quit program
                Quit_program()   
                
            case '1':
                clear_screen()
                try:
                    x0 = float(compact_signs(input('Input starting distance (m): '))) 
                    v0 = float(compact_signs(input('Input starting speed (m/s): ')))  
                    a = float(compact_signs(input('Input acceleration (m/s^2): ')))
                    t = abs(float(compact_signs(input('Input time (s): '))))
                    
                    x = x0 + v0 * t + 0.5 * a * t ** 2
                    
                    if math.isinf(x):
                        Invalid_input_InfinityError()
                    else:
                        print('Your final distance is', x, 'm')
                        
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            
            case '2':
                clear_screen()
                try:
                    v0 = float(compact_signs(input('Input starting speed (m/s): ')))
                    a = float(compact_signs(input('Input starting acceleration (m/s^2): ')))
                    t = abs(float(compact_signs(input('Input time (s): '))))
                 
                    v = v0 + a * t
                    
                    if math.isinf(v):
                        Invalid_input_InfinityError()
                    else:
                        print('Your speed is', v, 'm/s')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            
            case '3':
                clear_screen()
                try:
                    v = float(compact_signs(input('Input speed (m/s): ')))
                    v0 = float(compact_signs(input('Input starting speed (m/s): ')))
                    t = abs(float(compact_signs(input('Input time (s): '))))
                    
                    if t == 0:
                        Invalid_input_ZeroDivisionError()
                        continue

                    a = (v - v0) / t
                    
                    if math.isinf(a):
                        Invalid_input_InfinityError()
                    else:
                        print('Your acceleration is', a, 'm/s^2')
                        
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
                 
            case _:  # Handle invalid option
                Invalid_input_NotRecognized()

# Function for handling calculations related to gravity force
def gravity():
    """
    This function handles calculations related to gravity.
    It calculates gravity based on mass and the gravitational constant.
    """
    clear_screen()
    while True:  # loop for navigating back

        user_input = compact_signs(input('What would you like to calculate?\n1. Gravity\n2. Mass\n3. Gravitational constant\nB to go back\nQ to stop\nInput: '))

        match user_input:
            case 'B' | 'b':  # Go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # Quit program
                Quit_program()
            case '1':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(input('Input mass (kg): '))))
                    g_constant = float(compact_signs(input('Input gravitational constant (m/s^2): ')))

                    f_g = mass * g_constant
                    if math.isinf(f_g):
                        Invalid_input_InfinityError()
                    else:
                        print('Your force of gravity is', f_g, 'N')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '2':
                clear_screen()
                try:
                    g_constant = float(compact_signs(input('Input gravitational constant (m/s^2): ')))
                    f_g = float(compact_signs(input('Input force of gravity (N): ')))

                    if g_constant == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    mass = f_g / g_constant
                    if math.isinf(mass):
                        Invalid_input_InfinityError()
                    else:
                        print('Your mass is', mass, 'Kg')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '3':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(input('Input mass (kg): '))))
                    f_g = float(compact_signs(input('Input force of gravity (N): ')))

                    if mass == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    g_constant = f_g / mass
                    if math.isinf(g_constant):
                        Invalid_input_InfinityError()
                    else:
                        print('Your gravitational constant is', g_constant, 'm/s^2')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case _:  # Handle invalid option
                Invalid_input_NotRecognized()

# Function for handling calculations related to air resistance
def air_resistance():
    """
    This function handles calculations related to air resistance.
    It calculates air resistance based on the air resistance coefficient, density, surface area, and speed.
    """
    clear_screen()
    while True:  # loop for navigating back

        user_input = input('What would you like to calculate?\n1. Air resistance\n2. Air resistance coefficient\n3. Air density\n4. Surface area\n5. Speed\nB to go back\nQ to stop\nInput: ')

        match user_input:
            case 'B' | 'b':  # Go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # Quit program
                Quit_program()
            case '1':
                clear_screen()
                try:
                    c_w = float(compact_signs(input('Input air resistance coefficient: ')))
                    density = float(compact_signs(input('Input air density (kg/m^3): ')))
                    surface_area = float(compact_signs(input('Input surface area (m^2): ')))
                    speed = float(compact_signs(input('Input speed (m/s): ')))

                    f_air = 0.5 * c_w * density * surface_area * speed ** 2
                    if math.isinf(f_air):
                        Invalid_input_InfinityError()
                    else:
                        print('Your air resistance is', f_air, 'N')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '2':
                clear_screen()
                try:
                    density = float(compact_signs(input('Input air density (kg/m^3): ')))
                    surface_area = float(compact_signs(input('Input surface area (m^2): ')))
                    speed = float(compact_signs(input('Input speed (m/s): ')))
                    f_air = float(compact_signs(input('Input air resistance (N): ')))

                    if density == 0 or surface_area == 0 or speed == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    c_w = (2 * f_air) / (density * surface_area * speed ** 2)
                    if math.isinf(c_w):
                        Invalid_input_InfinityError()
                    else:
                        print('Your air resistance coefficient is', c_w)
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '3':
                clear_screen()
                try:
                    c_w = float(compact_signs(input('Input air resistance coefficient: ')))
                    surface_area = float(compact_signs(input('Input surface area (m^2): ')))
                    speed = float(compact_signs(input('Input speed (m/s): ')))
                    f_air = float(compact_signs(input('Input air resistance (N): ')))

                    if surface_area == 0 or c_w == 0 or speed == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    density = (2 * f_air) / (surface_area * c_w * speed ** 2)
                    if math.isinf(density):
                        Invalid_input_InfinityError()
                    else:
                        print('Your density is', density, 'kg/m^3')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '4':
                clear_screen()
                try:
                    c_w = float(compact_signs(input('Input air resistance coefficient: ')))
                    density = float(compact_signs(input('Input air density (kg/m^3): ')))
                    speed = float(compact_signs(input('Input speed (m/s): ')))
                    f_air = float(compact_signs(input('Input air resistance (N): ')))

                    if c_w == 0 or speed == 0 or density == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    surface_area = (2 * f_air) / (density * c_w * speed ** 2)
                    if math.isinf(surface_area):
                        Invalid_input_InfinityError()
                    else:
                        print('Your surface area is', surface_area, 'm^2')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '5':
                clear_screen()
                try:
                    c_w = float(compact_signs(input('Input air resistance coefficient: ')))
                    density = float(compact_signs(input('Input air density (kg/m^3): ')))
                    surface_area = float(compact_signs(input('Input surface area (m^2): ')))
                    f_air = float(compact_signs(input('Input air resistance (N): ')))

                    if density == 0 or surface_area == 0 or c_w == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    speed = math.sqrt((2 * f_air) / (density * c_w * surface_area))
                    if math.isinf(speed):
                        Invalid_input_InfinityError()
                    else:
                        print('Your speed is', speed, 'm/s')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case _:  # Handle invalid option
                Invalid_input_NotRecognized()

# Function for handling calculations related to static friction
def friction_static():
    """
    This function handles calculations related to static friction.
    It calculates static friction based on normal force and the static friction coefficient.
    """
    clear_screen()
    while True:  # loop for navigating back

        user_input = compact_signs(input('What would you like to calculate?\n1. Static friction\n2. Normal force\n3. Static friction coefficient\nB to go back\nQ to stop\nInput: '))

        match user_input:
            case 'B' | 'b':  # Go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # Quit program
                Quit_program()
            case '1':
                clear_screen()
                try:
                    normal_force = float(compact_signs(input('Input normal force (N): ')))
                    c_s_friction = float(compact_signs(input('Input static friction coefficient: ')))

                    s_friction = normal_force * c_s_friction
                    if math.isinf(s_friction):
                        Invalid_input_InfinityError()
                    else:
                        print('Your static friction is', s_friction, 'N')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '2':
                clear_screen()
                try:
                    c_s_friction = float(compact_signs(input('Input static friction coefficient: ')))
                    s_friction = float(compact_signs(input('Input static friction (N): ')))

                    if c_s_friction == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    normal_force = s_friction / c_s_friction
                    if math.isinf(normal_force):
                        Invalid_input_InfinityError()
                    else:
                        print('Your normal force is', normal_force, 'N')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '3':
                clear_screen()
                try:
                    normal_force = float(compact_signs(input('Input normal force (N): ')))
                    s_friction = float(compact_signs(input('Input static friction (N): ')))

                    if normal_force == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    c_s_friction = s_friction / normal_force
                    if math.isinf(c_s_friction):
                        Invalid_input_InfinityError()
                    else:
                        print('Your static friction is', c_s_friction, 'N')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case _:  # Handle invalid option
                Invalid_input_NotRecognized()

# Function for handling calculations related to dynamic friction
def friction_dynamic():
    """
    This function handles calculations related to dynamic friction.
    It calculates dynamic friction based on normal force and the dynamic friction coefficient.
    """
    clear_screen()
    while True:  # loop for navigating back

        user_input = input('What would you like to calculate?\n1. Dynamic friction\n2. Normal force\n3. Dynamic friction coefficient\nB to go back\nQ to stop\nInput: ')

        match user_input:
            case 'B' | 'b':  # Go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # Quit program
                Quit_program()
            case '1':
                clear_screen()
                try:
                    normal_force = float(compact_signs(input('Input normal force (N): ')))
                    c_d_friction = float(compact_signs(input('Input dynamic friction coefficient: ')))

                    d_friction = normal_force * c_d_friction
                    if math.isinf(d_friction):
                        Invalid_input_InfinityError()
                    else:
                        print('Your dynamic friction is', d_friction, 'N')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '2':
                clear_screen()
                try:
                    c_d_friction = float(compact_signs(input('Input dynamic friction coefficient: ')))
                    d_friction = float(compact_signs(input('Input dynamic friction (N): ')))

                    if c_d_friction == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    normal_force = d_friction / c_d_friction
                    if math.isinf(normal_force):
                        Invalid_input_InfinityError()
                    else:
                        print('Your normal force is', normal_force, 'N')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '3':
                clear_screen()
                try:
                    normal_force = float(compact_signs(input('Input normal force (N): ')))
                    d_friction = float(compact_signs(input('Input dynamic friction (N): ')))

                    if normal_force == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    c_d_friction = d_friction / normal_force
                    if math.isinf(c_d_friction):
                        Invalid_input_InfinityError()
                    else:
                        print('Your dynamic friction is', c_d_friction, 'N')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case _:  # Handle invalid option
                Invalid_input_NotRecognized()

# Function for handling calculations related to spring force
def spring_force():
    """
    This function handles calculations related to spring force.
    It calculates spring force based on the spring constant and the stretch of the spring.
    """
    clear_screen()
    while True:  # loop for navigating back

        user_input = input('What would you like to calculate?\n1. Spring force\n2. Spring constant\n3. Stretch\nB to go back\nQ to stop\nInput: ')

        match user_input:
            case 'B' | 'b':  # Go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # Quit program
                Quit_program()
            case '1':
                clear_screen()
                try:
                    spring_c = float(compact_signs(input('Input spring constant (N/m): ')))
                    stretch = float(compact_signs(input('Input stretch (m): ')))

                    force_spring = spring_c * stretch
                    if math.isinf(force_spring):
                        Invalid_input_InfinityError()
                    else:
                        print('Your spring force is', force_spring, 'N')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '2':
                clear_screen()
                try:
                    stretch = float(compact_signs(input('Input stretch (m): ')))
                    force_spring = float(compact_signs(input('Input spring force (N): ')))

                    if stretch == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    spring_c = force_spring / stretch
                    if math.isinf(spring_c):
                        Invalid_input_InfinityError()
                    else:
                        print('Your spring constant is', spring_c, 'N/m')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '3':
                clear_screen()
                try:
                    spring_c = float(compact_signs(input('Input spring constant (N/m): ')))
                    force_spring = float(compact_signs(input('Input spring force (N): ')))

                    if spring_c == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    stretch = force_spring / spring_c
                    if math.isinf(stretch):
                        Invalid_input_InfinityError()
                    else:
                        print('Your stretch is', stretch, 'm')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case _:  # Handle invalid option
                Invalid_input_NotRecognized()
    
# Function for handling calculations related to centripedal force
def centripedal_force():
    """
    This function handles calculations related to centripedal force.
    It calculates centripedal force based on mass, velocity and radius.
    """
    clear_screen()
    while True:  # loop for navigating back
        
        user_input = input('What would you like to calculate?\n1. Centripedal force\n2. Mass\n3. Velocity\n4. Radius\nB to go back\nQ to stop\nInput: ')

        match user_input:
            case 'B' | 'b':  # Go back to the previous menu
                clear_screen()
                break
            case 'Q' | 'q':  # Quit program
                Quit_program()
            case '1':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(input('Input mass (kg): '))))
                    velocity = float(compact_signs(input('Input stretch (m): ')))
                    radius = float(compact_signs(input('Input radius (m): ')))

                    if radius == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    f_mpz = (mass * velocity ** 2) / radius
                    if math.isinf(f_mpz):
                        Invalid_input_InfinityError()
                    else:
                        print('Your centripedel force is', f_mpz, 'N')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '2':
                clear_screen()
                try:
                    velocity = float(compact_signs(input('Input stretch (m): ')))
                    radius = float(compact_signs(input('input radius (m): ')))
                    f_mpz = abs(float(compact_signs(input('Input mass (kg): '))))

                    if velocity == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    mass = (f_mpz * radius) / velocity ** 2
                    if math.isinf(mass):
                        Invalid_input_InfinityError()
                    else:
                        print('Your mass is', mass, 'kg')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '3':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(input('Input mass (kg): '))))
                    radius = float(compact_signs(input('Input radius (m): ')))
                    f_mpz = abs(float(compact_signs(input('Input mass (kg): '))))

                    if mass == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    velocity = math.sqrt((f_mpz * radius) / mass)
                    if math.isinf(velocity):
                        Invalid_input_InfinityError()
                    else:
                        print('Your velocity is', velocity, 'm/s')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
            case '4':
                clear_screen()
                try:
                    mass = abs(float(compact_signs(input('Input mass (kg): '))))
                    velocity = float(compact_signs(input('Input stretch (m): ')))
                    f_mpz = abs(float(compact_signs(input('Input mass (kg): '))))

                    if f_mpz == 0:
                        Invalid_input_ZeroDivisionError()
                        continue
                    radius = (mass * velocity ** 2) / f_mpz
                    if math.isinf(radius):
                        Invalid_input_InfinityError()
                    else:
                        print('Your radius is', radius, 'm')
                except ValueError:
                    Invalid_input_ValueError()
                except Exception as e:
                    Invalid_input_NotRecognized()
                
            case _:  # Handle invalid option
                Invalid_input_NotRecognized()
