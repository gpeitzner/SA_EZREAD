import unittest
from app import app
from unittest.mock import patch
import json


def findOne_mock(_):
    return {
        "Editorial": "Espasa",
        "Titulo": "Entre lobos y autómatas",
        "Genero": "Filosofía",
        "Autor": "Antonio Orbe",
        "Activo": 1,
        "Cantidad": 25,
        "Precio": 100.25,
        "Imagen": ""
    }


class FlaskTest(unittest.TestCase):

    def test_default(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        data = response.data.decode("utf-8")
        self.assertEquals(status_code, 200)
        self.assertEquals(data, '<p>libro_crear</p>')

    @ patch("app.col.find_one", findOne_mock)
    def test_Create(self):
        tester = app.test_client(self)
        response = tester.post(
            "/libros/crear", data=json.dumps({"Editorial": "Espasa",
                                              "Titulo": "Entre lobos y autómatas",
                                              "Genero": "Filosofía",
                                              "Autor": "Antonio Orbe",
                                              "Activo": 1,
                                              "Cantidad": 25,
                                              "Precio": 100.25,
                                              "Imagen": ""}), content_type='application/json')
        status_code = response.status_code
        data = response.data.decode("utf-8")
        datos = json.loads(data)
        # print(data)
        self.assertEqual(status_code, 200)
        self.assertIn("mensaje", data)
        self.assertEquals(datos["mensaje"], "ya existe")


if __name__ == '__main__':
    unittest.main()
