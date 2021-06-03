docker build --force-rm --no-cache --tag autenticacion:latest .
docker run -it -p 5002:5002 --rm autenticacion:latest