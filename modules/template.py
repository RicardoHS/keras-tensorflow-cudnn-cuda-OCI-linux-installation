from __future__ import print_function
import subprocess

def main():
    bashCommand = '''
echo "Hello"
'''

    #Execute the program
    for proc in bashCommand.split('\n'):
        #If proc is not empty
        if proc:
            print(proc.split())
            try:
                process = subprocess.Popen(proc, stdout=subprocess.PIPE, shell=True)
                output, error = process.communicate()
            except OSError as e:
                print(e)
                break

def getDescription():
	description = "The template of the variables"
	return description
