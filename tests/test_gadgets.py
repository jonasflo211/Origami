import unittest
from logic.pleat import Pleat
from logic.gadgets import AND, OR, NOT, NAND, XOR
from logic.network import Network

class TestGadgets(unittest.TestCase):
    def test_AND(self):
        a, b, out = Pleat("a"), Pleat("b"), Pleat("out")
        gate = AND("AND", [a, b], [out])
        for av in [False, True]:
            for bv in [False, True]:
                a.value, b.value = av, bv
                gate.evaluate()
                self.assertEqual(out.value, av and bv)

    def test_half_adder(self):
        a, b = Pleat("a"), Pleat("b")
        sum_, carry = Pleat("sum"), Pleat("carry")
        net = Network()
        xor_gate = XOR("XOR", [a, b], [sum_])
        and_gate = AND("AND", [a, b], [carry])
        net.add_pleat(a); net.add_pleat(b)
        net.add_pleat(sum_); net.add_pleat(carry)
        net.add_gadget(xor_gate); net.add_gadget(and_gate)

        expected = {
            (False, False): (False, False),
            (False, True):  (True, False),
            (True, False):  (True, False),
            (True, True):   (False, True)
        }

        for av, bv in expected:
            net.set_inputs({"a": av, "b": bv})
            net.run()
            self.assertEqual((sum_.value, carry.value), expected[(av, bv)])

if __name__ == "__main__":
    unittest.main()
