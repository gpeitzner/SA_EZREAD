ECHO "Starting environment ..."
ECHO "Building autentication microservices ..."
docker build --force-rm --no-cache --tag ezread_login:latest ./src/backend/autenticacion/login/
ECHO "Building book microservices ..."
docker build --force-rm --no-cache --tag ezread_libro_crear:latest ./src/backend/libro/crear/
docker build --force-rm --no-cache --tag ezread_libro_editar:latest ./src/backend/libro/editar/
docker build --force-rm --no-cache --tag ezread_libro_eliminar:latest ./src/backend/libro/eliminar/
docker build --force-rm --no-cache --tag ezread_libro_obtener:latest ./src/backend/libro/obtener/
ECHO "Building order microservices ..."
docker build --force-rm --no-cache --tag ezread_orden_crear:latest ./src/backend/orden/crear/
docker build --force-rm --no-cache --tag ezread_orden_editar:latest ./src/backend/orden/editar/
docker build --force-rm --no-cache --tag ezread_orden_eliminar:latest ./src/backend/orden/eliminar/
docker build --force-rm --no-cache --tag ezread_orden_obtener:latest ./src/backend/orden/obtener/
ECHO "Building user microservices ..."
docker build --force-rm --no-cache --tag ezread_usuario_crear:latest ./src/backend/usuario/crear/
docker build --force-rm --no-cache --tag ezread_usuario_editar:latest ./src/backend/usuario/editar/
docker build --force-rm --no-cache --tag ezread_usuario_eliminar:latest ./src/backend/usuario/eliminar/
docker build --force-rm --no-cache --tag ezread_usuario_obtener:latest ./src/backend/usuario/obtener/
ECHO "Building web page ..."
docker build  --force-rm --no-cache --build-arg NODE_ENV=dev --tag ezread_ui:latest ./src/frontend/
ECHO "Cleaning intermediate building images ..."
docker image prune -f
ECHO "Everything it's ok :]"

