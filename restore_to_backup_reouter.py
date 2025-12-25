#!//usr/bin/python

import vymgmt  # Import vymgmt module 

import crendential # Import credential module

crendential.init()  # Initialize the credential global variables

publicInterfaceIpAddress=['150.70.196.17/24','150.70.196.18/24','150.70.196.19/24','150.70.196.20/24','150.70.196.21/24','150.70.196.22/24','150.70.196.23/24','150.70.196.24/24','150.70.196.25/24']  # array of public interfaces

system_gateway_address='150.70.196.1'

nat_Exclude_CIDR=['10.0.0.0/8','150.70.0.0/16']

nat_translate_addresses=['150.70.196.182/24','150.70.196.183/24']

nat_source_address='10.42.32.0/24'

nat_translate_range='150.70.196.17-150.70.196.25'

original_private_gw_address='10.42.32.71/24'

vyos = vymgmt.Router(crendential.host,crendential.username, password=crendential.password, port=22) #instantiate vymgmt router object

vyos.login()  # Router instacne login

vyos.configure() # Router instacne configuration mode

def set_public_interface_ip(str):   #function to set public interface
        for i in str:
                vyos.set("interface ethernet eth0 address " + i)
        return

def set_system_gateway_address(str):   #function to set system gateway
        vyos.set("system gateway-address " + str)
	return

def set_source_nat_exclude_address(address):   #function to set Source NAT Exclusion
        n=210
        for i in address:
        	vyos.set("nat source rule " + str(n) + " " + "exclude")
        	vyos.set("nat source rule " + str(n) + " " + "outbound-interface eth0")
        	vyos.set("nat source rule " + str(n) + " " + "description" + " " +  '"' + "Source NAT Exclusion for Trend Micro " + i + " network" + '"')
        	vyos.set("nat source rule " + str(n) + " " + "source address " + nat_source_address)
        	vyos.set("nat source rule " + str(n) + " " + "destination address " + i)
                n=n+10 
        return


def set_source_nat(address, range):        #function to set source nat
        n=310
	vyos.set("nat source rule " + str(n) + " " + "outbound-interface eth0")
	vyos.set("nat source rule " + str(n) + " " + "description" + " " +  '"' + "Source NAT for " + address + " network" + '"')
        vyos.set("nat source rule " + str(n) + " " + "log enable ")
        vyos.set("nat source rule " + str(n) + " " + "source address " + address)
        vyos.set("nat source rule " + str(n) + " " + "translation address " + range)
        return        

def set_original_gw_address(address):
	vyos.set("interface ethernet eth1 address " + address)
	return

def delete_nat():
        vyos.delete("nat")
	return

def delete_original_private_gw_address(address):
	vyos.delete("interface ethernet eth1 address " + address)
        return 


def delete_public_interface_ip(str):
	for i in str:
                vyos.delete("interface ethernet eth0 address " + i)
        return

#vyos.set("interface ethernet eth0 address 150.70.196.182/24")  # Router instacne  set
#vyos.delete("system options reboot-on-panic") # router Instacne delete

#set_public_interface_ip(publicInterfaceIpAddress)

#set_system_gateway_address(system_gateway_address)  #already exist, so comment out

#set_source_nat_exclude_address(nat_Exclude_CIDR)

#set_source_nat(nat_source_address, nat_translate_range)

#set_original_gw_address(original_private_gw_address)


delete_nat()
delete_original_private_gw_address(original_private_gw_address)
delete_public_interface_ip(publicInterfaceIpAddress)

vyos.commit()  # Router instacne commit
vyos.save()    # Router instacne save 

#r = vyos.run_op_mode_command("show configuration | no-more") # Rrouter instacne show config- operation mode
#r = vyos.run_conf_mode_command("show  | no-more") # Rrouter instacne show config- config mode
#print r

vyos.exit()    # Router instacne exit 

vyos.logout()  # Router instacne logout

