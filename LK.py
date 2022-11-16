import os

import requests

import time

import uuid

logo= """

\033[1;37m  .d8b.  db   dD d888888b d8b   db  d888b

 d8' `8b 88 ,8P'   `88'   888o  88 88' Y8b

 88ooo88 88,8P      88    88V8o 88 88       \033[1;34mP\033[1;37m

 88~~~88 88`8b      88    88 V8o88 88  oooo\033[1;31m R\033[1;37m

 88   88 88 `88.   .88.   88  V888 88. ~8~  \033[1;35mO\033[1;37m

 YP   YP YP   YD Y888888P VP   V8P  Y888P

----------------------------------------------

 Author    : IMTIAZ AKING

 Github    : AKING110

 Facebook  : MR.AKING.07                           Tool Name : AKING-PRO

 Type type : PAID

 Version   : 1.8.0                                ----------------------------------------------     AKING Pro version 1.8.0

 For Haters: Tumhare Okat Nhi Barabari Karna Ke ðŸ¤ž

----------------------------------------------"""

os.system('termux-setup-storage')

def lpol():

	print("")	input("""\033[1;37m [1] Start Cloning V1.8.0

 [2] Start Cloning V1.7.5

\033[1;37m [0] Exit menu

 Choose: """)

	time.sleep(3)

	print ("")

	print ("""install modules...                                It will take some seconds...""")

	os.system('xdg-open https://www.facebook.com/majid.afridi.5680')

	time.sleep(6)

	print("")

	print("""[\033[1;34mnotice\033[1;37m] A new release of pip available: \033[1;31m22.3 -> \033[1;32m22.3.1                        \033[1;37m                     [\033[1;34mnotice\033[1;37m] To update, run: \033[1;32mpip install --upgrade pip\033[1;37m""")

	time.sleep(2)

	print("")

	print("Checking updates...")

	time.sleep(2)

	open('/sdcard/LKING.txt' , 'a').write('')

	time.sleep(2)

	os.system('clear')

	print(logo)

	login()

def login():

	imt="xMEU9PQ=="

	ak="QUtJTkctWxMDQ"

	try:

		key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()

	except IOError:

		myid=uuid.uuid4().hex[:17].upper()

		print("""\033[1;31mFirst Read Note :

\33[1;36mWe Not Responsible if facebook

go on update you not get ok idz

We don't responsible if you delete your

termux and key need approve""")

		print("\033[1;37m----------------------------------------------")

		print('\033[1;31mYour Key not Registered')

		print ("\033[1;37mYour Key : "+ak+myid+imt)

		print("\033[1;37m----------------------------------------------")

		kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')

		kok.write(myid+imt)

		kok.close()

	r1= open('/sdcard/LKING.txt', 'r').read()

	if key1 in r1:

		paid()

	else:

		print('\033[1;31mYour Key not Registered')

		print ("\033[1;37mYour Key : "+ak+key1)

		print("""----------------------------------------------

Tools.. : Facebook Cloning

Massage : Your Key Not Registered

Status  :\033[1;31m Trail

\x1b[97m\033[31;42m Note: If You Are Free User Don't Come IB \033[0;m""")

		loll()

		input('Choose Option : ')

def loll():

	print("""\033[1;37m----------------------------------------------

[+] File crack

[+] Create ids file

[+] Public crack

[+] Random number crack\033[1;37m

[+] Random gmail crack

[+] Exit menu

[1] Upgrade Tool To (\033[1;35mPremium\033[1;37m)

----------------------------------------------""")

os.system('clear')

def paid():

	os.system('clear')

	print(logo)

	time.sleep(3)

	print("""[1] File cloning

[2] Create ids file                               [3] Public cloning

[4] Random number cloning

[5] Random gmail crack                            [6] WhatsApp Group (join)                         [7] Download Vpn                                  [8] How To Use Video

[0] Exit menu

----------------------------------------------""")

	input (" Choose an option: ")

	print(" Option not found in menu...")

lpol()
