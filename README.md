# Pink

Pi Ink frame based on Wareshare ePaper

## Install

```shell
# Dependencies
sudo apt update && sudo apt upgrade -y
sudo apt-get install -y \
  autoconf \
  automake \
  Build-essentisl \
  cmake \
  g++ \
  gettext \
  libncurses5-dev \
  libtool \
  libtool-bin \
  libunibilium-dev \
  libunibilium4 \
  ninja-build \
  pkg-config \
  python3-pip \
  software-properties-common \
  unzip

pip3 install setuptools
pip3 install --upgrade pynvim

# This project
git clone https://github.com/zhangtai/pink.git
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Development

Because most of the test need to be done on the Pi, the model I am using is not very powerful to run remote VSCode, so a VIM editor IDE setup is required.

### Neovim and LunarVim

First install Neovim as [official instruction](https://github.com/neovim/neovim/wiki/Building-Neovim).

```shell
# Or install the release code instead of clone whole project
git clone https://github.com/neovim/neovim
make CMAKE_BUILD_TYPE=RelWithDebInfo
sudo make install
```

