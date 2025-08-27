from logic.pleat import Pleat
from logic.gadgets import AND, XOR
from logic.network import Network

# Half-adder
a = Pleat("a")
b = Pleat("b")
sum_ = Pleat("sum")
carry = Pleat("carry")

xor_gate = XOR("XOR", [a, b], [sum_])
and_gate = AND("AND", [a, b], [carry])

net = Network()
for p in [a, b, sum_, carry]:
    net.add_pleat(p)
net.add_gadget(xor_gate)
net.add_gadget(and_gate)

# Prueba todas las combinaciones
for av in [False, True]:
    for bv in [False, True]:
        net.set_inputs({"a": av, "b": bv})
        net.run()
        print(f"a={av}, b={bv} => sum={sum_.value}, carry={carry.value}")
