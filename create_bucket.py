#!/usr/bin/env python3

import sys
import boto3
import json

# Declaring S3 variable
s3 = boto3.resource("s3")

# Creates a new bucket
def create_bucket():

    print ('\nCreating a new bucket')
    # Ask the user to give the new bucket a name
    bucketname = input('Please give your new bucket a unique name: ')

    # try/except so the script will not crash
    try:
        response = s3.create_bucket(Bucket = bucketname, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
        print ('\nA new bucket has been created')
        print (response)

        # Adds Read-Only permissions to an Anonymous User
        # http://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-2
        print ('Adding Read-Only Permissions')
        policy = {
            "Version":"2012-10-17",
            "Statement":[
                {
                    "Sid":"AddPerm",
                    "Effect":"Allow",
                    "Principal": "*",
                    "Action":["s3:GetObject"],
                    "Resource":["arn:aws:s3:::" + bucketname + "/*"]
                }
            ]
        }

        # The bucket policy as a JSON document
        # http://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.BucketPolicy.policy
        # https://stackoverflow.com/questions/7408647/convert-dynamic-python-object-to-json
        policy = json.dumps(policy)

        # Add Read-Only Permissions to new bucket
        # http://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-policy.html
        boto3.client('s3').put_bucket_policy(Bucket = bucketname, Policy = policy)
        print ('Read-Only Permissions added to ' + bucketname)

    except Exception as error:
        print (error)

# Define a main() function
def main():
    create_bucket()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()

