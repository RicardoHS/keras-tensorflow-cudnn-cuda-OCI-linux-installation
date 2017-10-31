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

export CUDA_HOME=/usr/local/cuda-8.0/
export LD_LIBRARY_PATH=${CUDA_HOME}lib64
PATH=${CUDA_HOME}/bin:${PATH}
export PATH

#the following line doesnt work, download manually
echo "Now go to https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v6/prod/8.0_20170307/cudnn-8.0-linux-x64-v6.0-tgz and download the file. Save in"
path=$(pwd)
pwd
echo "and press enter."
read
while [ ! -f $path"/cudnn-8.0-linux-x64-v6.0.tgz" ]
do
  echo "the file $path\"cudnn-8.0-linux-x64-v6.0.tgz\" does not exists"
  read
done

tar -zxvf cudnn-8.0-linux-x64-v6.0.tgz

cp cuda/include/* $CUDA_HOME"/include/"
cp cuda/lib64/* $CUDA_HOME"/lib64/"

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
			except OSError as e:
				print(e)
				break

def getDescription():
	description = "CUDA 8.0 - cudNN 6.0 - TensorFlow (master) - Keras (master)"
	return description
