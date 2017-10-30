# WIP - Work In Progress
Currently, Tensorflow doesnt support CUDA9, so CUDA8 and cudNN6 is needed.

Things to add:
* Modular script for diferent distros
* Ubuntu 16.04 and 14.04 modules
* Unistall script (if something goes wrong)

## links

https://www.tensorflow.org/install/

https://keras.io/#installation

CUDA instructions http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4VZnqTJ2A

cudNN instructions http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html

graphic cards compute capability https://developer.nvidia.com/cuda-gpus

CUDA download links https://developer.nvidia.com/cuda-toolkit-archive

cudNN download links (you need to create a developer account) https://developer.nvidia.com/cudnn


# keras-tensorflow-cudnn-cuda-OCI-linux-installation
One-Click-Installation script and configuration for any suported linux distribution.

This will install and configure:
* nvidia-CUDA
* nvidia-cudNN
* TensorFlow
* Keras

The script will perform the following actions.
```
mkdir nvidia_GC_installation_file
cd nvidia_GC_installation_file/

wget https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb
mv cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb 
sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb 
sudo apt-get update
sudo apt-get install cuda

sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb 
sudo apt-get update
sudo apt-get install cuda
export CUDA_HOME=/usr/local/cuda-8.0/
export LD_LIBRARY_PATH=${CUDA_HOME}lib64 
PATH=${CUDA_HOME}/bin:${PATH} 
export PATH 

#the following line doesnt work, download manually
wget https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v6/prod/8.0_20170307/cudnn-8.0-linux-x64-v6.0-tgz

tar -zxvf cudnn-8.0-linux-x64-v6.0.tgz 

cp cuda/include/* $CUDA_HOME"/include/"
cp cuda/lib64/* $CUDA_HOME"/lib64/"

sudo apt-get install libcupti-dev

sudo apt-get install python-pip python-dev
sudo pip install --upgrade pip

sudo pip install tensorflow-gpu
sudo pip install h5py

sudo pip install keras

```

## Unistall Cuda
```
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
```
