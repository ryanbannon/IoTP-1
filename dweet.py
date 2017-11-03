# import fcntl, socket, struct,
import dweepy, time, platform, random

def getTemp():
    return random.randint(1,10)
    # Utilize and adjust sample code given by Grove to your needs

def getHumidity():
    return random.randint(1,100)
    # Utilize and adjust sample code given by Grove to your needs

def getNoiseLevel():
    return random.randint(1,1000)
    # Utilize and adjust sample code given by Grove to your needs

# from http://stackoverflow.com/questions/159137/getting-mac-address
'''
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])
'''

def post(dic):
    thing = 'ryan-iot-ca1'
    print dweepy.dweet_for(thing, dic)

def getReadings():
    dict = {}
    dict["temperature"] = getTemp()
    dict["humidity"] = getHumidity()
    dict["noise_level"] = getNoiseLevel()
    return dict

while True:
    dict = getReadings();
    post(dict)
    time.sleep(5)
