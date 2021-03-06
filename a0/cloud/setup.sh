# #!/bin/bash
# 
set -x
# 
# # Don't download stuff to the git repo, that's messy.
pushd ${HOME}
# 
# Update packages
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install bzip2

ANACONDA_INSTALLER="Anaconda3-5.1.0-Linux-x86_64.sh"
wget "https://repo.continuum.io/archive/$ANACONDA_INSTALLER"
bash "$ANACONDA_INSTALLER"

source ${HOME}/.bashrc

# TF_BINARY_URL="https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.4.1-cp36-cp36m-linux_x86_64.whl"
TF_BINARY_URL="https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.8.0-cp36-cp36m-linux_x86_64.whl"
${HOME}/anaconda3/bin/pip install --upgrade pip
${HOME}/anaconda3/bin/pip install $TF_BINARY_URL
${HOME}/anaconda3/bin/jupyter notebook --generate-config

# Downgrade numpy to remove the annoying but harmless warning message "FutureWarning: Conversion..."
pip install numpy==1.13.3

# Copy Jupyter config
popd
mkdir ${HOME}/.jupyter
cp -v $(dirname $0)/support/jupyter_notebook_config.py ${HOME}/.jupyter/jupyter_notebook_config.py
