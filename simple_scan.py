import socket
import sys

if len(sys.argv) < 2:
    print('\n Use: python3 simple_scan.py [IP]')
    exit(1)

ports = [21, 22, 80, 8080, 443, 53, 3306, 3389]

for i in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    try:
        response = client.connect_ex((sys.argv[1], i))
        if response == 0:
            print('PORT: ' + str(i) + ' OPEN')
    except:
        print('[ERROR] HOST NOT FOUND')
        exit(1)