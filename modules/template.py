import numpy

def main():
    bashCommand = '''
echo "Hello"
'''

    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    return output, error

def getDescription():
	description = "The template of the variables"
	return description
