#!/usr/bin/env python
import ntplib
import time
import mysql.connector
import datetime
import sys
import subprocess
 

dbcon = mysql.connector.connect(host="localhost",user="txmanager",passwd="Avoka0nly!",db="txmanager")


thecommand = '''cut -d" " -f 1'''
getIP = subprocess.Popen(('hostname', '-I'), stdout=subprocess.PIPE) 
output = subprocess.check_output(thecommand, shell=True, stdin=getIP.stdout)
print(output)

dbcurCTE = dbcon.cursor()
sql_cmd = "UPDATE txmanager.portal SET context_path = REPLACE(context_path, 'localhost', '" + output + "') WHERE context_path LIKE '%localhost%';"
sql_cmd = sql_cmd.replace('\n', '')
print repr(sql_cmd)
dbcurCTE.execute(sql_cmd)
dbcurCTE.close()
dbcon.commit()
dbcon.close()

with open('/usr/share/nginx/html/scripts/ip.js', 'w') as the_file:
    interim1 = 'var local_ip = "'
    interim3 = '";'
    linetowrite = interim1 + output + interim3
    linetowrite = linetowrite.replace('\n', '')
    print(linetowrite)
    the_file.write(linetowrite)