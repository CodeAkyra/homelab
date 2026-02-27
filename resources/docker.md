# HOW NOT TO DOCKER

## Install Docker on Ubuntu
>[!TIP]
>Start Clean! `sudo apt update && sudo apt upgrade`

>sudo apt update && sudo apt upgrade
>
>sudo apt install -y docker.io docker-compose
>
>sudo usermod -aG docker $USER
>
>newgrp docker
>
>docker --version
>
>docker-compose --version

##  Directory Setup
Create docker project directory

>[!NOTE]
>Name your project directory whatever you want it.
>I named my directory `vuln_docker` to create a dedicated penetration testing environment for our capstone project with intentional security vulnerabilities.

>cd ~
>
>mkdir vuln_docker
>
>cd vuln_docker

## Docker Configuration Files
>[!NOTE]
>I uploaded my docker config files here at configs, feel free to modify it.

>move the `Dockerfile` and `docker-compose.yml` inside the Docker project directory you created.

## Clone your repo

>mkdir app
>
>cd app
>
>git clone <your_repo>

## Start Docker Container

>Inside the `vuln_docker`, enter command `docker-compose up -d`
>
>Verify if containers are running by entering `docker-compose ps`  
