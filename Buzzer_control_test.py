import Buzzer_control as buzz

try:
    buzz.setup()
    buzz.loop()
except KeyboardInterrupt:
    buzz.destroy()
