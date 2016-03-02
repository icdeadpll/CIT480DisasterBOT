import Ultrasonic_control as Ultra

try:
    Ultra.setup()
    Ultra.loop()
except KeyboardInterrupt:
    Ultra.destroy()
