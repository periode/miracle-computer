from sys import stdout
from time import sleep

interval = 0.03

def set_interval(new_value):
    global interval
    interval = new_value

def spell(string, line_break):
    index = 0

    while index < len(string):
        stdout.write(string[index])
        stdout.flush()
        sleep(interval)
        index += 1

    for x in range (0, line_break):
        print(" ")
