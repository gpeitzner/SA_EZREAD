# SA_EZREAD

# Run backend in dev mode

1. Build the images using the following commands:

```bash
sh compile-dev.sh #unix
.\compile-dev.bat #windows
```

2. Create an environment variables file named `.env-dev` with the follow structure:

```env
MONGO_INITDB_ROOT_USERNAME=<mongo_user>
MONGO_INITDB_ROOT_PASSWORD=<mongo_user_password>
db_host=db
db_password=<mongo_user_password>
db_port=27017
db_name=<db_name>
db_user=<mongo_user>
```

3. Deploy the docker-compose file named `docker-compose-dev.yml` using the following command:

```bash
docker-compose -f ./docker-compose-dev.yml up -d
```

4. To stop all microservices run the follow command:

```bash
docker-compose -f ./docker-compose-dev.yml down
```
