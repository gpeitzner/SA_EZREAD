# Login

## Route

```
http://localhost:5000/
```

## Methods

- POST

## Body

```json
{
	"email": "guillermopeitzner@gmail.com",
	"password": "1234"
}
```

## Expected responses

### Good credentials

HTTP / 200

```json
{
	"_id": "60c280e219b8d8664b1a06b6",
	"activo": 1,
	"apellido": "Peitzner",
	"correo": "guillermopeitzner@gmail.com",
	"direccion": "15 Calle C 15-27 Zona 11 de Mixco",
	"nombre": "Guillermo",
	"telefono": "50235240107",
	"tipo": "administrador"
}
```

### Bad credentials

HTTP / 400

```json
{
	"message": "bad credentials"
}
```
