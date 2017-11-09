#!/usr/bin/env python3

import boto3
import subprocess

s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

def add_file():
    for bucket in s3.buckets.all():
        print (bucket.name)
        print ("----------------")
        for item in bucket.objects.all():
            print ("\t%s" % item.key)

    bucket = input('\nPlease type in the name of the bucket you wish to choose a file from: ')
    file = input('\nPlease type in the name of the file you wish to copy to the Index page: ')
    file_url = "https://s3-eu-west-1.amazonaws.com/" + bucket + "/" + file

    try:
        for instance in ec2.instances.all():
            print (instance.id, instance.state, instance.public_ip_address)

        cmd = " 'echo \"<img src=" + file_url + " />\" | sudo tee -a  /usr/share/nginx/html/index.html' "
        index = "ssh -i coady91.pem ec2-user@" + instance.public_ip_address + ' ' + cmd

        (status, output) = subprocess.getstatusoutput(index)
        print (output)

    except Exception as error:
        print (error)

# Define a main() function
def main():
    add_file()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()


