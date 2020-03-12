# coding=utf-8
from unittest import TestCase

class Test(TestCase):
    def test_validar_dni(self):
        from funcionesCli import validarDNI
        self.assertTrue(validarDNI('39453357P'))
