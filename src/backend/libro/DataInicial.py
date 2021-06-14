import os
import json
import pymongo

db_host = os.environ["db_host"] if "db_host" in os.environ else "localhost"
db_password = os.environ["db_password"] if "db_password" in os.environ else ""
db_port = int(os.environ["db_port"]) if "db_port" in os.environ else 27017
db_name = os.environ["db_name"] if "db_name" in os.environ else "ezread"
db_user = os.environ["db_user"] if "db_user" in os.environ else ""

client = pymongo.MongoClient(
    host=db_host, port=db_port, username=db_user, password=db_password)
db = client[str(db_name)]
col = db["libros"]

data = [
    {
        "Editorial": "Alienta",
        "Titulo": "Código no verbal",
        "Genero": "Autoayuda",
        "Autor": "Sonia El Hakim",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Alienta1.jpg",
        "Path": "Alienta1.jpg"

    },
    {
        "Editorial": "Alienta",
        "Titulo": "Vende a la mente, no a la gente",
        "Genero": "Finanzas",
        "Autor": "Jürgen Klaric",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Alienta2.jpg",
        "Path": "Alienta2.jpg"
    },

    {
        "Editorial": "Alienta",
        "Titulo": "El camino del inversor",
        "Genero": "Economía",
        "Autor": "Javier del Valle y Fernando Ruiz de Velasco",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Alienta3.jpg",
        "Path": "Alienta3.jpg"
    },

    {
        "Editorial": "Alienta",
        "Titulo": "Aprendiendo de los mejores",
        "Genero": "Autoayuda",
        "Autor": "Francisco Alcaide Hernández",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Alienta4.jpg",
        "Path": "Alienta4.jpg"
    },
    {
        "Editorial": "Alienta",
        "Titulo": "Obras completas",
        "Genero": "Religion",
        "Autor": "Miyamoto Musashi",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Alienta5.jpg",
        "Path": "Alienta5.jpg"
    },
    {
        "Editorial": "Alienta",
        "Titulo": "El Gym y el ñam",
        "Genero": "Nutricion",
        "Autor": "Ruben García Carnicero",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Alienta6.jpg",
        "Path": "Alienta6.jpg"
    },
    {
        "Editorial": "Alienta",
        "Titulo": "¡Es la microbiota, idiota",
        "Genero": "Nutricion",
        "Autor": "Sari Arponen",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Alienta7.jpg",
        "Path": "Alienta7.jpg"
    },
    {
        "Editorial": "Alienta",
        "Titulo": "Irrompible",
        "Genero": "Autoayuda",
        "Autor": "Francisco García Vena",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Alienta8.jpg",
        "Path": "Alienta8.jpg"
    },
    {
        "Editorial": "Alienta",
        "Titulo": "Los 88 peldaños del éxito",
        "Genero": "Autoayuda",
        "Autor": "Anxo Perez Rodriguez",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Alienta9.jpg",
        "Path": "Alienta9.jpg"
    },
    {
        "Editorial": "Alienta",
        "Titulo": "El tao de Warren Buffett",
        "Genero": "Economía",
        "Autor": "Mary Buffet y David Clark",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Alienta10.jpg",
        "Path": "Alienta10.jpg"
    },
    {
        "Editorial": "Planeta Comic",
        "Titulo": "Las Guerras de las galaxias",
        "Genero": "Ciencia Ficción",
        "Autor": "AA. VV.",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Comic1.jpg",
        "Path": "Comic1.jpg"
    },
    {
        "Editorial": "Planeta Comic",
        "Titulo": "Los Tres Fantasmas de Tesla",
        "Genero": "Ciencia Ficción",
        "Autor": "Marazano Richard",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Comic2.jpg",
        "Path": "Comic2.jpg"
    },
    {
        "Editorial": "Planeta Comic",
        "Titulo": "Star Wars Discipulo oscuro",
        "Genero": "Ciencia Ficción",
        "Autor": "Christie Golden",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Comic3.jpg",
        "Path": "Comic3.jpg"
    },
    {
        "Editorial": "Planeta Comic",
        "Titulo": "Star Wars Ahsoka (novela)",
        "Genero": "Ciencia Ficción",
        "Autor": "E. K. Johnston",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Comic4.jpg",
        "Path": "Comic4.jpg"
    },
    {
        "Editorial": "Planeta Comic",
        "Titulo": "Windhaven",
        "Genero": "Comic y manga juvenil",
        "Autor": "George R. R. Martin",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Comic5.jpg",
        "Path": "Comic5.jpg"
    },
    {
        "Editorial": "Planeta Comic",
        "Titulo": "Dragon Ball Serie Roja n271",
        "Genero": "Comic y manga juvenil",
        "Autor": "Akira Toriyama",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Comic6.jpg",
        "Path": "Comic6.jpg"
    },
    {
        "Editorial": "Planeta Comic",
        "Titulo": "Garfield 2016-2018",
        "Genero": "Comic y manga juvenil",
        "Autor": "Jim Davis",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Comic7.jpg",
        "Path": "Comic7.jpeg"
    },
    {
        "Editorial": "Planeta Comic",
        "Titulo": "A de Anonymus",
        "Genero": "Novela Gráfica",
        "Autor": "David Kushner y Koren Shadmi",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Comic8.jpg",
        "Path": "Comic8.jpg"
    },
    {
        "Editorial": "Planeta Comic",
        "Titulo": "Coronavirus",
        "Genero": "Novela Gráfica",
        "Autor": "Ana Polegre, Enfermera en apuros",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Comic9.jpg",
        "Path": "Comic9.jpg"
    },
    {
        "Editorial": "Planeta Comic",
        "Titulo": "Creepshow de Stephen King y Bernie Wrightson",
        "Genero": "Novela Gráfica",
        "Autor": "Stephen King y Bernie Wrightson",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Comic10.jpg",
        "Path": "Comic10.jpg"
    },
    {
        "Editorial": "Tusquets Editores S.A",
        "Titulo": "Imperio, Crónicas de los invasores II",
        "Genero": "Ciencia Ficción",
        "Autor": "John Connolly y Jennifer Ridyard",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Tusquets1.jpg",
        "Path": "Tusquets1.jpg"
    },
    {
        "Editorial": "Tusquets Editores S.A",
        "Titulo": "El espacio culinario",
        "Genero": "Cocina",
        "Autor": "Miguel Espinet",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Tusquets2.jpg",
        "Path": "Tusquets2.jpg"
    },
    {
        "Editorial": "Tusquets Editores S.A",
        "Titulo": "El sabor de Cuba",
        "Genero": "Cocina",
        "Autor": "René Vásquez Díaz",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Tusquets3.jpg",
        "Path": "Tusquets3.jpg"
    },
    {
        "Editorial": "Tusquets Editores S.A",
        "Titulo": "Vinos de Espania",
        "Genero": "Cocina",
        "Autor": "Julian Jeff",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Tusquets4.jpg",
        "Path": "Tusquets4.jpg"
    },
    {
        "Editorial": "Tusquets Editores S.A",
        "Titulo": "La fisica Cuantica del futuro",
        "Genero": "Ciencia",
        "Autor": "Hans Christian von Baeyer",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Tusquets5.jpg",
        "Path": "Tusquets5.jpg"
    },
    {
        "Editorial": "Tusquets Editores S.A",
        "Titulo": "La entropia desvelada",
        "Genero": "Ciencia",
        "Autor": "Arieh Ben-Naim",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Tusquets6.jpg",
        "Path": "Tusquets6.jpg"
    },
    {
        "Editorial": "Tusquets Editores S.A",
        "Titulo": "El jazz de la Física",
        "Genero": "Ciencia",
        "Autor": "Stefphon Alexander",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Tusquets7.jpg",
        "Path": "Tusquets7.jpg"
    },
    {
        "Editorial": "Tusquets Editores S.A",
        "Titulo": "Un maestro de arquitectos en Barcelona",
        "Genero": "Arte",
        "Autor": "Federico Correo",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Tusquets8.jpg",
        "Path": "Tusquets8.jpg"
    },
    {
        "Editorial": "Tusquets Editores S.A",
        "Titulo": "El drama del niño dotado",
        "Genero": "Psicología",
        "Autor": "Alice Miller",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Tusquets9.jpg",
        "Path": "Tusquets9.jpg"
    },
    {
        "Editorial": "Tusquets Editores S.A",
        "Titulo": "El caso del inocente niño asesino",
        "Genero": "Psicología",
        "Autor": "André Gide",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Tusquets10.jpg",
        "Path": "Tusquets10.jpg"
    },
    {
        "Editorial": "Click Ediciones",
        "Titulo": "Maldita Reliquia",
        "Genero": "Humor",
        "Autor": "David José Balleser",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/clic1.jpg",
        "Path": "clic1.jpg"

    },
    {
        "Editorial": "Click Ediciones",
        "Titulo": "El renacer los monstruos",
        "Genero": "Humor",
        "Autor": "Francesc Marí",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/clic2.jpg",
        "Path": "clic2.jpg"
    },
    {
        "Editorial": "Click Ediciones",
        "Titulo": "Controlar lo incontrolable",
        "Genero": "Autoayuda",
        "Autor": "Artur Amich",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/clic3.jpg",
        "Path": "clic3.jpg"
    },
    {
        "Editorial": "Click Ediciones",
        "Titulo": "El club de los aventureros y los hombres de plata",
        "Genero": "Infantil",
        "Autor": "Enrique Gómez Medina",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/clic4.jpg",
        "Path": "clic4.jpg"
    },
    {
        "Editorial": "Click Ediciones",
        "Titulo": "Todo de mí",
        "Genero": "Novela Romántica",
        "Autor": "Moruena Estríngana",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/clic5.jpg",
        "Path": "clic5.jpg"
    },
    {
        "Editorial": "Click Ediciones",
        "Titulo": "La marquesa de Connemara",
        "Genero": "Novela Romántica",
        "Autor": "J. F. Morgan",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/clic6.jpg",
        "Path": "clic6.jpg"
    },
    {
        "Editorial": "Click Ediciones",
        "Titulo": "La leyenda de la mariposa azul",
        "Genero": "Novela Romántica",
        "Autor": "Calista Sweet",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/clic7.jpg",
        "Path": "clic7.jpg"
    },
    {
        "Editorial": "Click Ediciones",
        "Titulo": "La España fabulosa",
        "Genero": "Viajes",
        "Autor": "Jesus Callejo",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/clic8.jpg",
        "Path": "clic8.jpg"
    },

    {
        "Editorial": "Click Ediciones",
        "Titulo": "Tex Kerba",
        "Genero": "Viajes",
        "Autor": "Miguel Angel Francisco",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/clic9.jpg",
        "Path": "clic9.jpg"
    },
    {
        "Editorial": "Click Ediciones",
        "Titulo": "Cerebro y Ordenador",
        "Genero": "Ciencia",
        "Autor": "Antonio Orbe",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/clic10.jpg",
        "Path": "clic10.jpg"
    },
    {
        "Editorial": "Espasa",
        "Titulo": "Entre lobos y autómatas",
        "Genero": "Filosofía",
        "Autor": "Antonio Orbe",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Espasa1.jpg",
        "Path": "Espasa1.jpg"
    },
    {
        "Editorial": "Espasa",
        "Titulo": "La Rebelión de las masas",
        "Genero": "Filosofía",
        "Autor": "José Ortega y Gasset",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Espasa2.jpg",
        "Path": "Espasa2.jpg"
    },
    {
        "Editorial": "Espasa",
        "Titulo": "HItos del sentido",
        "Genero": "Filosofía",
        "Autor": "Antonio Escohotado",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Espasa3.jpg",
        "Path": "Espasa3.jpg"
    },
    {
        "Editorial": "Espasa",
        "Titulo": "Emocionarte. La doble vida de los cuadros",
        "Genero": "Ciencias Humanas y sociales",
        "Autor": "Carlos del Amor",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Espasa4.jpg",
        "Path": "Espasa4.jpg"
    },
    {
        "Editorial": "Espasa",
        "Titulo": "Un ciudadano libre",
        "Genero": "Ciencias Humanas y sociales",
        "Autor": "Albert Rivera",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Espasa5.jpg",
        "Path": "Espasa5.jpg"
    },
    {
        "Editorial": "Espasa",
        "Titulo": "La guerra mas larga de la Historia",
        "Genero": "Ciencias Humanas y sociales",
        "Autor": "Lola Venegags, Isabe M. Reverte y Margo Venegas",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Espasa6.jpg",
        "Path": "Espasa6.jpg"
    },
    {
        "Editorial": "Espasa",
        "Titulo": "Despleagando velas",
        "Genero": "Ciencias Humanas y sociales",
        "Autor": "Cristina Villanueva",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Espasa7.jpg",
        "Path": "Espasa7.jpg"
    },
    {
        "Editorial": "Espasa",
        "Titulo": "Déjame entrar",
        "Genero": "Terror",
        "Autor": "John Ajvide LIndqvist",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Espasa8.jpg",
        "Path": "Espasa8.jpg"
    },
    {
        "Editorial": "Espasa",
        "Titulo": "La Zona",
        "Genero": "Terror",
        "Autor": "Juan Miguel Aguilera",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Espasa9.jpg",
        "Path": "Espasa9.jpg"
    },
    {
        "Editorial": "Espasa",
        "Titulo": "Hay alguien ahí",
        "Genero": "Terror",
        "Autor": "Jorge Magano",
        "Activo": 1,
        "Cantidad": 25,
        "Imagen": "https://books-pics.s3.us-east-2.amazonaws.com/Espasa10.jpg",
        "Path": "Espasa10.jpg"
    }
]

result = col.insert_many(data)
print({'insertados': col.count_documents})
