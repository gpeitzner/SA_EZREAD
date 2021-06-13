import os
from fabric import Connection

cd_host = os.environ["CD_HOST"]


Connection(cd_host).run("sudo apt update")
Connection(cd_host).run("sudo apt upgrade")
Connection(cd_host).run("sudo apt autoremove")
Connection(cd_host).run("sudo snap install docker")
Connection(cd_host).put("./docker-compose-prod.yml",
                        "./docker-compose-prod.yml")
Connection(cd_host).put("./dev_ops/cd/.env-prod", "./.env-prod")
Connection(cd_host).run(
    "sudo docker-compose -f ./docker-compose-prod.yml down")
Connection(cd_host).run(
    "sudo docker-compose -f ./docker-compose-prod.yml pull")
Connection(cd_host).run(
    "sudo docker-compose -f ./docker-compose-prod.yml up -d")
