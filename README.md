# WIP - Work In Progress
Currently, Tensorflow doesnt support CUDA9, so CUDA8 and cudNN6 is needed for the newest installations.

More info: https://github.com/tensorflow/tensorflow/issues/12052

TODO list (you can contribute):
* ~~Modular script for diferent distros support~~
* Hardware detection
* Info about witch hardware suports witch CUDA and cudNN versions
* Concurrent info on the bash commands
* ~~Ubuntu 16.04 and 14.04 modules~~
* ~~Unistall script (if something goes wrong)~~ (see below)

# keras-tensorflow-cudnn-cuda-OCI-linux-installation
One-Click-Installation script and configuration for any suported linux distribution.

This will install and configure:
* nvidia-CUDA
* nvidia-cudNN
* TensorFlow

Keras is already in the TensorFlow module. You can use it with `tf.keras`
 
Suported distros:
* Ubuntu 16.04
* Ubuntu 14.04

If you want a specific distro installation, open a [new issue](https://github.com/RicardoHS/keras-tensorflow-cudnn-cuda-OCI-linux-installation/issues/new) and I will try to implement it.

# Contribute
You can contribute to the project adding modules to the Linux distro version you want, just copy-paste the template with the name you want, add bash commands to the `bashCommand` variable and [Pull Request](https://help.github.com/articles/about-pull-requests/).

Comments, Issues and Forks are welcome.

## links

tensorflow instructions https://www.tensorflow.org/install/

CUDA instructions http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4VZnqTJ2A

cudNN instructions http://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html

graphic cards compute capability https://developer.nvidia.com/cuda-gpus

CUDA download links https://developer.nvidia.com/cuda-toolkit-archive

cudNN download links (you need to create a developer account) https://developer.nvidia.com/cudnn

keras instructions https://keras.io/#installation

## Unistall Cuda
### Instructions from nvida web
```

To uninstall the CUDA Toolkit, run the uninstallation script provided in the bin directory of the toolkit. By default, it is located in /usr/local/cuda-9.0/bin:

$ sudo /usr/local/cuda-9.0/bin/uninstall_cuda_9.0.pl

To uninstall the NVIDIA Driver, run nvidia-uninstall:

$ sudo /usr/bin/nvidia-uninstall

To enable the Nouveau drivers, remove the blacklist file created in the Disabling Nouveau section, and regenerate the kernel initramfs/initrd again as described in that section.

Read more at: http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#ixzz4xquMpi4V
Follow us: @GPUComputing on Twitter | NVIDIA on Facebook
```

### Instructions if you have installed via package mannager

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
