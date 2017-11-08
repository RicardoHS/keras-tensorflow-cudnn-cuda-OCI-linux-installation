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

kk contains all the autocomplete string (double tab) of ```sudo dpkg -P cuda```
```
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
for i in $(cat kk); do sudo dpkg -P $i ;done 
```

## Installation Problems

### On importing Tensorflow
If you see this message on `import tensorflow`
``` 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/__init__.py", line 24, in <module>
    from tensorflow.python import *
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/__init__.py", line 49, in <module>
    from tensorflow.python import pywrap_tensorflow
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/pywrap_tensorflow.py", line 52, in <module>
    raise ImportError(msg)
ImportError: Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/pywrap_tensorflow.py", line 41, in <module>
    from tensorflow.python.pywrap_tensorflow_internal import *
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 28, in <module>
    _pywrap_tensorflow_internal = swig_import_helper()
  File "/usr/local/lib/python2.7/dist-packages/tensorflow/python/pywrap_tensorflow_internal.py", line 24, in swig_import_helper
    _mod = imp.load_module('_pywrap_tensorflow_internal', fp, pathname, description)
ImportError: libcudnn.so.5: cannot open shared object file: No such file or directory


Failed to load the native TensorFlow runtime.

See https://www.tensorflow.org/install/install_sources#common_installation_problems

for some common reasons and solutions.  Include the entire stack trace
above this error message when asking for help.
```
Means that you Tensorflow version uses a different version of cudNN, check the line:

> ImportError: **libcudnn.so.5**: cannot open shared object file: No such file or directory

And install the cudNN version that the number said (in this case, cudNN version 5 for CUDA 8)
