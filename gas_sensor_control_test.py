import gas_sensor_control as GAS

try:
    GAS.setup()
    GAS.loop()
except KeyboardInterrupt:
    GAS.destroy()
