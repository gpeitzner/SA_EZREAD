import os
from fabric import Connection

cd_host = os.environ["CD_HOST"]


Connection(cd_host).run("sudo apt update")
Connection(cd_host).run("sudo apt upgrade")
Connection(cd_host).run("sudo apt autoremove")


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

