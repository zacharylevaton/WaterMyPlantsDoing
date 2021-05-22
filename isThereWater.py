# Author: Zachary Levaton
# Description: Python file loaded onto Raspberry Pi Zero. Checks moisture level of soil and write to AWS database.
import time
import pymysql
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

# Setting up I2C protocol to allow the Raspberry Pi to read data from the moisture sensor.
i2c_bus = busio.I2C(SCL, SDA)
ss = Seesaw(i2c_bus, addr=0x36)


def isThereWater():
    """
    Function that connects to AWS Database, selects the 'moisture' table, and writes the moisture data to the db.
    """
    # Read moisture level through capacitive touch pad
    moisture = ss.moisture_read()
    sensorid = 1

    # Connecting to AWS Database
    username = 'zachlevaton'
    password = 'zalpassword'
    hostname = 'istherewaterdb.cdelqzkyx7bn.us-east-2.rds.amazonaws.com'

    # Writing to database
    db = pymysql.connect(host=hostname, user=username, password=password)
    cursor = db.cursor()
    connect_sql = '''use istherewaterdb'''
    cursor.execute(connect_sql)
    write_sql = '''insert into moisture(sensorid, moisturelevel) values(%s, %s)''' % (sensorid, moisture)
    cursor.execute(write_sql)
    db.commit()


if __name__ == "__main__":
    isThereWater()
