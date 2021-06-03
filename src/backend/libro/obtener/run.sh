docker build --force-rm --no-cache --tag autenticacion:latest .
docker run -it -p 5001:5001 --rm autenticacion:latest