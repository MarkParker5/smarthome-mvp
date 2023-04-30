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