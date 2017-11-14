import dweepy
#import platform
import random
import config
#import grovepi
#from grovepi import *
from time import sleep

def getDistance():
    return random.randint(1,100)
    '''
    ultrasonic_ranger = 4

    while True:
        try:
            distance = ultrasonicRead(ultrasonic_ranger)
            return distance
            sleep(1)

        except IOError:
            print ("Error")
    '''
def getTemperature():
    return random.randint(1,30)
    '''
    sensor = 3

    blue = 0
    white = 1

    while True:
        try:
            [temp] = grovepi.dht(sensor,blue)
            if math.isnan(temp) == False:
                return temp
                sleep(1)

        except IOError:
            print ("Error")
    '''
def getLight():
    return random.randint(1,500)
    '''
    light_sensor = 0

    grovepi.pinMode(light_sensor,"INPUT")

    while True:
        try:
            sensor_value = grovepi.analogRead(light_sensor)
            return sensor_value
            sleep(1)

        except IOError:
            print ("Error")
    '''
def post(dic):
    #thing = 'ryan-iot-ca1'
    #print dweepy.dweet_for(thing, dic)

    thing = config.thing
    print dweepy.dweet_for(thing, dic)

def getReadings():
    dict = {}
    dict["distance"] = getDistance()
    dict["temperature"] = getTemperature()
    dict["light_level"] = getLight()
    return dict

while True:
    dict = getReadings();
    post(dict)
    sleep(5)
