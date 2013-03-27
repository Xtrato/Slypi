#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate(busnum = 0)

# The following are the modules which can be added the SlyPi Device.
# To add the module simply define the function below and then add the module name and function name to the modules dictonary.
# All code the module executes is to be placed in the function.
def inlineSniffer():
    print "Inline Sniffer"
    
def printer():
    print "Mass Network Printer"
    
def aprSpoof():
    print "ARP Cache Poisoning"

def reverseSSH():
    print 'Reverse SSH'

def deauthFlood():
    print 'Deauth Flood'
    
def upsidedown():
    print 'Upside Down internet'
    
def nmapScanUpload():
    print 'Nmap Scan & Upload'  

#Contains all modules which can be run on the device. The key is the displayed name on the LCD and the value is the function name
modules = {'Inline Ethernet\nSniffer': 'inlineSniffer', 'Mass Network\nPrinter': 'printer', 'ARP Cache\nSpoofing': 'aprSpoof', 'Reverse SSH\nTunnel': 'reverseSSH', 'Deauth\nFlooding': 'deauthFlood', 'Upside-Down\nInternet': 'upsidedown', 'NMAP Scan\nand Upload': 'nmapScanUpload'}
displayText = modules.keys()
# Clears the display
lcd.clear()
#Used to control the flow through the menu
menuOption = 0
lcd.backlight(lcd.BLUE)
lcd.message("SlyPi\nPress Select")

#The following while loop controls the LCD menu and the control using the keypad through the menu.
while True:
    if lcd.buttonPressed(lcd.SELECT):
        sleep(0.5)
        lcd.clear()
        lcd.message(displayText[menuOption])
        while True:
            if lcd.buttonPressed(lcd.DOWN):
                menuOption = menuOption + 1
                if menuOption > len(modules) - 1:
                    menuOption = 0
                lcd.clear()
                lcd.message(displayText[menuOption])
                sleep(0.5)
            if lcd.buttonPressed(lcd.UP):
                menuOption = menuOption - 1
                if menuOption < 0:
                    menuOption = len(modules) - 1
                lcd.clear()
                lcd.message(displayText[menuOption])
                sleep(0.5)
            if lcd.buttonPressed(lcd.SELECT):
                globals().get(modules[displayText[menuOption]])()
                sleep(0.5)                 