# TEST CONNECTIONS
def init_i2c():{}
def init_uart():{}
def init_adc():{}
def init_ble():{}
def init_connections():{}

# Test load everything to max value
def full_load():{}

from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
  led.value(not led.value())
  sleep(0.5)
# MATH FUNCTIONS