#!/usr/bin/python3

import os
import time
import sys
import subprocess

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")

print("                 						 `/-          ")
print("                                     .oy-              ")
print("                                   -sd/  `-+o:         ")
print("                              -  -sds../sdh/`          ")
print("                             o+`+hh//shhy/`            ")
print("                            /y-syyoyyyy/`              ")
print("                           -ysyyyyyyy+`                ")
print("                          `syyyyyyyo.                  ")
print("                          /yyyyyys:                    ")
print("                         `syyyyy+`                     ")
print("                      .` :yyyys-                       ")
print("                     `.dhyysso.                        ")
print("                      `+MMmymy. `                      ")
print("                       `NMmhNN- `                      ")
print("                      ``mMmhhNs `                      ")
print("                      `yMMmyhhms.``                    ")
print("                    `/dMMmmyNyhmdo-``                  ")
print("               ` `-smNMMNmmsNNssddhs:.                 ")
print("              `-odNMMMMNhNmsdMNo+hhhhys/. `            ")
print("           `-odNMMMNNNmsdNdhsNNN+/yyyyyyyo-`           ")
print("         `:hNMMNNNNmhsymNNdydoNNN:/yyyyyyyyo-` `       ")
print("      ` -hNMNNNNmhsshmNNNNdyNhomNm.osssssssss+. `      ")
print("     ` +NNNNNNdsshmNNNNNNhdoNNh+mNs-ooooooooooo- `     ")
print("    ` sNNNNNdsydNNNNmmmmhhh/hmmh+mm.+ooooooooooo- `    ")
print("   ` +NNNNNssmNNNmmmmmdhhmhs+dmmssm:-++++++++++++. `   ")
print("    `NNNNN/yNNNmmmmdyyhmmmhsh+dmm/m/`////////+//// `   ")
print("  ` /NNNNo+NNmmmmyoydmddddhsdd/dmoy+ /////////////`    ")
print("    +NNNN.dNmmmd+sdmddddddy+ddy/dyo+ :////////////` `  ")
print("  ` /NNNN.mmmmh/dmddddddyoy+sdd:yy// :::::::::::::`    ")
print("    `mNNN/hmmm:hmddddddo+hys-hdoos+: ::::::::::::-     ")
print("   ` +NNNh:mmd.mmddddds/hhys:sdo++o``------------` `   ")
print("    ` sNNNo+mm.dmddddd-hhhyo+/hoo:s `-----------.      ")
print("     ` omNm+omoodddddd-ddhyso:d/o-/ ...........` `     ")
print("      ` -hmmo/d/oddddd.hddys//d./o` ..........` `      ")
print("       ```/dmy:y+/hdddo/ddys.so::: `.......`` ``       ")
print("          ``:ydo+s:/hddo/hh/.h:.- ````````  ``         ")
print("             ``:+/+o///so//`/-`  ``````   `            ")
print("                `  ``.-. ``        `                   ")
print("                          `  `     				      ")
print("		OnionPi v0.1\n 	by Speed09 - www.speed09.com\n")

print("Welcome to OnionPi!")
conf = input("[?] Do you want to start the setup? (Y/N)\n")

if(conf != "y" and conf != "Y"):
	
	sys.exit("[*] Bye!")
else:

	print("[*] Let's begin!")
	os.system("apt-get update && apt-get upgrade")
	print("[+] Installing Tor")
	os.system("apt-get install tor")
	print("[+] Creating Tor user")
	os.system("adduser tor")
	os.system("echo 'tor ALL=(ALL) ALL' >> /etc/sudoers")
	os.system("echo -n "" > /etc/tor/torrc")
	time.sleep(1)
	os.system("clear")

	print("##### TOR NODE SETUP #####")
	
	conf = ""
	while(conf == ""):
		
		conf = input("[?] Do you want to install a tor relay on your Raspberry Pi? (Y/N)\n")
	
	if(conf != "y" and conf != "Y"):
	
		print("[*] Ok, let's keep going!")
	
		conf = ""
		while(conf == ""):
	
			conf = input("[?] Do you want to install a tor bridge on your Raspberry Pi? (Y/N)\n")
	
		if(conf != "y" and conf != "Y"):
	
			sys.exit("\n\n[!] OnionPi finished it job. Quitting.")
	
		else:
		
			pub = ""
			while(pub == ""):
		
				pub = input("[?] Do you want torproject.org to know your bridge? Y/N")
		
			if(pub == y or pub == Y):
		
				os.system("echo 'PublishServerDescriptor 0' >> /etc/tor/torrc")
		
			os.system("echo 'SocksPort 0' >> /etc/tor/torrc")
			os.system("echo 'BridgeRelay 1' >> /etc/tor/torrc")
			os.system("echo 'Exitpolicy reject *:*' >> /etc/tor/torrc")

	else:
		
		name = ""
		while(name == ""):
			name = input("[?] What name do you want to give to your relay?\n")
		os.system("echo 'Nickname " + name + "' >> /etc/tor/torrc")
		

		band = 0
		while(band == 0):
			band = str(input("[?] How much do you want alocate bandwith to your relay? (in Kb/s)\n"))
		
		os.system("RelayBandwidthRate " + band + " KB' >> /etc/tor/torrc")
		os.system("RelayBandwidthBurst " + band + " KB' >> /etc/tor/torrc")
		os.system("echo 'SocksPort 0' >> /etc/tor/torrc")
		os.system("echo 'Log notice file /var/log/tor/notices.log' >> /etc/tor/torrc")
		os.system("echo 'RunAsDaemon 1' >> /etc/tor/torrc")
		os.system("echo 'ORPort 9001' >> /etc/tor/torrc")
		os.system("echo 'DirPort 9030' >> /etc/tor/torrc")
				
		ex = ""
		while(ex == ""):
		
			ex = input("[?] Do you want to run your relay as an exit relay? (Dangerous for home devices) (Y/N)\n")
		
		if(ex == "Y" or ex == "y"):
		
			os.system("echo 'ExitPolicy accept *:20-23     # FTP, SSH, telnet' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:43        # WHOIS' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:53        # DNS' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:79-81     # finger, HTTP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:88        # kerberos' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:110       # POP3' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:143       # IMAP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:194       # IRC' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:220       # IMAP3' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:389       # LDAP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:443       # HTTPS' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:464       # kpasswd' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:531       # IRC/AIM' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:543-544   # Kerberos' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:554       # RTSP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:563       # NNTP over SSL' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:636       # LDAP over SSL' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:706       # SILC' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:749       # kerberos ' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:873       # rsync' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:902-904   # VMware' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:981       # Remote HTTPS management for firewall' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:989-995   # FTP over SSL, telnets, IMAP over SSL, etc' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1194      # OpenVPN' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1220      # QT Server Admin' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1293      # PKT-KRB-IPSec' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1500      # VLSI License Manager' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1533      # Sametime' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1677      # GroupWise' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1723      # PPTP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1755      # RTSP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1863      # MSNP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:2082      # Infowave Mobility Server' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:2083      # Secure Radius Service (radsec)' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:2086-2087 # GNUnet, ELI' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:2095-2096 # NBX' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:2102-2104 # Zephyr' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:3128      # SQUID' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:3389      # MS WBT' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:3690      # SVN' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:4321      # RWHOIS' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:4643      # Virtuozzo' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:5050      # MMCC' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:5190      # ICQ' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:5222-5223 # XMPP, XMPP over SSL' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:5228      # Android Market' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:5900      # VNC' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:6660-6669 # IRC' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:6679      # IRC SSL  ' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:6697      # IRC SSL  ' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8000      # iRDMI' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8008      # HTTP alternate' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8074      # Gadu-Gadu' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8080      # HTTP Proxies' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8087-8088 # Simplify Media SPP Protocol, Radan HTTP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8332-8333 # BitCoin' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8443      # PCsync HTTPS' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8888      # HTTP Proxies, NewsEDGE' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:9418      # git' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:9999      # distinct' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:10000     # Network Data Management Protocol' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:11371     # OpenPGP hkp (http keyserver protocol)' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:12350     # Skype' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:19294     # Google Voice TCP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:19638     # Ensim control panel' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:23456     # Skype' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:33033     # SkypeExitPolicy accept *:20-23     # FTP, SSH, telnet' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:43        # WHOIS' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:53        # DNS' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:79-81     # finger, HTTP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:88        # kerberos' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:110       # POP3' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:143       # IMAP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:194       # IRC' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:220       # IMAP3' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:389       # LDAP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:443       # HTTPS' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:464       # kpasswd' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:531       # IRC/AIM' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:543-544   # Kerberos' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:554       # RTSP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:563       # NNTP over SSL' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:636       # LDAP over SSL' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:706       # SILC' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:749       # kerberos ' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:873       # rsync' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:902-904   # VMware' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:981       # Remote HTTPS management for firewall' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:989-995   # FTP over SSL, telnets, IMAP over SSL, etc' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1194      # OpenVPN' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1220      # QT Server Admin' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1293      # PKT-KRB-IPSec' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1500      # VLSI License Manager' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1533      # Sametime' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1677      # GroupWise' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1723      # PPTP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1755      # RTSP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:1863      # MSNP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:2082      # Infowave Mobility Server' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:2083      # Secure Radius Service (radsec)' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:2086-2087 # GNUnet, ELI' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:2095-2096 # NBX' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:2102-2104 # Zephyr' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:3128      # SQUID' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:3389      # MS WBT' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:3690      # SVN' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:4321      # RWHOIS' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:4643      # Virtuozzo' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:5050      # MMCC' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:5190      # ICQ' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:5222-5223 # XMPP, XMPP over SSL' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:5228      # Android Market' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:5900      # VNC' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:6660-6669 # IRC' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:6679      # IRC SSL  ' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:6697      # IRC SSL  ' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8000      # iRDMI' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8008      # HTTP alternate' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8074      # Gadu-Gadu' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8080      # HTTP Proxies' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8087-8088 # Simplify Media SPP Protocol, Radan HTTP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8332-8333 # BitCoin' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8443      # PCsync HTTPS' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:8888      # HTTP Proxies, NewsEDGE' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:9418      # git' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:9999      # distinct' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:10000     # Network Data Management Protocol' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:11371     # OpenPGP hkp (http keyserver protocol)' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:12350     # Skype' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:19294     # Google Voice TCP' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:19638     # Ensim control panel' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:23456     # Skype' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy accept *:33033     # Skype ' >> /etc/tor/torrc")
			os.system("echo 'ExitPolicy reject *:*' >> /etc/tor/torrc")
			
		else:
		
			os.system("ExitPolicy reject *:*' >> /etc/tor/torrc")
			

		arm = ""
		while(arm == ""):
			
			arm = input("[?] Do you want to install Tor-Arm to monitor you relay? (Y/N)\n")
		
		if(arm == "Y" or arm == "y"):
		
			os.system("apt-get install tor-arm")
			
		else:
		
			print("[*] You can check your relay logs in the /var/log/tor/ folder.")

		print("[+] Restarting Tor")
		os.system("service tor restart")		

		print("[!] Done! Your Tor Relay is up and running!")

		if(arm == "Y" or arm == "y"):

			print("You can check the status of your Relay by running this command:\nsudo -u debian-tor arm\n")

		verif = ""
		while(verif == ""):

			verif = input("[?] Do you want to configure a Hidden Service on you Raspberry Pi? (Y/N)")

		if(verif == N or verif == n):
			
			sys.exit("[*] Bye !")
		
		else:
			
			os.system("clear")
			print("##### HIDDEN SERVICE SETUP #####")
			
			if(not os.path.exists("/usr/sbin/nginx")):
			
				os.system("apt-get install nginx")
			
			nick = ""
			while(nick == ""):
			
				nick = input("[?] What name do you want to give to your Hidden Service? (One word!!!)\n")

			os.system("mkdir /var/lib/tor/" + nick +"/")
			os.system("mkdir /var/www/" + nick + "/")
			os.system("echo 'HiddenServiceDir /var/lib/tor/" + nick +"/' >> /etc/tor/torrc")
			os.system("echo 'HiddenServicePort 80 127.0.0.1:44480' >> /etc/tor/torrc")
			os.system("cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak")
			proc = subprocess.Popen(['cat /var/lib/tor/' + nick + "/hostname"], stdout=subprocess.PIPE, shell=True)
			(out, err) = proc.communicate()
			os.system("echo 'server {' > /etc/nginx/sites-available/default")
			os.system("echo '    listen       127.0.0.1:44480;' >> /etc/nginx/sites-available/default")
			os.system("echo '    server_name  " + str(out) + ".onion;' >> /etc/nginx/sites-available/default")
			os/system("echo '	 root /var/www/" + nick + "/;")
			os.system("echo '    allow 127.0.0.1;' >> /etc/nginx/sites-available/default")
			os.system("echo '    deny all;' >> /etc/nginx/sites-available/default")
			os.system("echo '    server_tokens off;' >> /etc/nginx/sites-available/default")			
			os.system("echo '    rewrite ^/(.*) http://www." + str(out) +".onion/$1 permanent;' >> /etc/nginx/sites-available/default")
			os.system("echo '}' >> /etc/nginx/sites-available/default")
			os.system("chown debian-tor:debian-tor -R /var/lib/tor/" + nick +"/")
			os.system("chown debian-tor:debian-tor -R /var/www/" + nick + "/")
			
			print("[!] Done! Your Tor Hidden Service is up and running!")
			print("[!] You can access by this URL: " + str(out))
			
			sys.exit("\n\n[!] OnionPi finished it job. Quitting.")
