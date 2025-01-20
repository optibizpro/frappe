#!/bin/bash
set -e

echo "Setting Up System Dependencies..."

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
echo "::group::apt packages"
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
sudo apt update
sudo apt remove mysql-server mysql-client
sudo apt install libcups2-dev redis-server mariadb-client

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
wget -q https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo apt install ./wkhtmltox_0.12.6.1-2.jammy_amd64.deb
=======
install_wkhtmltopdf() {
  wget -q https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
  sudo apt install ./wkhtmltox_0.12.6.1-2.jammy_amd64.deb
}
install_wkhtmltopdf &
echo "::endgroup::"
>>>>>>> 53615bb31040628756ac2b31ed112197ce976581
=======
wget -q https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo apt install ./wkhtmltox_0.12.6.1-2.jammy_amd64.deb
>>>>>>> b4ee936175174b0954ceee845039d7e9c9e808df
=======
wget -q https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb
sudo apt install ./wkhtmltox_0.12.6.1-2.jammy_amd64.deb
>>>>>>> 61099500f6f137a058d07823f121b41b3ad85b02
