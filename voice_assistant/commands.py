from typing import Callable, TypeAlias
from dataclasses import dataclass


Keywords: TypeAlias = dict[float, list[str]] # weight: [keywords...]

@dataclass
class Command:
    name: str
    keywords: Keywords
    runner: Callable[[str], str]
    
all_commands: list[Command] = []

def add_command(name: str, keywords: Keywords, runner: Callable[[str], str]):
    global all_commands
    all_commands.append(Command(name, keywords, runner))

# -------------    Hello     ----------------

def hello(string: str) -> str:
    return 'Hello!'

add_command('hello', {
    1: ['hello', 'hi'],
}, hello)

# -------------    Current time     ----------------

import datetime

def current_time(string: str) -> str:
    return datetime.datetime.now().strftime('%H:%M')

add_command('current_time', {
    1: ['How much time is it', 'What time is it'],
    0.5: ['time'],
}, current_time)

# -------------    SmartHome     ----------------

import requests

base_url = 'http://raspberrypi:8000'

def toggle_relay(string: str) -> str:
    response = requests.get(f'{base_url}/toggle/relay')
    if response.status_code == 200:
        return 'Relay toggled'
    else:
        return 'Request failed'
    
add_command('toggle_relay', {
    1: ['toggle relay', 'toggle light'],
    0.5: ['light', 'relay', 'lamp', 'toggle'],
}, toggle_relay)

def toggle_led(string: str) -> str:
    response = requests.get(f'{base_url}/toggle/led')
    if response.status_code == 200:
        return 'LED toggled'
    else:
        return 'Request failed'
    
add_command('toggle_led', {
    1: ['toggle led'],
    0.5: ['led'],
}, toggle_led)

def led_red(string: str) -> str:
    response = requests.get(f'{base_url}/led/red')
    if response.status_code == 200:
        return 'LED set to red'
    else:
        return 'Request failed'

add_command('led_red', {
    1: ['led red', 'turn on red led', 'turn on red light'],
    0.5: ['red',],
    0.1: ['light', 'led']
}, led_red)

def led_green(string: str) -> str:
    response = requests.get(f'{base_url}/led/green')
    if response.status_code == 200:
        return 'LED set to green'
    else:
        return 'Request failed'
    
add_command('led_green', {
    1: ['led green', 'turn on green led', 'turn on green light'],
    0.5: ['green',],
    0.1: ['light', 'led']
}, led_green)

def led_blue(string: str) -> str:
    response = requests.get(f'{base_url}/led/blue')
    if response.status_code == 200:
        return 'LED set to blue'
    else:
        return 'Request failed'

add_command('led_blue', {
    1: ['led blue', 'turn on blue led', 'turn on blue light'],
    0.5: ['blue',],
    0.1: ['light', 'led']
}, led_blue)
