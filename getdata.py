from github import Github
from color import *
import re


GITHUB_TOKEN='ghp_7WiEi'
OWNER='raja_tac'
REPO='Android-Spyware'

g = Github(GITHUB_TOKEN)
user = g.get_user()
for repo in user.get_repos():
    prGreen(repo)
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        # prRed(file_content)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            data_file = file_content.decoded_content.decode()
            # prCyan(data_file)
            raw_content = open("raw_content.txt", "w", encoding='unicode_escape', errors='ignore')
            raw_content.write(data_file)
            raw_content.close()

            with open("raw_content.txt", 'r', encoding= 'unicode_escape', errors='ignore') as raw_file_reading:
                scan_keyword=raw_file_reading.readlines()
                for line in scan_keyword:
                    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                    
                if re.search('password =', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print(line)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
            
                if re.search('aws.secret.key', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print(line)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
            
                if re.search('aws.access.key', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print(line)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
            
                if re.search('awsAccessKey', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print(line)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
            
                if re.search('token =', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print(line)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
                
                if re.search('api keys', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print(line)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")

                if re.search('Api_keys', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print(line)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")

                if re.search('user', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
            
                if re.search('pass', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
                
                if re.search('api_key', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")

                if re.search('authorization_bearer', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
                
                if re.search('oauth', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")

                if re.search('auth', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")

                if re.search('authentication', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
                
                if re.search('client_secret', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
                
                if re.search('api_token', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")

                if re.search('DB_DATABASE', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")

                if re.search('DB_HOST', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")

                if re.search('DB_PORT', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
                
                if re.search('DB_PASSWORD', line, re.I):
                    prYellow("Found Sensitive information on this location: "+file_content.path)
                    print("Please refer this link to verify: \n"+data_file)
                    print("---------------------------------------\n")
                    
        
print("Scanning completed")
