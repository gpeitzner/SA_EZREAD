# MICROSERVICIO ORDEN

## Crear Orden

PUERTO: 5002

TIPO: POST

RUTA: /ordenes

### Body:
- usuario:string [obligatorio]
- libro: string [obligatorio]
- cantidad: string [obligatorio]
- precio: string

### Respuesta:

Nueva orden: {"mensaje":"Orden creada","id":'id_orden'}

Nuevo libro agregado: {"mensaje":"Nuevo libro agregado"}

## Editar Orden

PUERTO: 5003

TIPO: PUT

RUTA: /ordenes

### Body:
- usuario:string [obligatorio]
- estado: string (0 para orden activa)
- libros: array [obligatorio]

### Parametros de cada libro
- id_libro: string
- cantidad_libro: string
- precio_libro: string


### Respuesta:

Correcta: {"mensaje":"Orden modificada"}

Incorrecto: {"mensaje":"El usuario no tiene orden activa"}

## Eliminar Orden

PUERTO: 5004

TIPO: DELETE

RUTA: /ordenes

### Body:
- usuario:string [obligatorio]

### Respuesta:

Correcta: {"mensaje":"Usuario eliminado"}

## Obtener Orden

PUERTO: 5005

TIPO: GET

RUTA: /ordenes

### Body:
- usuario:string [obligatorio]

### Respuesta:

Correcta: json object

Incorrecta: {"mensaje":"No tiene ordenes"}