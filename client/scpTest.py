import time
import paramiko
from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("140.96.115.194",  22, "demo", "demo")

# SCPCLient takes a paramiko transport as its only argument
scp = SCPClient(ssh.get_transport())


def getDnnFile():
    print("Get remote DNN log....")
    scp.get('Happy.txt', 'faceData.txt')
    time.sleep(1)   

while True:
    getDnnFile()


scp.close()


