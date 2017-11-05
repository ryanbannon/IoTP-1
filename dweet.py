# import fcntl, socket, struct,
import dweepy, time, platform, random
#from grovepi import *


def getDistance():
    return random.randint(1,10)

    '''
    # Connect the Grove Ultrasonic Ranger to digital port D4
        ultrasonic_ranger = 4
        led = 2

        pinMode(led,"OUTPUT")
        unsure about this line->(pinMode(ultrasonic_ranger,"INPUT"))

        while True:
            try:
    # Read distance value from Ultrasonic
                distance = ultrasonicRead(ultrasonic_ranger)
                print(distance,'cm')
                if distance <= 20:
                    unsure about this line->(return grovepi.digitalWrite(distance))
                    digitalWrite(led,1)
                    print ("LED ON!")
                else:
                    digitalWrite(led,0)
                    print ("LED OFF!")

            except KeyboardInterrupt:
                digitalWrite(led,0)
                break
            except TypeError:
                print("Error")
            except IOError:
                print("Error")
    ----------------------------------------------------------------
    '''

def getLED():
    return random.randint(1,100)
    # Utilize and adjust sample code given by Grove to your needs
    '''

while True:
    try:
        if led == 1:
            return grovepi.digitalWrite(1)
        else:
            return grovepi.digitalWrite(0)
    ----------------------------------------------------------------
    '''

def getNoise():
    return random.randint(1,1000)

    '''
    # Connect the Grove Sound Sensor to analog port A0
        sound_sensor = 0
        grovepi.pinMode(sound_sensor,"INPUT")
        threshold_value = 0
        while True:
        try:
    # Read the sound level
            sensor_value = grovepi.analogRead(sound_sensor)

    # If louder than threshold_value, return value
            if sensor_value > threshold_value:
                unsure about this line->(return grovepi.digitalWrite(sensor_value))

            print("sensor_value = %d" %sensor_value)

        except IOError:
            print ("Error")
    ----------------------------------------------------------------
    '''

# from http://stackoverflow.com/questions/159137/getting-mac-address
#def getHwAddr(ifname):
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
#    return ':'.join(['%02x' % ord(char) for char in info[18:24]])

def post(dic):
    thing = 'ryan-iot-ca1'
    print dweepy.dweet_for(thing, dic)

def getReadings():
    dict = {}
    dict["distance"] = getDistance()
    dict["led_state"] = getLED()
    dict["noise_level"] = getNoise()
    return dict

while True:
    dict = getReadings();
    post(dict)
    time.sleep(5)
