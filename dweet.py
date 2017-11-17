import dweepy
import random
import config
import grovepi
from grovepi import *
from time import sleep

def getDistance():

    ultrasonic_ranger = 4

    while True:
        try:
            distance = ultrasonicRead(ultrasonic_ranger)
            return distance
            sleep(1)

        except IOError:
            print ("Error")

def getTemperature():

    dht_sensor = 3

    while True:
        try:
            [temp,hum] = dht(dht_sensor,0)
            temperature = str(temp)
            return temperature
            sleep(1)

        except IOError:
            print ("Error")

def getLight():

    #Does the light sensor need to be changed to port A1 so light_sensor value [0] does
    #not clash with dht blue sensor also [0]
    light_sensor = 0

    grovepi.pinMode(light_sensor,"INPUT")

    while True:
        try:
            sensor_value = grovepi.analogRead(light_sensor)
            return sensor_value
            sleep(1)

        except IOError:
            print ("Error")

def post(dic):

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
