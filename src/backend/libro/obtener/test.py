import unittest
from app import app
from unittest.mock import patch
import json


def find_mock():
    return [
        {
            "Activo": 1,
            "Autor": "Antonio Orbe",
            "Cantidad": 25,
            "Editorial": "Espasa3",
            "Genero": "Filosofía",
            "Imagen": "https://ezreadbooks.s3.us-east-2.amazonaws.com/Entre_lobos-589e5dd1-b452-4c1d-9064-ac40338ad7a4.png",
            "Precio": 100,
            "Titulo": "Entre lobos",
            "_id": "60c52bd12733066334bec2cd",
            "Path": "Entre_lobos-589e5dd1-b452-4c1d-9064-ac40338ad7a4.png"
        },
        {
            "Activo": 1,
            "Autor": "Antonio Orbe",
            "Cantidad": 25,
            "Editorial": "Espasa",
            "Genero": "Filosofía",
            "Imagen": "https://ezreadbooks.s3.us-east-2.amazonaws.com/Entre_lobos-c8bce17b-d9b7-47a4-b9a4-0eabff26070c.png",
            "Precio": 100,
            "Titulo": "Entre lobos",
            "_id": "60c5758616bbb4c624afe109",
            "Path": "Entre_lobos-c8bce17b-d9b7-47a4-b9a4-0eabff26070c.png"
        }
    ]


def findOne_mock(_):
    return{
        "Activo": 1,
        "Autor": "Antonio Orbe",
        "Cantidad": 25,
        "Editorial": "Espasa3",
        "Genero": "Filosofía",
        "Imagen": "https://ezreadbooks.s3.us-east-2.amazonaws.com/Entre_lobos-589e5dd1-b452-4c1d-9064-ac40338ad7a4.png",
        "Precio": 100,
        "Titulo": "Entre lobos",
        "_id": "60c52bd12733066334bec2cd",
        "Path": "Entre_lobos-589e5dd1-b452-4c1d-9064-ac40338ad7a4.png"
    }


def findGenders(_):
    return[
        {
            "_id": "Filosofía",
            "libros": [
                {
                    "Activo": 1,
                    "Autor": "Antonio Orbe",
                    "Cantidad": 25,
                    "Editorial": "Espasa3",
                    "Imagen": "https://ezreadbooks.s3.us-east-2.amazonaws.com/Entre_lobos-589e5dd1-b452-4c1d-9064-ac40338ad7a4.png",
                    "Precio": 100,
                    "Titulo": "Entre lobos",
                    "id": "60c52bd12733066334bec2cd",
                    "Genero": "Filosofía"
                },
                {
                    "Activo": 1,
                    "Autor": "Antonio Orbe",
                    "Cantidad": 25,
                    "Editorial": "Espasa",
                    "Imagen": "https://ezreadbooks.s3.us-east-2.amazonaws.com/Entre_lobos-c8bce17b-d9b7-47a4-b9a4-0eabff26070c.png",
                    "Precio": 100,
                    "Titulo": "Entre lobos",
                    "id": "60c5758616bbb4c624afe109",
                    "Genero": "Filosofía"
                }
            ]
        }
    ]


class FlaskTest(unittest.TestCase):

    @ patch("app.col.find", find_mock)
    def test_Obtener(self):
        tester = app.test_client(self)
        response = tester.get("/libros")
        status_code = response.status_code
        data = response.data.decode("utf-8")
        # print("data-->",data)
        self.assertEqual(status_code, 200)

    @ patch("app.col.find_one", findOne_mock)
    def test_getLibro(self):
        tester = app.test_client(self)
        response = tester.get(
            "/libro?id=60c52bd12733066334bec2cd")
        status_code = response.status_code
        data = response.data.decode("utf-8")
        # print(data)
        self.assertEqual(status_code, 200)
        self.assertIn("libro", data)

    @ patch("app.col.aggregate", findGenders)
    def test_getGenders(self):
        tester = app.test_client(self)
        response = tester.get("/libros/Generos")
        status_code = response.status_code
        data = response.data.decode("utf-8")
        datos = json.loads(data)
        self.assertEqual(status_code, 200)
        self.assertIn("Generos", data)
        self.assertEqual(len(datos['Generos']),1)


if __name__ == '__main__':
    unittest.main()
