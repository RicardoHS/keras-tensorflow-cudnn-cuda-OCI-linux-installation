#!/usr/bin/python

import sys, getopt, inspect
import modules
import os
import subprocess

from modules import *

class InstallationProcess():
	"""Load the code form the respective module and store it"""
	def __init__(self, variable):
		self.variable = variable
		for (name, data) in inspect.getmembers(modules,inspect.ismodule):
			if name == variable:
				self.install = getattr(data,'main')
				self.getDescription = getattr(data,'getDescription')

def getHelpMessage():
    counter=1
    variables = []
    head = """This program will install the last version compatible with your hardware of:
* CUDA
* cudNN
* TensorFlow
* Keras (already in the TensorFlow module)

"""
    body = checkHardware() + """

The following systems are suported:

"""

    for (name, data) in inspect.getmembers(modules,inspect.ismodule):
        if name != 'glob' and name != 'template':
            body += str(counter) + ') ' + str(name) + '\t\t\t' + str(getattr(data,'getDescription')()) + '\n'
            counter +=1
            variables.append(str(name))

    return head + body, variables

def checkHardware():
	vga_nvidia_command="lspci | grep -i '.*vga.*nvidia'"
	vga_command="lspci | grep -i vga"

	p1 = subprocess.Popen(vga_nvidia_command,shell=True,stdout=subprocess.PIPE)
	out = p1.communicate()

	if out[0]:
		message = "Nvidia Graphic Card:\n%s"%(out[0])
	else:
		p1 = subprocess.Popen(vga_command,shell=True,stdout=subprocess.PIPE)
		out = p1.communicate()[0]
		message = "Graphic Card\nWarning, No Nvidia-GPU detected\n%s"%(out)

	return message

def main():
    helpMessage, installationModules = getHelpMessage()
    print helpMessage

    #Get the system installation
    while True:
        try:
            inpt = int(input('Installation option: '))
            if inpt < 1:
                raise IndexError
            foo=installationModules[inpt-1]
            break
        except (IndexError, NameError):
            print("No valid index")

    print "Starting installation for %s\n"%(installationModules[inpt-1])
    InstallationProcess(installationModules[inpt-1]).install()



if __name__ == "__main__":
    #Check if runing as sudo
    if os.getuid() != 0:
        print "Please, run as sudo."
        sys.exit()

    main()
