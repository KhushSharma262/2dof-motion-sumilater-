import serial
import pygame
import time

# Initialize Serial Connection to Arduino
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)  # Replace 'COM3' with your port
    time.sleep(2)  # Allow Arduino time to reset
    print("Connected to Arduino!")
except serial.SerialException as e:
    print(f"Error connecting to Arduino: {e}")
    exit()

# Initialize Pygame for Controller Input
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected! Please connect a gaming controller.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Controller Connected: {joystick.get_name()}")

# Helper Function to Send Commands to Arduino
def send_command_to_arduino(command):
    try:
        arduino.write(command.encode())  # Send command to Arduino
        print(f"Sent to Arduino: {command}")
    except Exception as e:
        print(f"Error sending command: {e}")

# Main Loop to Capture Controller Input
try:
    print("Use the controller to control the servos. Press 'Start' to exit.")
    while True:
        pygame.event.pump()  # Process controller events

        # Read joystick axes (0: horizontal, 1: vertical)
        axis_x = joystick.get_axis(0)  # Left joystick, horizontal
        axis_y = joystick.get_axis(1)  # Left joystick, vertical

        # Map joystick movements to commands
        if axis_y < -0.5:  # Joystick up
            send_command_to_arduino('w')  # Tilt up
        elif axis_y > 0.5:  # Joystick down
            send_command_to_arduino('s')  # Tilt down
        elif axis_x < -0.5:  # Joystick left
            send_command_to_arduino('a')  # Tilt left
        elif axis_x > 0.5:  # Joystick right
            send_command_to_arduino('d')  # Tilt right

        # Check if 'Start' button is pressed to exit
        if joystick.get_button(7):  # Button 7 is often the "Start" button
            print("Exiting program...")
            break

        time.sleep(0.1)  # Prevent flooding Arduino with commands
except KeyboardInterrupt:
    print("Program interrupted by user.")
finally:
    arduino.close()
    pygame.quit()
    print("Program terminated.")
