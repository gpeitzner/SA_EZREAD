import os
from fabric import SerialGroup


cd_host1 = os.environ["CD_HOST1"]
cd_host2 = os.environ["CD_HOST2"]

try:
    SerialGroup(cd_host1, cd_host2).run('docker-compose -f ./docker-compose-prod.yml down')
except:
    print("Stack not created")


SerialGroup(cd_host1, cd_host2).run('export DEBIAN_FRONTEND=noninteractive')
SerialGroup(cd_host1, cd_host2).run('sudo apt update')
SerialGroup(cd_host1, cd_host2).run('sudo apt upgrade -y')
SerialGroup(cd_host1, cd_host2).run('sudo apt autoremove -y')
SerialGroup(cd_host1, cd_host2).run('sudo apt-get update')
SerialGroup(cd_host1, cd_host2).run('sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release -y')
try:
    SerialGroup(cd_host1, cd_host2).run(
        'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg')
    SerialGroup(cd_host1, cd_host2).run('echo \
    "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
except:
    print("Repository already exists")
SerialGroup(cd_host1, cd_host2).run('sudo apt-get update')
SerialGroup(cd_host1, cd_host2).run(
    'sudo apt-get install docker-ce docker-ce-cli containerd.io -y')
SerialGroup(cd_host1, cd_host2).run('sudo usermod -aG docker jenkins')
SerialGroup(cd_host1, cd_host2).run('newgrp docker')
SerialGroup(cd_host1, cd_host2).run(
    'sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
SerialGroup(cd_host1, cd_host2).run('sudo chmod +x /usr/local/bin/docker-compose')


try:
    SerialGroup(cd_host1, cd_host2).run('docker rmi -f $(docker images -a -q)')
except:
    print("registry has not images")


try:
    SerialGroup(cd_host1, cd_host2).run("rm ./docker-compose-prod.yml")
except:
    print("docker-compose-prod.yml doesn't exists")
try:
    SerialGroup(cd_host1, cd_host2).run("rm ./.env-prod")
except:
    print(".env-prod doesn't exist")


try:
    SerialGroup(cd_host1, cd_host2).put("./docker-compose-prod.yml",
                            "./docker-compose-prod.yml")
except:
    print("docker-compose-prod.yml already exists")
try:
    SerialGroup(cd_host1, cd_host2).put("./.env-prod", "./.env-prod")
except:
    print("env-prod already exists")
try:
    SerialGroup(cd_host1, cd_host2).run(
        'docker-compose -f ./docker-compose-prod.yml up -d')
except:
    print("Stack already created")
