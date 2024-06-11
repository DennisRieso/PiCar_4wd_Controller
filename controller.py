import picar_4wd as fc
import pygame

# Eventuell vorher nochmal kurz das Script "test_pygame.py" testen, ob pygame vorinstalliert ist

# Pygame initialisieren
pygame.init()
pygame.joystick.init()

# Xbox-Controller initialisieren
joystick = pygame.joystick.Joystick(0)
joystick.init()

power_val = 100

def get_joystick_input():
    pygame.event.pump()
    axis_0 = joystick.get_axis(0)  # Links/Rechts (X-Achse des linken Sticks)
    axis_1 = joystick.get_axis(1)  # Vorwärts/Rückwärts (Y-Achse des linken Sticks)
    button_4 = joystick.get_button(4)  # LB
    button_5 = joystick.get_button(5)  # RB
    button_back = joystick.get_button(6)  # BACK-Taste

    return axis_0, axis_1, button_4, button_5, button_back

###Test###
#def adjust_power(power_val, button_4, button_5):
#    if button_5:
#        if power_val <= 90:
#            power_val += 10
#            print("power_val:", power_val)
#    elif button_4:
#        if power_val >= 10:
#            power_val -= 10
#            print("power_val:", power_val)
#    return power_val

def control_car(axis_0, axis_1, power_val):
    if axis_1 < -0.5:
        fc.forward(power_val)
    elif axis_1 > 0.5:
        fc.backward(power_val)
    elif axis_0 < -0.5:
        fc.turn_left(power_val)
    elif axis_0 > 0.5:
        fc.turn_right(power_val)
    else:
        fc.stop()

def main():
    global power_val
    print("Zum Beenden: 'BACK' Taste am Xbox controller.")
    try:
        while True:
            axis_0, axis_1, button_4, button_5, button_back = get_joystick_input()
            #power_val = adjust_power(power_val, button_4, button_5)
            control_car(axis_0, axis_1, power_val)
            
            if button_back:
                print("beenden")
                break
    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()
        fc.stop()

if __name__ == '__main__':
    main()
