# -*- coding: utf-8 -*-

import unittest
from cerberus import Validator

# Objeto correcto
list_validation_object_ok = {
    "list_a": [1, 5, 10, 99, 400],
    "list_b": ["foo", "bar", 1]
}

# Objeto inválido 1
list_validation_object_wrong = {
    "list_a": [3, 6, -9, 100],
    "list_b": ["simple", "validation", -9]
}

# Objeto inválido 2
list_validation_object_wrong_2 = {
    "list_a": [1, 5, 10, 99, 400],
    "list_b": ["simple", "validation", None]
}

def string_or_integer_list(field, value, error):
    if not isinstance(value, list):
        error(field, u'No es una lista')
    else:
        for item in value:
            if isinstance(item, int) or isinstance(item, str):
                # Test ok: es un valor válido
                pass
            else:
                error(field, u'No es válido')

class TestValidation002(unittest.TestCase):
    
    def factory_validator(self):
        return Validator({
            "list_a": {
                "type": "list",
                "required": True,
                "schema": {
                    "type": "integer",
                    "min": 1
                }
            },
            "list_b": {
                "type": "list",
                "validator": string_or_integer_list
            },
        })

    def test_ok_validation(self):
        self.assertTrue(self.factory_validator().validate(list_validation_object_ok))

    def test_wrong_validation(self):
        self.assertFalse(self.factory_validator().validate(list_validation_object_wrong))
    
    def test_wrong_validation_2(self):
        self.assertFalse(self.factory_validator().validate(list_validation_object_wrong_2))


if __name__ == "__main__":
    unittest.main()