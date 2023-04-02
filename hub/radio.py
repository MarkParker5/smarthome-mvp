import RPi.GPIO as GPIO
import spidev
GPIO.setmode(GPIO.BCM)
from lib_nrf24 import NRF24
from enum import Enum


radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)
radio.setPALevel(NRF24.PA_HIGH)
radio.setDataRate(NRF24.BR_2MBPS)
radio.setChannel(0x60)
radio.setPayloadSize(2)
radio.setAutoAck(True)
radio.setRetries(10, 20)

class Device(Enum):
    relay = [0xff, 0x00, 0x00, 0x00, 0x01]
    led = [0xff, 0x00, 0x00, 0x00, 0x02]
    
def toggle(device: Device):
    radio.stopListening()
    radio.openWritingPipe(device.value)
    radio.write([0x01, 0x02])
    
def led_red():
    radio.stopListening()
    radio.openWritingPipe(Device.led.value)
    radio.write([0x02, 0x01])
    
def led_green():
    radio.stopListening()
    radio.openWritingPipe(Device.led.value)
    radio.write([0x02, 0x02])
    
def led_blue():
    radio.stopListening()
    radio.openWritingPipe(Device.led.value)
    radio.write([0x02, 0x03])