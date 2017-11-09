# DevOps Assignment Specification

The overall objective of this assignment is to automate using Python 3 the process of creating, launching and monitoring a public-facing web server in the Amazon cloud. The web server will run on an EC" instance and display some static content that is stored in S3.

### Details:

#### run_newwebserver.py
* Creates and launches a new Amazon EC2 micro instance.
* Uses the boto3 API library.
* Launches into the appropriate security group (Hard-coded).
* Provides _"User Data"_ start-up script when creating instance.
    * Installs required patches.
    * Installs python35.
    * Installs Nginx webserver and starts it.
* Secure copies the __check_webserver.py__ file to the instance.

#### check_webserver.py
* Checks to see if Nginx is running and starts it if it is not.

#### create_bucket.py
* Creates an S3 bucket with a unique name.
*  Adds Read-Only Permissions to the bucket.

#### put_bucket.py
* Secure copies a file to a bucket.
* Adds Public Read Only Access to the file.

#### add_file.py
* Appends a file url to the index.html page of the Nginx webserver.
* This can be then viewed by going to the instance ip address.

#### menu.py
* User friendly menu used to run the scripts.

### Running the Scripts:
Before starting the __KeyName__ and __SecurityGroupsIds__ must be changed in the __run_newwebserver.py__ to the users credentials (pem file) or else the script will not work. The Secure Copy command folder location must also be changed to allow copying of files to the instance. This will also affect the SSH commands and pem file name will have to be changed here to.

In the __put_bucket.py__ script the source folder must be changed.

To kick off the program run the command __./menu.py__ from the file location in the terminal.

