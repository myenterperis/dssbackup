import os
import ftplib

# create DATABSE BACKUP
password = 'R@@tmotech2023'
os.system('mysqldump -u root -p%s --all-databases > database.sql' % password)

# send backup to FTO server
session = ftplib.FTP('192.168.4.65', 'ftpuser', 'ftpuser')
file = open('database.sql', 'rb')
session.storbinary('STOR databse.sql', file)
file.close()
session.quit()
