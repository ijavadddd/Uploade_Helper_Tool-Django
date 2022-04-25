import requests
import argparse

##Detail of project and help ...
parser = argparse.ArgumentParser(
    prog = 'Upload Helper Tool - Client edition',
    description='Upload fast & easy in your server.',
    epilog = 'May enjoy our app',
    add_help = True)

# Add argument to get file for upload
parser.add_argument("-f","--file", help='address of file you want upload.')

args = parser.parse_args()

# The URL of the site we gonna upload file thier
uploadURL = 'http://127.0.0.1:8000/api/new/'

file = args.file    # File You set in command
test_response = requests.post(uploadURL, files = {"file": open(file, "rb")})

if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
else:
    print(test_response)