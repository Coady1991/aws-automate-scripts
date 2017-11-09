#!/usr/bin/env python3

import boto3
import subprocess

# Declaring EC2 variable
ec2 = boto3.resource('ec2')

try:
    # Retriving a List of instances
    for instance in ec2.instances.all():
        print (instance.id, instance.state, instance.public_ip_address)

    cmd = "ssh -i coady91.pem ec2-user@" + instance.public_ip_address + " 'python3 check_webserver.py'"

    (status, output) = subprocess.getstatusoutput(cmd)
    print (output)

except Exception as error:
    print (error)
