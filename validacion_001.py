# -*- coding: utf-8 -*-

import unittest
from cerberus import Validator

# Objeto correcto > Validación correcta
validation_object_001 = dict(
    age=29,
    email="urodoz@gmail.com",
    name="Albert"   
)

# Objeto incorrecto > Validación incorrecta
validation_object_002 = dict(
    age="cincuenta",
    email="urodoz@gmail.com",
    name="Albert"   
)

cerberus_validator = Validator({
    "age": {
        "type": "integer",
        "min": 19,
        "max": 119,
        "required": True
    },
    "email": {
        "type": "string",
        "required": True,
        "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    },
    "name": {
        "type": "string",
        "empty": False,
        "required": True
    }
})

class TestValidation001(unittest.TestCase):

    def test_ok_validation(self):
        self.assertTrue(cerberus_validator.validate(validation_object_001))

    def test_wrong_validation(self):
        self.assertFalse(cerberus_validator.validate(validation_object_002))


if __name__ == "__main__":
    unittest.main()