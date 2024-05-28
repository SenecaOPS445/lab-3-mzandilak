#!/usr/bin/env python3

# Author ID: mzandilak


import subprocess

def free_space():
    # Start a subprocess that runs linux command to check available disk spacw
    free_space = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    output = free_space.communicate()
    
    # Convert stdout to a string and strip off the newline characters
    stdout = output[0].decode('utf-8').strip()
    
    # Return the processed stdout
    return stdout

if __name__ == '__main__':
    # Print free disk space
    print(free_space())
