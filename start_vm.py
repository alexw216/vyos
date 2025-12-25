#!/usr/bin/env python
"""
vSphere Python SDK program for shutting down VMs
"""
from __future__ import print_function

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl

import argparse
import atexit
import getpass
import sys
import ssl
import vccredential

vccredential.init()

def main():
    """
   Simple command-line program for shutting down virtual machines on a system. 
   """


    service_instance = None
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    context.verify_mode = ssl.CERT_NONE   

    try:
        service_instance = SmartConnect(host=vccredential.host,
                                                user=vccredential.username,
                                                pwd=vccredential.password,
                                                port=vccredential.port,
                                                sslContext=context)
        if not service_instance:
            print("Could not connect to the specified host using specified "
                  "username and password")
            return -1

        atexit.register(Disconnect, service_instance)

        content = service_instance.RetrieveContent()
        # Search for all VMs
        objview = content.viewManager.CreateContainerView(content.rootFolder,
                                                          [vim.VirtualMachine],
                                                          True)
        vmList = objview.view
        objview.Destroy()
 
        for vm in vmList:
            if (vm.name == 'vyos-1.1.8-amd64'):
                print("Starting VM: %s" % vm.name)
                vm.PowerOn()
	    else:
              pass

    except vmodl.MethodFault as error:
        print("Caught vmodl fault : " + "error to shutdown VM" + " " + vm.name)
        return -1

    return 0

# Start program
if __name__ == "__main__":
    main()
