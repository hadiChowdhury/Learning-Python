import os

#speciy the  directory path
directory_path = '/'

contents = os.listdir(directory_path)

for content in contents:
    print(content)