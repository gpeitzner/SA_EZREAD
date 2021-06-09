#MICROSERVICIO USUARIO

##Crear Usuario
###Puerto 5002
###TIPO: POST
###Ruta: /users
###Body Post
- tipo:string
- nombre:string [Required]
- apellido:string
- correo:string [Required]
- password:string [Required]
- telefono:string
- direccion:string
###Respuesta:
###Correcta
####{"mensaje":"Usuario Insertado","id":str(ret.inserted_id)}
###Incorrecta
####{"mensaje":"Correo ya existente"}

##Editar Usuario
###Puerto 5003
###TIPO: POST
###Ruta: /users
###Body Put
- id:string [Required]
- nombre:string [Required]
- apellido:string 
- correo:string [Required]
- password:string 
- telefono:string 
- direccion:string 
###Respuesta:
###Correcta
####{"mensaje":"Modificado"}
*Enviar informacion vieja porque se actualizan todos los campos, excepto la contraseña*

##Eliminar Usuario
###Puerto 5004
###TIPO: DELETE
###Ruta: /users/<string:id>
###Respuesta:
###Correcta
####{"mensaje":"Eliminado"}

##Obtener Todos los Usuarios
###Puerto 5005
###TIPO: GET
###Ruta: /users
###Respuesta:
###JSON ARRAY

##Obtener un Usuario
###Puerto 5005
###TIPO: GET
###Ruta: /users/<string:id>
###Respuesta:
###JSON OBJECT
