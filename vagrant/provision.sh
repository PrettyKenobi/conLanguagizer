# Setup for a clean bionic64 vm
# By PrettyKenobi

# Update apt cache
apt-get update

# Install packages
PKGS="build-essential libssl-dev git vim zsh"

apt-get install -y "${PKGS[@]}"

# Grab nvm repo for installing Node.js
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
source ~/.bashrc

# Install latest Node.js (as of 24/4/20)
nvm install v12.16.2

# Install yarn
cd /project
npm install yarn
