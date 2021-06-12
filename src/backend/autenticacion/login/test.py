import unittest
from app import app
from unittest.mock import patch
import json


def find_one_mock(_):
    return {
        "_id": "60c280e219b8d8664b1a06b6",
        "activo": 1,
        "apellido": "Peitzner",
        "correo": "guillermopeitzner@gmail.com",
        "direccion": "15 Calle C 15-27 Zona 11 de Mixco",
        "nombre": "Guillermo",
        "telefono": "50235240107",
        "tipo": "administrador",
    }


class FlaskTest(unittest.TestCase):

    @patch("app.col.find_one", find_one_mock)
    def test_default(self):
        tester = app.test_client(self)
        response = tester.post(
            "/", data=json.dumps({"email": "guillermopeitzner@gmail.com", "password": "1234"}), content_type='application/json')
        status_code = response.status_code
        data = response.data.decode("utf-8")
        print(data)
        self.assertEquals(status_code, 200)


if __name__ == '__main__':
    unittest.main()
