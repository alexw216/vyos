#!//usr/bin/python
import vymgmt  # Import vymgmt module 
import crendential # Import credential module

crendential.init()  # Initialize the credential global variables

vyos = vymgmt.Router(crendential.host,crendential.username, password=crendential.password, port=22) #instantiate vymgmt router object

vyos.login()  # Router instacne login
vyos.configure() # Router instacne configuration mode

#vyos.set("protocols static route 203.0.113.0/25 next-hop 192.0.2.20")  # Router instacne  set
#vyos.delete("system options reboot-on-panic") # router Instacne delete
r = vyos.run_op_mode_command("show configuration | no-more") # Rrouter instacne show config- operation mode
#r = vyos.run_conf_mode_command("show  | no-more") # Rrouter instacne show config- config mode
print r
#vyos.commit()  # Router instacne commit
#vyos.save()    # Router instacne save 
vyos.exit()    # Router instacne exit 
vyos.logout()  # Router instacne logout
