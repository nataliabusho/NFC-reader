"""

This example shows connecting to the PN532 with I2C (requires clock
stretching support), SPI, or UART. SPI is best, it uses the most pins but
is the most reliable and universally supported.
After initialization, try waving various 13.56MHz RFID cards over it!
"""

import api
import time
import RPi.GPIO as GPIO

from pn532 import *
locationID = '605fb0b2b1dbbcf7c526a506'

if __name__ == '__main__':
    try:
        #pn532 = PN532_SPI(debug=False, reset=20, cs=4)
        #pn532 = PN532_I2C(debug=False, reset=20, req=16)
        pn532 = PN532_UART(debug=False, reset=20)

        ic, ver, rev, support = pn532.get_firmware_version()
        print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

        # Configure PN532 to communicate with MiFare cards
        pn532.SAM_configuration()

        print('Waiting for RFID/NFC card...')
        while True:
            # Check if a card is available to read
            uid = pn532.read_passive_target(timeout=5)
            print('.', end="")
            # Try again if no card is available.
            if uid is None:
                continue
            print('Found card with UID: ', ('-'.join(str(x) for x in uid)))
            print('Get request to server to find out what user has this ID')
            RFID = '-'.join(str(x) for x in uid)
            user = api.findUserByRFID(RFID)
            print('Post request to save the user appearance to database')
            api.saveAppearance(user['_id'], locationID)
            time.sleep(0.5)
    except Exception as e:
        print(e)
    finally:
        GPIO.cleanup()
