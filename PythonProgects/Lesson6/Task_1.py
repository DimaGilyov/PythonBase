from time import sleep
from itertools import cycle


class TrafficLight:
    __colors = ("red", "yellow", "green")

    def __init__(self):
        self.__color = None

    def running(self):
        for color in cycle(TrafficLight.__colors):
            self.__color = color
            print(f"Current color is '{self.__color}'")
            self.__sleep_between_light()

    def __sleep_between_light(self):
        if self.__color == "red":
            sleep(7)
        elif self.__color == "yellow":
            sleep(2)
        else:
            sleep(5)


traffic_light = TrafficLight()
traffic_light.running()
