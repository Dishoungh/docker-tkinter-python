Install Docker Engine and Desktop

1. sudo apt update
2. sudo apt install apt-transport-https ca-certificates curl software-properties-common
3. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
4. sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
5. apt-cache policy docker-ce
6. sudo apt install docker-ce
7. sudo systemctl status docker
8. sudo usermod -aG docker ${USER}
9. su - ${USER}
10. groups
11. sudo apt-get install ca-certificates curl gnupg lsb-release
12. sudo mkdir -p /etc/apt/keyrings
13. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
14. echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
15. sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
16. sudo apt-get install ./docker-desktop-4.15.0-amd64.deb

Start Python Development

1. docker pull ubuntu:20.04
2. docker container run -it --name=sap ubuntu:20.04

This runs a containerized terminal session for Ubuntu 20.04. Install firefox, Python, Python-Pip, and Tkinter
Created DockerFile. See Dockerfile contents.

1. xhost +local:docker
2. docker build -t sample-python-app .
3. sudo docker run -it --rm --env="DISPLAY=$DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" sample-python-app
