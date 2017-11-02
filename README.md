# WIP - Work In Progress
Currently, Tensorflow doesnt support CUDA9, so CUDA8 and cudNN6 is needed for the newest installations.

More info: https://github.com/tensorflow/tensorflow/issues/12052

TODO list (you can contribute):
* ~~Modular script for diferent distros support~~
* Hardware detection
* Info about witch hardware suports witch CUDA and cudNN versions
* Concurrent info on the bash commands
* ~~Ubuntu 16.04 and 14.04 modules~~
* Unistall script (if something goes wrong)

# keras-tensorflow-cudnn-cuda-OCI-linux-installation
One-Click-Installation script and configuration for any suported linux distribution.

This will install and configure:
* nvidia-CUDA
* nvidia-cudNN
* TensorFlow
* Keras

Suported distros:
* Ubuntu 16.04
* Ubuntu 14.04

If you want a specific distro installation, open a [new issue](https://github.com/RicardoHS/keras-tensorflow-cudnn-cuda-OCI-linux-installation/issues/new) and I will try to implement it.

# Contribute
You can contribute to the project adding modules to the Linux distro version you want, just copy-paste the template with the name you want, add bash commands to the `bashCommand` variable and [Pull Request](https://help.github.com/articles/about-pull-requests/).

Comments, Issues and Forks are welcome.

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
