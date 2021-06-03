docker build --force-rm --no-cache --tag autenticacion:latest .
docker image prune -f
docker run -it -p 5000:5000 --rm --env-file	".env" autenticacion:latest
