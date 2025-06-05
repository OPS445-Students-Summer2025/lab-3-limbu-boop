#!/usr/bin/env python3
# Author ID: 174495234

import subprocess

def free_space():
    # Run the command df -h | grep '/$' | awk '{print $4}'
    # This shows available disk space on root directory
    
    # Use subprocess to run the shell command
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         shell=True)
    
    output, errors = p.communicate()
    
    # Decode bytes to string and strip newlines
    free = output.decode('utf-8').strip()
    
    return free

if __name__ == '__main__':
    print(free_space())

