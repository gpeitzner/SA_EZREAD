import unittest
from app import app
from unittest.mock import patch
import json


def updateOne_mock(_, d):
    return {
        "modified count": 1
    }


class FlaskTest(unittest.TestCase):

    def test_default(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        data = response.data.decode("utf-8")
        self.assertEquals(status_code, 200)
        self.assertEquals(data, '<p>libro_eliminar</p>')


if __name__ == '__main__':
    unittest.main()
