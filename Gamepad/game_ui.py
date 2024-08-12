import streamlit as st
import pygame
import time

# Initialize Pygame
pygame.init()

# Initialize the joystick
pygame.joystick.init()

if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    st.write(f"Connected to {joystick.get_name()}")
else:
    st.write("No joystick connected.")
    exit()

st.title("Gamepad Values")

# Create placeholders for button and potentiometer (axes) values
button_table = st.empty()
axes_table = st.empty()

# Main loop to read gamepad values
while True:
    pygame.event.pump()

    # Get button values
    button_values = {f"Button {i}": joystick.get_button(i) for i in range(joystick.get_numbuttons())}

    # Get potentiometer (axes) values
    axes_values = {f"Axis {i}": joystick.get_axis(i) for i in range(joystick.get_numaxes())}

    # Update the tables with the latest values
    button_table.table(button_values)
    axes_table.table(axes_values)

    # Adding a small delay to avoid high CPU usage
    time.sleep(0.1)
