import pygame
import socket

# Pygame initialisieren
pygame.init()
pygame.joystick.init()

# Xbox-Controller initialisieren
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Netzwerkverbindung zum Raspberry Pi
# Ändere die IP-Adresse zu der IP, mit der du dich auf das Picar verbindest
server_address = ('10.42.0.71', 5005)  # Portnummer 5005 einfach so lassen
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def get_joystick_input():
    pygame.event.pump()
    axis_0 = joystick.get_axis(0)  # Links/Rechts (X-Achse des linken Sticks)
    axis_1 = joystick.get_axis(1)  # Vorwärts/Rückwärts (Y-Achse des linken Sticks)
    button_4 = joystick.get_button(4)  # LB
    button_5 = joystick.get_button(5)  # RB
    button_back = joystick.get_button(6)  # BACK-Taste

    return axis_0, axis_1, button_4, button_5, button_back

def main():
    try:
        while True:
            axis_0, axis_1, button_4, button_5, button_back = get_joystick_input()
            message = f"{axis_0},{axis_1},{button_4},{button_5},{button_back}"
            sock.sendto(message.encode(), server_address)
            
            if button_back:
                print("beenden")
                break
    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()
        sock.close()

if __name__ == '__main__':
    main()
