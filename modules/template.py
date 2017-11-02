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
            except KeyboardInterrupt:
                response = raw_input('Are you sure you want to exit the installation? (y/N): ')
                if response.upper() == 'Y' or response.upper() == 'YES':
                    raise

def getDescription():
	description = "The template of the variables"
	return description
