from unittest import TestCase


class Test(TestCase):
    def test_precio_total(self):
        from funcionesHab import precioTotal
        self.assertTrue(precioTotal(5,10))