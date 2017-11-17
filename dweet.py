import dweepy
import config
import grovepi
from grovepi import *
from time import sleep
import sqlite3

# with help from: https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_ultrasonic.py
def getDistance():
    ultrasonic_ranger = 4

    while True:
        try:
            distance = ultrasonicRead(ultrasonic_ranger)
            return distance
            sleep(1)

        except IOError:
            print ("Error")

# with help from: https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_light_sensor.py
def getLight():
    light_sensor = 1

    pinMode(light_sensor,"INPUT")

    while True:
        try:
            sensor_value = analogRead(light_sensor)
            return sensor_value

        except IOError:
            print ("Error")

# with help from: https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_dht_pro.py
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

def post(dic):
    thing = config.thing
    print dweepy.dweet_for(thing, dic)

def getReadings():
    dict = {}
    dict["distance"] = getDistance()
    dict["light_level"] = getLight()
    dict["temperature"] = getTemperature()
    return dict

while True:
    dict = getReadings();
    post(dict)

    conn = sqlite3.connect("dweet.sqlite")
    #c = conn.cursor()
    #c.execute('IF NOT EXISTS (CREATE TABLE Sensor_Readings(dist_value INTEGER, light_value INTEGER, temp_value INTEGER));')
    #dbUpdate = "INSERT INTO Sensor_Readings(dist_value, light_value, temp_value) VALUES(dict["distance"], dict["light_level"], dict["temperature"])"
    #conn.commit()
    #c.execute(dbUpdate)

    sleep(5)
