import os
from fabric import Connection

cd_host = os.environ["CD_HOST"]

try:
    Connection(cd_host).run('docker-compose -f ./docker-compose-prod.yml down')
except:
    print("Stack not created")


Connection(cd_host).run('export DEBIAN_FRONTEND=noninteractive')
Connection(cd_host).run('sudo apt update')
Connection(cd_host).run('sudo apt upgrade -y')
Connection(cd_host).run('sudo apt autoremove -y')
Connection(cd_host).run('sudo apt-get update')
Connection(cd_host).run('sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release -y')
try:
    Connection(cd_host).run(
        'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg')
    Connection(cd_host).run('echo \
    "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
except:
    print("Repository already exists")
Connection(cd_host).run('sudo apt-get update')
Connection(cd_host).run(
    'sudo apt-get install docker-ce docker-ce-cli containerd.io -y')
Connection(cd_host).run('sudo usermod -aG docker jenkins')
Connection(cd_host).run('newgrp docker')
Connection(cd_host).run(
    'sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
Connection(cd_host).run('sudo chmod +x /usr/local/bin/docker-compose')


try:
    Connection(cd_host).run('docker rmi -f $(docker images -a -q)')
except:
    print("registry has not images")
try:
    Connection(cd_host).run("rm ./docker-compose-prod.yml")
except:
    print("docker-compose-prod.yml doesn't exists")
try:
    Connection(cd_host).run("rm ./.env-prod")
except:
    print(".env-prod doesn't exist")


try:
    Connection(cd_host).put("./docker-compose-prod.yml",
                            "./docker-compose-prod.yml")
except:
    print("docker-compose-prod.yml already exists")
try:
    Connection(cd_host).put("./.env-prod", "./.env-prod")
except:
    print("env-prod already exists")


try:
    Connection(cd_host).run('docker-compose -f ./docker-compose-prod.yml pull')
except:
    print("Stack updated")
try:
    Connection(cd_host).run(
        'docker-compose -f ./docker-compose-prod.yml up -d')
except:
    print("Stack already created")
