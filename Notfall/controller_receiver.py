import picar_4wd as fc
import socket

# Netzwerkverbindung einrichten
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# IP des Laptops eingeben, welche die Verbindung zum Raspberry ermöglicht!
server_address = ('0.0.0.0', 5005)  # Lausche auf Port 5005
sock.bind(server_address)

power_val = 100

###TEST###
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
    print("Warte auf Steuerungsbefehle...")
    try:
        while True:
            data, _ = sock.recvfrom(4096)
            axis_0, axis_1, button_4, button_5, button_back = map(float, data.decode().split(','))
            #power_val = adjust_power(power_val, button_4, button_5)
            control_car(axis_0, axis_1, power_val)
            
            if button_back:
                print("beenden")
                break
    except KeyboardInterrupt:
        pass
    finally:
        fc.stop()
        sock.close()

if __name__ == '__main__':
    main()
