'''
Website Blocker for certain times in the day
'''

import time
from datetime import datetime as dt 

hosts_path = 'C:\Windows\System32\drivers\etc\hosts'
hosts_temp = 'hosts'
redirect = '127.0.0.1'
websites =['www.facebook.com', 'facebook.com', 'www.google.com', 'google.com']

'''
Adding sites to hosts file that will block them from being accessed
'''
while True:
    #Compares the current time to the time that you wish to have the sites blocked
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        #opens the host file and check to see if the sites are already printed in the file
        with open(hosts_path, 'r+') as file:
            content = file.read()
            #For each site in the list, if the site is in the file pass otherwise write the site to the list
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect + " " + site + "\n")
    #When not in the time frame remove the sites from the file
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)
    