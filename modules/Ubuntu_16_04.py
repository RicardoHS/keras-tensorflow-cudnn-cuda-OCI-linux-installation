from __future__ import print_function
import subprocess

def main():
	bashCommand = '''
wget https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb
mv cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb

dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb
apt-get update
apt-get -y install cuda

rm cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb

echo "Now go to https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v6/prod/8.0_20170307/cudnn-8.0-linux-x64-v6.0-tgz and download the file and save it in $(pwd)"

while [ ! -f $(pwd)"/cudnn-8.0-linux-x64-v6.0.tgz" ];do sleep 1; done
echo "Installing cudNN"

tar -zxvf cudnn-8.0-linux-x64-v6.0.tgz

cp cuda/include/* "/usr/local/cuda-8.0/include/"
cp cuda/lib64/* "/usr/local/cuda-8.0/lib64/"

apt-get install libcupti-dev

apt-get install -y python-pip python-dev
pip install --upgrade pip

pip install tensorflow-gpu
pip install h5py

pip install keras
'''
	#Execute the program
	for proc in bashCommand.split('\n'):
		#If proc is not empty
		if proc:
			print(proc.split())
			try:
				process = subprocess.Popen(proc, stdout=subprocess.PIPE, shell=True)
				output, error = process.communicate()
				print(output,end='')
				if error:
					sys.exit()
			except OSError as e:
				print(e)
				break
			except KeyboardInterrupt:
				response = raw_input('Are you sure you want to exit the installation? (y/N): ')
				if response.upper() == 'Y' or response.upper() == 'YES':
					raise

	end_message='''\n\nInstallation have finished, dont forget to run:
			export CUDA_HOME=/usr/local/cuda-8.0/
			export LD_LIBRARY_PATH=${CUDA_HOME}lib64
			export ${CUDA_HOME}/bin:${PATH}'''

	print(end_message)

def getDescription():
	description = "CUDA 8.0 - cudNN 6.0 - TensorFlow (master) - Keras (master)"
	return description
