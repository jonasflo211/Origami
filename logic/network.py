# folding_logic/network.py
from typing import Dict
from .pleat import Pleat
from .gadgets import Gadget

class Network:
    """Red acíclica de gadgets y pleats, con cálculo automático de orden topológico."""
    def __init__(self):
        self.pleats: Dict[str, Pleat] = {}
        self.gadgets: list[Gadget] = []
        self.deps: Dict[Gadget, list[Gadget]] = {}  # Dependencias (para topological sort)

    def add_pleat(self, pleat: Pleat):
        self.pleats[pleat.name] = pleat

    def add_gadget(self, gadget: Gadget):
        self.gadgets.append(gadget)
        self.deps[gadget] = []

    def set_inputs(self, inputs: Dict[str, bool]):
        for name, val in inputs.items():
            if name in self.pleats:
                self.pleats[name].value = val
            else:
                raise ValueError(f"Pleat {name} no existe")

    def run(self, log=False):
        """Propagación de señales usando orden topológico y verificación de ciclos"""
        visited = set()
        temp = set()
        order = []

        def visit(g):
            if g in temp:
                raise ValueError("Ciclo de dependencias detectado")
            if g not in visited:
                temp.add(g)
                for dep in self.deps.get(g, []):
                    visit(dep)
                temp.remove(g)
                visited.add(g)
                order.append(g)

        for g in self.gadgets:
            visit(g)

        for g in order:
            g.evaluate()
            if log:
                print(f"{g.name} -> {[p.value for p in g.outputs]}")

        return {name: p.value for name, p in self.pleats.items()}
