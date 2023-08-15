# Install Docker Engine and Desktop

1. sudo apt update
2. sudo apt upgrade
3. sudo apt install apt-transport-https ca-certificates curl software-properties-common gnupg lsb-release
4. sudo mkdir -p /etc/apt/keyrings
5. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add –
6. sudo add-apt-repository “deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable”
7. apt-cache policy docker-ce
8. sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin
9. sudo apt install ./docker-desktop-(VERSION)-amd64.deb (Get .deb from https://docs.docker.com/desktop/install/ubuntu/)
10. sudo systemctl status docker
11. sudo usermod -aG docker ${USER}
12. su - ${USER}
13. groups

# Start Python Development

1. docker pull ubuntu:20.04
2. export DISPLAY=:0
3. xhost +local:docker
4. docker build -t sample-python-app .
5. sudo docker run -it --rm --env=”DISPLAY=$DISPLAY” --env=”QT_X11_NO_MITSHM=1” --volume=”/tmp.X11-unix:/tmp/.X11-unix:rw” sample-python-app
