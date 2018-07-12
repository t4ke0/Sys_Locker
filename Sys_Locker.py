#Author Yassine Messaoudi AKA TaKeO90
#I create this Program to shutdown, Restart or Lock the windows after a period
#u give it to the program 



import time
import ctypes
import subprocess
import os

print "Welcome"
time.sleep(2)
print "Please choose what the program can do for you : "

C = raw_input("Lock, Shutdown, Restart :")


T = raw_input("Time pc should be awake in seconds Please : ")






#Tracking Time
time.sleep(int(T))




def Lock() :
    
    if C == 'Lock' :
        print 'System will be Locked after 6 sec ..'
        t = 6
        while t > 0 :
            time.sleep(1)
            print t
            t -= 1 
        Lock = ctypes.windll.user32.LockWorkStation()
Lock()

def Shutdown():
    if C == 'Shutdown' :
        print 'System will shutdown after 6 sec ..'
        t = 6
        while t > 0:
            time.sleep(1)
            print t 
            t-=1
        Shutdown = os.system('shutdown -s')
        

Shutdown()

def Restart() :
    
    if C == 'Restart':
        print 'System will restart after 6 sec ..'
        t = 6
        while t > 0:
            time.sleep(1)
            print t 
            t-=1
        Restart = os.system('shutdown -r')
Restart()
    






