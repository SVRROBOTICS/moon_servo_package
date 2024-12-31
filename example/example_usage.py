import time
from moon_servo.connection import ModbusConnection
from moon_servo.motor import MoonServoMotor

# Initialize the motor with the desired parameters (passing port and baudrate directly)
motor = MoonServoMotor(port='/dev/ttyUSB0', baudrate=115200, base_address=0)  # Use port and baudrate here

# Connect to the motor
motor.connect()

# Control motor
motor.enable_driver1()
motor.enable_driver2()

motor.start_jogging1()
motor.start_jogging2()

motor.set_speed1(5000)
motor.set_speed2(5000)


time.sleep(5)
motor.stop_jogging1()
motor.stop_jogging2()

motor.disable_driver1()
motor.disable_driver2()

#Read Registe value
motor.read_register_32bit1(40011)
motor.read_register_32bit2(41011)
# Close connection
motor.disconnect()

