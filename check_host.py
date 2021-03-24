import sys
import subprocess

if(len(sys.argv) <= 1):
    print("IP address belum diberikan")
else:
    cmd = sys.argv[1]
    status, res = subprocess.getstatusoutput("ping -c1 " + cmd)
    if(status == 0):
        print(f'{cmd} UP')
    else:
        print(f'{cmd} DOWN')
