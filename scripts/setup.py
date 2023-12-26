import pygame
import os

from simulator import Graphics
import utils

# +=====================================================================+
# |                   Set here the robot parameters                     |
# |                                                                     |
ROBOT_WIDTH = 0.1 # Width of the robot chassis (meters)
INITIAL_MOTOR_SPEED = 10000 # Initial speed (rpm) of both motors
MAX_MOTOR_SPEED = 20000 # Max speed (rpm) of both motors
WHEEL_RADIUS = 0.04 # Radius of both the wheels (meters) 
SENSORS_NUMBER = 5 # Number of sensors
# |                                                                     |
# |                                                                     |
# +=====================================================================+


# Verify if the user wants to create a new setup file or use an existing one
if os.path.isfile('setup.txt'):
    print('\n\nThere is a setup.txt file already.')
    print('Do you want to overwrite it? (y/n)')
    answer = input()
    while answer not in ['y', 'n']:
        print('Invalid input. Please type \'y\' or \'n\'.')
        answer = input()

if answer == 'y':

    # +=====================================================================+
    # |                 Map, robot and sensors positioning                  |
    # +=====================================================================+
    
    # Initialize the map
    pygame.init()
    infoObject = pygame.display.Info() # Get screen dimensions
    MAP_DIMENSIONS = (infoObject.current_w - 30, infoObject.current_h - 100)
    gfx = Graphics(MAP_DIMENSIONS, 'images/robot.png', 'images/map.png')

    # Place the robot
    ROBOT_START, closed = gfx.robot_positioning()

    # Place the sensors
    SENSORS_POSITIONS, closed = gfx.sensors_positioning(ROBOT_START, closed)

    # Write exiting message on the screen
    gfx.show_important_message("The setup is complete! Exiting and saving...")
    pygame.display.update()
    pygame.time.wait(3500)


    # +=====================================================================+
    # |                        Saving the robot info                        |
    # +=====================================================================+

    setup_info = f"""{ROBOT_WIDTH}
    {INITIAL_MOTOR_SPEED}
    {MAX_MOTOR_SPEED}
    {WHEEL_RADIUS} 
    {SENSORS_NUMBER}
    {MAP_DIMENSIONS}
    {ROBOT_START}
    {SENSORS_POSITIONS}
    """

    # Write the setup.txt file
    utils.write_setup_file(setup_info)