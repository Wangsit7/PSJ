import subprocess
import sys


if(len(sys.argv) <= 1):
    print("IP address belum diberikan!")
else:
    ping = ['ping', '-c1', sys.argv[1]]
    check = subprocess.check_output(ping)
    if(check):
        print('UP')
    else:
        print('DOWN')
