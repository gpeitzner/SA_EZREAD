docker build --force-rm --no-cache --tag autenticacion:latest .
docker run -it -p 5000:5000 --rm autenticacion:latest