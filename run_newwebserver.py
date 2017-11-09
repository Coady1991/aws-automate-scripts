#!/usr/bin/env python3

import boto3
import time
import subprocess

# Declaring EC2 variable
ec2 = boto3.resource('ec2')

# Creates a new instance
def create_instance():
    # Ask the user to give the new instance a name
    instancename = input('Please give your new instance a name: ')
    tags = [{'Key': 'Name', 'Value': instancename}]
    tag_spec = [{'ResourceType': 'instance', 'Tags': tags}]

    # try/except so the script will not crash
    try:
        instance = ec2.create_instances(
        ImageId = 'ami-acd005d5',
        MinCount = 1,
        MaxCount = 1,
        InstanceType = 't2.micro',
        KeyName = 'coady91',
        TagSpecifications = tag_spec,
        SecurityGroupIds = ['sg-9e143de6'],
        # UserData that will be executed on creation of the instance
        UserData = '''#!/bin/bash
                      yum -y update
                      yum -y install python35
                      yum -y install nginx
                      service nginx start
                      chkconfig nginx on
                      touch home/ec2-user/testFile''')

        print ("An EC2 instance with ID", instance[0].id, "has been created.")
        time.sleep(5)
        instance[0].reload()
        print ("Public IP address:", instance[0].public_ip_address)

        # Suppress the new host key confirmation prompt and allow SSH remote command execution
        cmd = "ssh -o StrictHostKeyChecking=no -i coady91.pem ec2-user@" + instance[0].public_ip_address + " 'pwd'"
        time.sleep(60)
        (status, output) = subprocess.getstatusoutput(cmd)
        print (output)

        # SCP the check_webserver.py file to the instance
        cmd_scp = "scp -i coady91.pem /home/coady/devops-assignment/check_webserver.py ec2-user@" + instance[0].public_ip_address + ":."
        (status, output) = subprocess.getstatusoutput(cmd_scp)
        print (output)

    except Exception as error:
        print (error)



# Define a main() function
def main():
    create_instance()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
