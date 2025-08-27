import unittest
from logic.pleat import Pleat
from logic.gadgets import AND, OR, NOT, NAND, XOR
from logic.network import Network

# Pruebas unitarias para cada compuerta lógica
class TestGadgetsTruthTables(unittest.TestCase):
    def setUp(self):
        # Se ejecuta antes de cada test: prepara pleats de entrada/salida
        self.a = Pleat("a")
        self.b = Pleat("b")
        self.o = Pleat("o")
        self.net = Network()
        # Registrar todos los pleats en la red
        for p in (self.a, self.b, self.o):
            self.net.add_pleat(p)

    def test_and(self):
        # Prueba compuerta AND
        g = AND("AND1", [self.a, self.b], [self.o])
        self.net.add_gadget(g)
        # Recorre todas las combinaciones de entradas (0/1 → False/True)
        for av in (False, True):
            for bv in (False, True):
                self.net.set_inputs({"a": av, "b": bv})
                self.net.run()
                # Verifica que el resultado sea el esperado
                self.assertEqual(self.o.value, av and bv)
        # Limpia los gadgets de la red después de la prueba
        self.net.gadgets.clear()

    def test_or(self):
        # Prueba compuerta OR
        g = OR("OR1", [self.a, self.b], [self.o])
        self.net.add_gadget(g)
        for av in (False, True):
            for bv in (False, True):
                self.net.set_inputs({"a": av, "b": bv})
                self.net.run()
                self.assertEqual(self.o.value, av or bv)
        self.net.gadgets.clear()

    def test_not(self):
        # Prueba compuerta NOT
        g = NOT("NOT1", [self.a], [self.o])
        self.net.add_gadget(g)
        for av in (False, True):
            self.net.set_inputs({"a": av})
            self.net.run()
            self.assertEqual(self.o.value, (not av))
        self.net.gadgets.clear()

    def test_nand(self):
        # Prueba compuerta NAND
        g = NAND("NAND1", [self.a, self.b], [self.o])
        self.net.add_gadget(g)
        for av in (False, True):
            for bv in (False, True):
                self.net.set_inputs({"a": av, "b": bv})
                self.net.run()
                self.assertEqual(self.o.value, not (av and bv))
        self.net.gadgets.clear()

    def test_xor(self):
        # Prueba compuerta XOR
        g = XOR("XOR1", [self.a, self.b], [self.o])
        self.net.add_gadget(g)
        for av in (False, True):
            for bv in (False, True):
                self.net.set_inputs({"a": av, "b": bv})
                self.net.run()
                # XOR se define como (a OR b) AND NOT(a AND b)
                self.assertEqual(self.o.value, (av or bv) and not (av and bv))
        self.net.gadgets.clear()


# Prueba de integración: construcción de un medio sumador

class TestIntegrationHalfAdder(unittest.TestCase):
    def test_half_adder(self):
        # Pleats de entrada y salida
        a, b = Pleat("a"), Pleat("b")
        sum_, carry = Pleat("sum"), Pleat("carry")
        t_or, t_and = Pleat("t_or"), Pleat("t_and")

        net = Network()
        for p in (a, b, sum_, carry, t_or, t_and):
            net.add_pleat(p)

        # Definición de gadgets del medio sumador
        # Carry correcto = AND(a, b)
        net.gadgets.clear()
        g_and = AND("and1", [a, b], [carry])
        g_xor = XOR("xor1", [a, b], [sum_])

        # Registrar gadgets en la red
        for g in (g_and, g_xor):
            net.add_gadget(g)

        # Tabla de verdad esperada del medio sumador
        expected = {
            (False, False): (False, False),
            (False, True):  (True, False),
            (True, False):  (True, False),
            (True, True):   (False, True)
        }

        # Validar que la simulación coincida con la tabla de verdad
        for av, bv in expected:
            net.set_inputs({"a": av, "b": bv})
            net.run()
            self.assertEqual((sum_.value, carry.value), expected[(av, bv)])


if __name__ == "__main__":
    unittest.main()
