'''
Website Blocker for certain times in the day
'''

import time
from datetime import datetime as dt 

hosts_path = 'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
websites =['www.facebook.com', 'facebook.com', 'www.google.com', 'google.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Print Working hours')
    else:
        print('Fun hours')
    time.sleep(5)
    