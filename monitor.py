#!/usr/bin/python
import sys
import os
import time

existing_gw_server_ip = '10.42.32.71'
#server_ip = '8.8.8.8'

try:
    while True:

	rep1 = os.system('ping -c 4 -W 1 ' + existing_gw_server_ip)
	if rep1 == 0:
		print 'The server is up '
                print 'You can interrupt this monitor script at this moment with CTRL+C'
                time.sleep(1)
 	else:
		print 'The server is down'
        	print 'Shutting down existing vyos router'
		os.system('python shutdown_vm.py')  
        	print 'auto config backup vyos router'
		os.system('python auto_config_vyos.py')
                time.sleep(5)
        	rep2 = os.system('ping -c 4 -W 1 ' + existing_gw_server_ip)
        	if rep2 == 0:
			print 'The backup vyos router is ready'
		else: 
			print 'the backup vyos router is not ready'	  
              
except KeyboardInterrupt:
    print('interrupted!')
