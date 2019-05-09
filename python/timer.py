import sys
import time


def print_time_left(minutes):
    while minutes > 0:
        print('Minutes left:', minutes)
        minutes -= 1
        time.sleep(60)
    print('Time is up!')


minutes = int(input('How many minutes? '))
print_time_left(minutes)

