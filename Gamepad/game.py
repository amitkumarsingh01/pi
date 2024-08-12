import pygame
from time import sleep

# Initialize Pygame
pygame.init()

# Initialize the joystick
pygame.joystick.init()

# Check if there is a connected joystick
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Connected to {joystick.get_name()}")
else:
    print("No joystick connected.")
    exit()

try:
    while True:
        pygame.event.pump()

        # Get button values
        button_values = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]
        print(button_values)

        # Get potentiometer (axes) values
        axes_values = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
        print(axes_values)

        # Display values on Thonny's dashboard
        sleep(2)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    pygame.quit()
