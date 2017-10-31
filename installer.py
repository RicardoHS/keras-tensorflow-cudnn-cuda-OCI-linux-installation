#!/usr/bin/python

import sys, getopt, inspect
import modules
import os
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
* Keras

The following systems are suported:

"""
    body = ""

    for (name, data) in inspect.getmembers(modules,inspect.ismodule):
        if name != 'glob' and name != 'template':
            body += str(counter) + ') ' + str(name) + '\t\t\t' + str(getattr(data,'getDescription')()) + '\n'
            counter +=1
            variables.append(str(name))

    return head + body, variables


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
        except:
            print("No valid index")

    print "Installing for %s"%(installationModules[inpt-1])
    InstallationProcess(installationModules[inpt-1]).install()



if __name__ == "__main__":
    #Check if runing as sudo
    if os.getuid() != 0:
        print "Please, run as sudo."
        sys.exit()

    main()
