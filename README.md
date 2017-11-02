# WIP - Work In Progress
Currently, Tensorflow doesnt support CUDA9, so CUDA8 and cudNN6 is needed for the newest installations.

Things to add:
* Modular script for diferent distros
* ~~Ubuntu 16.04~~ and 14.04 modules
* Unistall script (if something goes wrong)

# keras-tensorflow-cudnn-cuda-OCI-linux-installation
One-Click-Installation script and configuration for any suported linux distribution.

This will install and configure:
* nvidia-CUDA
* nvidia-cudNN
* TensorFlow
* Keras

## links

tensorflow instructions https://www.tensorflow.org/install/

keras instructions https://keras.io/#installation

CUDA instructions http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4VZnqTJ2A

cudNN instructions http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html

graphic cards compute capability https://developer.nvidia.com/cuda-gpus

CUDA download links https://developer.nvidia.com/cuda-toolkit-archive

cudNN download links (you need to create a developer account) https://developer.nvidia.com/cudnn

## Unistall Cuda
kk contains all the autocomplete string (double tab) of ```sudo apt-get purge cuda```
```
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
```
